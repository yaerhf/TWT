# TWT-Core — a family of substrate theories, what it derives, and its first candidate

*Yaer Aharon Haddad Fennech · Independent Researcher · hfyaer@gmail.com*

*Engine, verification suite, and the instance dossier — `TWT_foundational_paper.md` with its companion*
*`TWT_foundational_paper_companion.md`: **https://github.com/yaerhf/TWT** —*
*`pip install -r requirements.txt && python twt_test.py` reproduces every algebraic claim below.*
*The research apparatus is published with the engine, in the `apparatus/` directory of **https://github.com/yaerhf/TWT** (§6).*

---

## Abstract

This is a structural-derivation programme with one named unbuilt object, not a completed unified
theory. It defines a **family** — TWT-Core, seven axioms and one refusal — and publishes the family's
**first candidate member**, V3, built all the way down to numbers. The family says which
Standard-Model structural facts follow from which premises. It says no magnitudes: every coupling,
absolute mass and absolute scale in the programme is downstream of the driven-dissipative substrate
dynamics, which is unbuilt.

Five structural results carry the paper. The charge lattice is discrete, because winding number is an
integer. Hydrogen neutrality is an identity in the charge functional's free normalization constant. A
wavefront-locked observer inside a positive-definite Euclidean substrate reads its own kinematics as
Lorentzian. Four-dimensional space carries exactly three anti-self-dual planes, so the family makes
exactly three generation seats available. And the list of three-dimensional hosts for weak isospin
inside the substrate's rotation algebra is computed closed at three conjugacy classes, which forces
the assignment. Against this paper's own separator (§3), two of the family's ten claimed structural
facts pass its first two clauses; the empirical score is zero of ten, and the structural score is one
pass reused.

Two wounds belong to the first candidate and not to the family. The isotropic dimension-six
Lorentz-violation coefficient's natural value at that candidate's own lattice scale is excluded
unconditionally by about one order of magnitude, and by six to seven orders only under a
mass-composition assumption the same observatory's data disfavours. The electroweak crossing scale is
not derived at all, and the candidate's one computable reading of it lands a third below the measured
`sin²θ_W(M_Z)`.

One kill condition is total and family-level: if the ordering that Bell-correlation selections follow
is measured and found to be a foliation measurably distinct from the cosmic rest frame, the family is
finished.

---

## The claims

| The claim | What it rides |
|---|---|
| **The charge lattice is discrete and cannot drift.** No continuous parameter is available by which a proton and an electron could come to differ. | Matter-as-defect, and the winding character of the endorsed defect class — no candidate pick. Supplies a lattice and its protection, never a value. |
| **Hydrogen neutrality is an identity in the charge functional's free normalization constant.** With `Q = T₃ + cY`, both brackets of `Q_p + Q_e` vanish separately, so the sum is zero for every `c`. | Four structural premises (P4–P7), an entered charge anchor, §2.4's weak assignment. Not a discriminator: the incumbent's surviving `B − L` direction preserves the same sum. |
| **A wavefront-locked observer inside a positive-definite substrate reads its own kinematics as Lorentzian.** `Cl(4,0) ≅ Cl(1,3)` as real algebras, and the Lorentz generators come with it. | Two axioms — the substrate and the lock. Kinematics, not relativistic field theory; the signature is relocated, not derived. |
| **Four-dimensional space carries exactly three anti-self-dual planes, so the family makes exactly three generation seats available.** A fourth generation is structurally forbidden, not excluded by tuning mass scales. | The identification of those planes with generation seats, and an associativity premise. The seat's carrier is claimed by two readings at once and nothing local separates them. |
| **The three-dimensional hosts for weak isospin inside the substrate's rotation algebra are computed closed at three conjugacy classes, and the self-dual host is forced.** Generation-blindness, the doublet, the up-sector's chirality and V−A follow. | The weak-hosting premise, one datum read from experiment — right-handed fermions are weak singlets — and the carrier branch this candidate takes. |

Nothing on that list is a magnitude, and the family derives none. The two wounds and the kill
condition are in the abstract; both wounds belong to the first candidate.

---

## Vocabulary

- **The lock** — the mechanical coupling of an observer to the advancing wavefront (axiom S3). An
  observer does not watch the front go by; it rides the front and sees a slice.
- **The refusal** — the family's commitment that the substrate is a material medium and not a field.
- **The separator** — the three-clause criterion of §3 distinguishing a structural fact *obtained*
  from one *relabelled*.
- **The picks** — the pinned choices that turn the family into a candidate: fifteen recorded choices
  in the first one, each with its menu and what un-picks it (§5.1).
- **The wounds** — the two places where the first candidate is already measured against and behind
  (§5.3).
- **The kill condition** — the one measurement that would end the whole family rather than one member
  (§4.1).
- **The incumbent** — the Standard Model, read where it matters as an effective field theory rather
  than a renormalizable truncation.

---

## How to read this paper

Six sections. §1 states the family. §2 is what the family derives with no candidate, each result in a
fixed shape — claim, premises, scope fence, argument. §3 is the separator applied to the family's own
list, and the comparison with the incumbent priced. §4 is the falsification surface. §5 is the first
candidate. §6 is the method.

This paper carries no inline tier tags and no result numbers. Every claim's recorded tier, engine
primitive, dependency edges and premise rows live in `TWT_foundational_paper_companion.md`; the dossier
`TWT_foundational_paper.md` is authoritative for the first candidate's technical detail where the two
differ. The comparative accounting — this family priced item by item against Copenhagen, Bohm, Everett
and the incumbent — is `TWT_COMPARATIVE_LEDGER.md`. **Every file named in this paper is in the
repository root at `github.com/yaerhf/TWT`, alongside the engine** — the comparative ledger, the
family tree and the negatives ledger included; a reviewer who cannot find one has hit a broken
pointer, and that is itself worth reporting. Pointers here are invitations, not dependencies.

**Four checks, five minutes each.** (1) `git clone https://github.com/yaerhf/TWT && cd TWT && pip
install -r requirements.txt && python twt_test.py` — expect `ALL CHECKS PASSED` (on Windows set
`PYTHONUTF8=1` first). (2) `weak_su2_menu_exhaustion()` — the finite classification sweep behind §2.4;
its only mathematical input is the engine-exact structure constants of the substrate's rotation
algebra, and it returns three conjugacy classes plus the residuals of the candidates that fail to
close. (3) `charge_normalization_anchor_free()` and `charge_sector_provenance()` — the neutrality
identity with the counterfactual that breaks it, and a machine-readable partition of which primitives
in the charge block compute and which assign; the suite asserts every primitive there sits on exactly
one side, so an unclassified addition fails. (4) `alpha_em_value()`, `texture_tetrad()`,
`qcd_collider_phenomenology()` — confirm they raise rather than return.

| here | in the dossier (and the ledgers) |
|---|---|
| §1.1 the picture | §A.1–§A.5 |
| §1.2 axioms and refusal · §1.3 preferred directions | §A.6.1 · §A.6.3 |
| §2.1 charge | §C.2.1, §C.2.2, §C.2.7, §C.2.8 |
| §2.2 Lorentz kinematics | §B.1.1–§B.1.4, §B.2.2 |
| §2.3 generation seats | §D.2.4, §C.3.8 |
| §2.4 the weak host | §C.4.2 |
| §2.5 Lorentz protection | §B.1.5, and the note `D4_lattice_quartic_isotropy.md` |
| §2.6 the `B − L` triad · the two-winding carrier · the monopole boundary | §C.5.4–§C.5.6 · §A.2, §A.5.2, §C.1.3 · §B.5.2 |
| §2.7 the quantum package | §B.3, §B.4 |
| §3 the separator · the comparative accounting | `TWT_COMPARATIVE_LEDGER.md` |
| §4.1 kill condition · §4.2 prohibitions · §4.3 knowability · §4.4 what is not claimed | §A.6.2 · §E.3.1 · §A.6.5 · §D.5, §E.2.3 |
| §5.1 the picks | §A.6.4, and `TWT_FAMILY_TREE.md` |
| §5.2 the numbers | §E.2.1, §E.2.3, §C.1.2, §C.3.5, §C.3.11 |
| §5.3 the wounds | §E.3.5, §C.4.5, §D.4.3 |
| §6 the method | companion Section 6, and `TWT_NEGATIVES_LEDGER.md` |

---

# §1 — The family

## 1.1 The picture, once

Time is a wave, and we are riding it.

The substrate is a four-dimensional Euclidean material medium carrying a wavefront that advances along
one distinguished axis. The lock is what makes `c` a property of the medium rather than a coincidence
of the observer: `c` is the front's advance rate. Applied once it converts winding-per-length into
oscillations-per-second; applied twice it is the `c²` of `E = mc²`, and the universality of that factor
is the monism of the substrate — one medium, so one conversion, so inertial and gravitational mass are
one quantity rather than two that happen to agree.

Matter is a **defect** of the medium — a protected pattern, stabilized by topology rather than by a
binding energy — and a defect has several independent axes on which it can be defective: its winding,
its deficit of carrier rotation, an internal rotation perpendicular to the advance, a notch in the
amplitude. Collapsing those into one scalar is the recurring error in reading this picture. Mass is the
frequency of the defect's rotation in meta-time. From inside the wavefront — the frame every
measurement is made in — matter reads as something positive over a vacuum at zero; from outside, the
vacuum is the full carrier and matter is where the carrier is missing. Both are appearances of one
thing, and the one thing is the defect. The hole is a picture and so is the positive; neither is a
premise, and no argument here reasons from either.

Two consequences of the lock bind everything that follows. **The inside frame is where data comes from;
the outside frame is where derivations are done** — reasoning *from* the inside view imports what is
supposed to be explained. And **the medium has two scales that must never be collapsed into each
other**: the grain layer, whose constituents are the medium's smallest parts, and the emergent cell
layer, where solitons and hadrons live. The two-layer architecture is a commitment of the family; the
*value* of the grain scale is not, and in the first candidate it is back-fitted from the measured
Newton constant.

## 1.2 Seven axioms and one refusal

A theory that has all seven is a member of the family. A theory that drops any one of them is a
different theory. The seven are stated in the form the family charter fixes them, verbatim.

> **S1a — The substrate.** Reality is a four-dimensional Euclidean material substrate; everything
> else the theory talks about is a property or a pattern of that substrate.

> **S2 — Meta-time.** There is a second time, `τ₅`, whose direction squares to −1, and the state of
> the substrate advances in it.

> **S3 — The lock and the slice.** The substrate carries an advancing wavefront; an observer is
> mechanically locked to it and can only ever see a slice, so a preferred foliation exists whether
> or not anything inside the slice can see it.

> **S4 — Matter is a defect.** A particle is not a piece of stuff sitting in the medium; it is a
> protected pattern of the medium itself — a defect.

> **S5 — The medium is driven.** The advance is one-way and constitutive: the medium is not resting
> and not merely relaxing toward rest, it is driven.

> **LS — The local state.** The medium's local state at each site — for any grain structure a family
> member realizes — is a 4D orientation — six real parameters; whether its `ℤ₂` sign lives in the
> state or in the emergent covering sector is a recorded open branch. The continuum field inherits
> this target unchanged. The wave's advance direction splits its generators into wave-parallel and
> wave-transverse.

> **B-6 — The preferred foliation is the cosmic rest frame.** The foliation of S3 is not left free:
> it is the frame in which the cosmic microwave background is isotropic — the comoving frame.

> **THE REFUSAL — the substrate is a material medium, not a field.**

**On S2: the clause places a complex structure, not a signature.** The observer's time is the advance
axis, which squares to `+1`, and §2.2's arc is independent of S2 outright. The substrate algebra is
central simple over the reals, so no *central* element squares to `−1`; adjoining a generator of
negative square is what makes the extended algebra carry a central copy of ℂ rather than splitting into
a real direct sum, and the central unit `E = I₄e₅` satisfies `E² = e₅²` exactly. What S2 buys is the
substrate's **one global phase**, on which the colour carrier, the carrier structure along the advance
direction and the mass floor are built. Negating it in the engine changes eighteen primitives and four
of the suite's ten modules, and nothing in §2 — which is why §2 read alone appears not to need it.

**On LS.** The axiom is witness-free: it fixes the size of the local state for any grain structure, and
each member re-witnesses it on its own grain. Its `ℤ₂` clause is deliberately not decided — both
branches deliver identical windings and identical fermionic-quantization structure, so the observed
fermionic character of matter cannot pay for the choice. The discriminators, if any exist, are the
substrate's own bond energetics, the sign-defect sector, and the emergent covering construction.

**On B-6.** The safe option was available and was declined: leave the foliation unnamed. A theory with
an unnamed preferred foliation cannot be caught, because "there is a frame, somewhere" survives every
measurement. Naming it as the comoving frame turns a metaphysical posture into a target, and that
target is the family's kill condition (§4.1).

**On the refusal, and its scope.** The rotor field running through the first candidate's development
and through the engine is **instance-level description**, not the ontology; an argument that needs the
field to *be* the world is not a family-level argument. A field is refused only as a *fundamental
description of what the world is made of*, never as a mathematical description of an **emergent
property** of the medium, the way temperature is a field-description of molecular motion — which is why
the field formalism works as well as it does. Two things ride that reading as commitments: the
grain-to-cell map is a real physical relation, plausibly driven by the wave, rather than a bookkeeping
device between two levels of description; and the cell's first description is an emergent pattern. The
refusal is about what the substrate *is*, not about whether it is grainy — graininess is a preferred
direction, not an axiom.

## 1.3 Preferred directions, and what they are not

Eight further commitments are endorsed as highly plausible and are **not** part of the definition. A
candidate that goes the other way on any of them is still a member of the family:

grain discreteness · Skyrmion-class defects · carrier structure along the advance direction · the
practice of anchoring on a measured constant and back-fitting · the Koide amplitude `c = √2` · the
identification of a defect's mass with its vacuum-subtracted rest cost · generations as the
anti-self-dual triple with an associativity premise · and the **weak-hosting premise**: that weak
isospin is hosted by a three-dimensional `su(2)` inside the substrate's own rotation algebra at all.

A large block of §2 is derived *given* one of these endorsements, and those results are family property
only in that conditional sense: they stand or fall with the endorsement they consume, and each result
below names the one it consumes.

---

# §2 — What the family derives with no candidate

Six results and one package, in a fixed shape: the claim, the premises it is *given*, the scope fence
saying what it is *not*, then the argument. Each is scale-free — the family has zero earned dimensionful
scales, and everything here is a sign, an integer, a dimension, a ratio or an algebra identity. That is
the shape of what a scale-free axiom set can deliver, and §4.4 states the corresponding limit.

## 2.1 Charge: a discrete spectrum, a neutrality identity, and an assignment

**C1. The charge lattice is discrete and protected against drift.** `π₃(S³) = ℤ`: winding number is an
integer, so no continuous parameter is available by which a proton and an electron could come to differ.
*Given:* S4, and the winding character of the endorsed defect class — that much of the endorsement and
no more, since integer-valuedness is what any winding-class defect supplies. No candidate pick.
*Not:* a value. The integer supplies a baryon number, that lattice, and its drift protection. A
re-anchored or re-arranged candidate inherits C1 unchanged.

**C2. Hydrogen neutrality is an identity in the charge functional's normalization constant.** Two
one-line computations in the substrate algebra carry it. For a grade-three blade `B`,
`B̃ · e₄ · B = (±1)·e₄`: the advance-bearing trivectors `e₁₂₄, e₁₃₄, e₂₃₄` return `+e₄`, the spatial
`e₁₂₃` returns `−e₄`, so **the two orbits carry opposite signs** — the whole content of the hypercharge
bracket — and hypercharge is constant across each weak doublet by Schur's lemma. And those three
compose to the advance axis, `e₁₂₄ · e₁₃₄ · e₂₃₄ = e₄`, **alternating** over the six orderings, so the
sign belongs to an *oriented* triple and an orientation convention must be named wherever it is used.
Then with `Q = T₃ + c·Y` and `c` free,

> `Q_p + Q_e = [2T₃(u) + T₃(d) + T₃(e)] + c·[3Y_Q + Y_lep] = 0 + c·0 = 0`

**identically in `c`.** The isospin bracket vanishes because `uud` plus the electron is one complete
quark doublet plus an up-versus-down-opposed pair; the hypercharge bracket because the two orbits carry
opposite signs and the trivector orbit supplies the factor of three — the `3 × 1/3 = 1` arithmetic,
written throughout in the normalization `Y_lep / Y_Q = −3`, three times the conventional hypercharge
scale. The same computation returns the neutron–neutrino cancellation and singles out `uud` uniquely
among the four three-facet composites.
*Given:* **four named structural premises plus an entered anchor** — measured electric charge is the
eigenvalue of *one* universal linear generator across all sectors (P4); the charge is
chirality-independent per defect (P5); the inside-frame identification of the proton with the
three-facet composite `uud` (P6); the cross-sector weak-isospin alignment placing the charged lepton in
the slot opposite the doubly-represented quark (P7). P7 is posited, in the engine's own literal:
flipping the lepton slot alone gives `+1`, the quark slots alone `−1`, only the global flip is a
convention. The isospin bracket further inherits §2.4's weak assignment, so C2 is family property only
in §1.3's conditional sense — a candidate hosting weak isospin outside the substrate's rotation algebra
re-derives this identity on its own host or loses it. C1 inherits nothing and stands either way.
*Not:* a discriminator. The `10⁻²¹` neutrality measurement tests the identity rather than calibrating
it, but the incumbent's anomaly structure protects the same sum by structure, so passing it separates
nothing. The measurement that *would* separate is the neutron's (C4) — with one caveat that belongs in the same
breath: the tightest neutron-charge figure is carried over from the same neutrality-of-matter
experiment by an assumed charge-conservation identity in neutron beta decay, so the genuinely
independent leg is the cold-neutron deflection measurement, and it is the weaker one.

**C3. No per-defect charge outside `{0, ±1/3, ±2/3, ±1}` is reachable in the algebra at all, and a lone
facet is not a valid configuration.** A lone facet is one orthogonal component of one circular winding;
the three facets are one object, not three bound together, and the topological reading is the formal
shadow of that — there is no smooth map `S³ → S³` of degree one third. The absence of free fractional
charge here is a statement about what shapes exist, not a force holding something in.
*Given:* the orbit's three-plus-one structure plus an **entered homomorphism**. Blade composition is
multiplicative and charge is additive, so passing between them needs a homomorphism, and that
homomorphism — one third of the integer winding per facet — is entered, not computed.
*Not:* a confinement dynamics, and not the short-distance behaviour of the same sector, which is the
family's sharpest structural exposure (§4.4). Composite charges are integer sums of those units and are
not confined to the list: the engine's three-facet table returns `+2` for `uuu`, the `Δ⁺⁺`. The algebra
fixes the unit, not the total.

**What is assigned rather than derived.** Which state carries `+2/3` and which `−1/3` is an assignment:
the winding chain supplies integer-valuedness and protection, the charge functional supplies the
normalization, the values are entered, and the engine partitions the two machine-readably. Two
counterfactuals are runnable: requiring one universal `c` across both orbits forces `Q_p − Q_n = 1`
exactly and leaves the absolute anchor free; and with the factor of three deleted, the only anchor
admitting one universal `c` is a half-charged proton with a negatively charged neutron. That factor is
what makes an integer nucleon anchor compatible with the premise at all — substrate-specific, not
generic.

**Against the incumbent, at equal depth and against its best version.** In the one-generation Standard
Model with no right-handed neutrino, Yukawa gauge invariance together with the `[SU(2)_L]²U(1)_Y` and
`[U(1)_Y]³` anomaly conditions fixes the hypercharge ratios uniquely, and the observed charges come out
— a structural earning. What that route quantizes depends on the completion: with right-handed neutrinos
`U(1)_{B−L}` is anomaly-free and gaugeable, and a one-parameter dequantization
`Q = Q_SM + ε(B − L)/2` then survives for Dirac neutrinos at any number of generations, closed only by
an explicit breaking — a Majorana mass, or a single right-handed neutrino rather than three. This family
forbids the Majorana mass outright (§2.6), so it argues in the completion where the incumbent's route
does **not** close, and three caveats travel with that sentence wherever it is quoted: the
one-generation model with no right-handed neutrino does fix the charges; a single right-handed neutrino
restores quantization with no Majorana mass anywhere; and the surviving flat direction is `B − L`, which
gives the proton `+1` and the electron `−1` and therefore **preserves `Q_p + Q_e = 0` exactly** — what
it charges is the neutron, bounded at the `10⁻²¹` level, on an average whose tightest input is not
independent of the atom-neutrality measurement above. **So hydrogen neutrality specifically is
anomaly-protected either way.**

One disclosure belongs here because it cuts the other way: the right-handed hypercharge values this
family uses are pinned in its own engine by **the incumbent's anomaly package, imported and
registered** — the same machinery the comparison is drawn against — with the family's own premise
resolving only a relabelling the neutrality identity is invariant under. **Where the incumbent derives
those values, this family borrows the derivation.** At full strength against this family: the two
one-parameter charge families *coincide as assignments*. The free normalization here maps onto the
incumbent's surviving `B − L` direction, both preserve the two neutrality sums identically, and in both
it is the neutron's charge the free parameter moves — so nothing in the charge *values* separates the
frameworks, and "nothing was tuned" is true of the incumbent in the same sense by the same identity.
What separates them is the price — topology and one orbit, against anomaly conditions on a chosen
content in a chosen completion — and, sharper, **what closes the free direction**.

**C4. Under this family's own closure the neutron's charge is a prediction: exactly zero.** The
wave-decoupled sterile neutrino must carry zero hypercharge, which derives the normalization rather than
entering it.
*Given:* exact `B − L`, and the Dirac partner's placement. Unconditioned, this family consumes a charge
anchor exactly as C2 records and `Q_n = 0` is input; under the closure that anchor is **no longer
consumed**, and only then does the neutron's charge become an output. The closure is a
framing-supported inference with its own stated failure condition.
*Not:* read from experiment. **The closure is structural.** Exact `B − L` forces the Dirac partner into
the substrate's wave-decoupled ideal, whose decoupling is a property of the algebra, not an observation,
so the substrate has no slot for a hypercharged singlet to occupy. Had the closure instead *read* the
sterility off experiment, the incumbent would close its own flat direction by the same reading and the
parity would return, exactly as it does for hydrogen. (§2.4's right-handed-singlet datum is a separate
consumption, and this closure does not ride it.) A nonzero neutron charge at any level splits the two
frameworks; its bound today is at the `10⁻²¹` level, on an average whose tightest input is not
independent of the atom-neutrality measurement above — the genuinely independent cold-neutron
deflection leg is weaker, at 68% confidence — and this family's conditional prediction sits at
exactly zero, where the incumbent's surviving direction is closed by nothing but the measurement itself.

**Where this sits among structural routes.** A grand-unified embedding or a Dirac monopole would supply
the quantization structurally rather than as a condition on a chosen representation content, and Pati
and Salam's fourth colour reads lepton number as the fourth value of the colour index — the same 3+1
arithmetic (*Related work*). So this family does not uniquely earn the 3+1 split; it **joins a class of
structures that furnish it and is the only member of that class that furnishes it without buying a
group**, where that scheme pays with an enlarged gauge group, a breaking sector, and quark-to-lepton
gauge vertices whose flavour-violating meson decays are experimentally constrained. What is distinctive
is the price, not the possession — and the price has a matching cost (§4.4): no gauge dynamics is
delivered with it.

## 2.2 Lorentz kinematics from four axioms

**C5. A wavefront-locked observer inside a positive-definite substrate reads its own kinematics as
Lorentzian, and the Lorentz algebra comes with it.** Take `γ⁰ := e₄`, `γʲ := e₄ e_j` — the only
ontologically distinguished multivector plus the three spatial generators. Then `(γ⁰)² = +1`,
`(γʲ)² = −1`, all anticommutators vanish, and the map extends to a real-algebra homomorphism between two
sixteen-dimensional simple algebras, hence an isomorphism:

> **`Cl(4,0) ≅ Cl(1,3) ≅ M₂(ℍ)` as real associative algebras.**

*Given:* `{S1a, S3}`, plus `{S4, S5}` for the matter-sector extension — four axioms, no endorsement, no
candidate pick, no fitted number. The only external mathematics is the real classification of the
`Cl(p, q)` at `p + q = 4`.
*Not:* a derivation of the signature — and the *spatial* legs are posited too, which is the sharper
half and is stated here rather than left to be found. The lock puts the observer's timelike direction
on the advance axis; that is an axiom, and every theory must locate its signature somewhere. But a
Clifford algebra does not remember its quadratic form: the form is read off a **designated**
grade-one subspace, and two designations containing the advance axis are available — `{e₄; e₄e_j}`,
giving `(1,3)`, and `{e₄; e_j}`, the substrate's own generating set, giving `(4,0)`. Mixing them is
algebraically forbidden, so the choice is a **binary**, and it is the binary that decides Lorentzian
against Euclidean. Nothing in the lock forces it. What the wavefront geometry delivers is therefore
**an algebra identity, not a forced signature**; the observer tetrad is posited, and given it the
signature and the Lorentz generators follow. Read strictly, the family **relocates** the signature
and gets a theorem in exchange. One posit, two facts.

`Cl(3,1)` and `Cl(2,2)` are both `≅ M₄(ℝ)`, a different real algebra, so the construction lands on a
nondegenerate Lorentzian partner and not the split form; what is convention-independent is the
*pattern*, one generator squaring one way and three the other rather than two and two. The observer's
time is carried by `γ⁰ = e₄`, with `e₄² = +1`; the meta-time generator does not enter, so the arc is
independent of S2. The boost and rotation generators are `K_j = ½ e_j` and `J_i = −½ e_{jk}` — grade-one
and grade-two elements of the *same* algebra — closing on `so(1,3)` with the correct signs, and that the
boost generator is grade-one and not a plane is what makes it hyperbolic rather than circular:
rapidities add and velocities compose by Einstein's rule exactly, rather than by the wrong-signed,
unbounded law a rotation of a Euclidean plane would give. Two boosts commute to a rotation,
`[K_i, K_j] = −ε_{ijk} J_k` — Thomas precession as a closure sign rather than an added correction — and
an observer's three spatial axes are `γʲ = e₄ e_j`, **bivectors** each containing the advance direction,
which is why the substrate's own geometry is not visible from inside. This is the family's cheapest
result: `gammas()`, `so13_closure_signs()`, `thomas_KK(1,2)`, `boost(1)`, `rotation(1,2)` are
parameterless calls returning exact multivectors, a machine-checkable difference from every gravity route
in the corpus, each of which takes a fitted default or raises.

**Four fences travel with the result.**

1. **Kinematics, not relativistic field theory.** The construction delivers signature, the Lorentz
   generators, Thomas precession and the mass shell, and no relativistic quantum field theory. The
   Osterwalder–Schrader debt is registered and unpaid: no reflection positivity has been exhibited for
   this substrate, so any statement that the Euclidean substrate *inherits* a Hilbert space, a vacuum
   and a self-adjoint Hamiltonian by virtue of being Euclidean is asserted, not derived. There are two
   discharges — exhibit the positivity, or say so at every inheritance site — and the second is what is
   done here.
2. **The antecedent is an axiom, not an endorsement.** The conditionality is S3, inside the definition;
   applying §1.3's conditional clause to it would demote an axiom to a preference.
3. **Lorentz-covariant in the reading, not Lorentz-invariant in the ontology.** S3 and B-6 put a
   preferred foliation under everything; the standing objection that this violates relativity is
   answered by a published reply with no load-bearing use in the corpus, not by a derivation of our own
   (*Related work*, which also records the external precedent for the necessity of something like the
   lock, and that it is not a derivation of it).
4. **The equivalence of inertial observers is not derived here.** What this subsection delivers is an
   algebra and one locked observer's reading of it. What makes Lorentz invariance *physical content* is
   that inertial observers agree on the laws, and that requires the substrate's emergent dispersion to
   actually be `ω² = c²k²` — the unbuilt dynamics; §2.5 and §5.3 carry the exposure, and §2.5's
   one-medium argument reaches the dimension-four relative-boost coefficient only. The algebra says as
   much on its own face: the boost generator is grade-one, so conjugation by `B = exp(ζ e₁/2)` is not a
   rotation of the substrate and does not preserve its Euclidean quadratic form — the grade-two norm
   picks up `cosh²ζ` on exactly the components sharing the boost direction, engine-exact
   (`boost_projection_leak_identity`). **A substrate boost is therefore not a substrate isometry**, and
   the hyperbolic behaviour named as a feature above is that same fact read from the other side. That
   two locked observers in relative motion read the same dynamics is owed.

## 2.3 Exactly three generation seats

**C6. Four-dimensional space carries exactly three anti-self-dual planes, so the family makes exactly
three generation seats available, and a fourth generation is structurally forbidden rather than excluded
by a tuning of mass scales.** Grade two is six-dimensional; left multiplication by the pseudoscalar
`I₄ = e₁e₂e₃e₄` is an involution on it — `I₄² = +1`, a real duality and not a complex unit — so grade two
splits into self-dual and anti-self-dual halves, and the trace of the projector `(1 − I₄·)/2` gives the
dimension directly: `dim Λ²₋(ℝ⁴) = 3`, **computed rather than asserted over a hand-written list** — the
same six-dimensional space that supplies the local state of §1.2, read through its own duality.
*Given:* the reading of the three anti-self-dual planes as **generation seats**, a preferred direction
and not an axiom; and an **associativity premise** the family must own — drop associativity and the
octonions offer seven imaginary units, which is not an outside objection but the family's own named
alternative (*Related work*). Frobenius's theorem enters as a structural remark through that premise,
not as the operative exclusion.
*Not:* a statement about the seat's **carrier**. Read as an internal action rather than as a bare index
set, the anti-self-dual triple is claimed by at least two candidate readings at once — three generation
seats, or a second weak factor gripping exactly the half of the even algebra the first annihilates, and
it may be both or neither — and nothing at the level of the local algebra separates them; the
computation that would is the quantization of the defect's collective coordinates, and it is not built.
What the count is read through is not the triple but the meta-time phase, with the three planes as its
index set, so the count does not sit directly on the carrier question; but whether an index set survives
being gauged is a passage this candidate owes and has not written, so the insulation is a claim about
where to look, not a result.
*Also not:* which seat nature occupies, or why. The count is a fact about four-dimensional space; the
occupancy is not addressed.

## 2.4 The weak host: a menu computed closed

**C7. The three-dimensional Lie subalgebras of the substrate's grade-two rotation algebra `so(4)` are
exactly three up to conjugacy, and the self-dual host is forced.**

> **SD** — the self-dual chiral factor · **ASD** — the anti-self-dual one · **the diagonal `so(3)`
> class** `{Stab(v) : v a unit vector}`, of which the `e₄`-free spatial-rotation triple is one member.

*Given:* the **weak-hosting premise** — that weak isospin is hosted by a three-dimensional `su(2)`
inside the substrate's own rotation algebra at all. It is not derived anywhere; it is one of §1.3's
preferred directions, and a candidate hosting weak isospin elsewhere is untouched by anything here. And
the **datum**: no right-handed charged current is observed at any accessible energy, so the right-handed
fermions are read as weak-isospin singlets — read from experiment rather than tuned, and reversible,
since an observed right-handed charged current reverses it. And the carrier branch below.
*Not:* **first discovery.** That weak `SU(2)` is one chiral half of a four-dimensional rotation
algebra is the founding observation of the graviweak literature (Nesti & Percacci 2008;
Alexander, Marcianò & Smolin 2014 — engaged in full under *Related work*, where the delta is
stated: those constructions complexify and select the chiral half by a vacuum expectation value,
this one is a real split with no vacuum expectation value anywhere). What this claim adds over
them is the closure of the menu and the discriminator, not the identification. Also not a
classification of larger hosts. The sweep covers *three-dimensional* subalgebras, so a
candidate hosting weak isospin in a larger structure — a two-scale host — is outside its scope rather
than refuted by it. And not a statement about a label carried by a defect's collective coordinates
rather than by the local state; that is a different construction, and it is unbuilt.
*Given it:* generation-blindness, the doublet structure and the up-sector's chirality follow — as does
V−A, named last rather than first, because purely-left-handed coupling is what the entered datum says
and `V − A` is that same statement in Dirac-bilinear form. The first three are consequences in domains
the datum did not fix; V−A is the datum wearing different notation. Divergence at this node therefore
happens one level down, at the endorsement.

**Why the classification closes.** Its only mathematical input is the structure tensor, which on an
orthonormal basis of either chiral factor is exactly `c·ε_{ijk}`. Total antisymmetry alone forces three
facts about each factor — no two-dimensional subalgebra, simple, all automorphisms inner — and Goursat's
lemma then reduces the classification of three-dimensional subalgebras of a sum of two such factors to a
finite sweep over projection and kernel dimensions, which returns those three cases and no others. Two
structures the geometry might seem to offer are not subalgebras at all: the parity-odd `e₄`-bearing
triple, and every proper handed mixture of the two chiral factors, which fails to close because the
factors carry opposite structure-constant signs. The engine returns the failing residuals alongside the
classification.

**ASD is not a rival; it is the same assignment mirrored.** The two chiral factors are distinguished
only by the sign of the pseudoscalar, and an orientation-reversing frame reflection exchanges them
exactly while fixing the diagonal class and flipping that sign — verified on three inequivalent
reflection vectors including a non-basis one, so the exchange is generic rather than an artefact of the
basis. Counted up to the automorphisms of `so(4)` the menu has two entries, not three: one member, two
descriptions. If some independent object ever pins the substrate's orientation this reverts and ASD
becomes a real branch; nothing in the corpus pins it.

**The diagonal class is excluded by data — and not by the datum one would expect.** Every grade-two
element commutes with the pseudoscalar, so every candidate preserves both Weyl halves of the spinor
module. Restricted to the half a single-Weyl neutrino occupies, the diagonal class and SD span the
**same** three-dimensional algebra, so a left-handed single-Weyl neutrino cannot tell them apart. The
discriminator is the *other* half: SD annihilates it outright — that half is a weak singlet sector —
while the diagonal class charges it exactly as strongly as the first, which would make the right-handed
fermions a second weak doublet sector at full strength, and they are not. The family supplies the
occupancy the argument needs from its own structure: the charged lepton occupies both Weyl ideals, and
that two-ideal occupancy is its Dirac-mass channel, so the other half is not empty and the datum bites.

**The conditioning of that excluding step.** Which module the host acts on is an open branch for this
family, and the discriminator's verdict *moves with it* — computed: on the two candidate carriers the
image of the self-dual factor on the right-handed half is empty on one and three-dimensional on the
other, so on the second the datum would refute the assignment instead of confirming it. **The
elimination holds given the carrier branch this candidate takes**, and an arc that takes a structural
pass with an open module inside its excluding step is reported at that strength, not above it.

**C8. Which side the host acts on is computed, not assumed: the body frame.** The local state is a full
four-dimensional orientation, so an algebra can act on it from either of two sides, and the two are not
interchangeable. The observer's rotations and boosts act from the space frame; weak isospin acts from
the body frame — an internal reorientation of the state relative to itself — and the two actions commute
identically, by associativity alone and for every realization of the lock. That is what makes the weak
label a Lorentz scalar rather than something a boost of the apparatus could turn, and why the side is
not a free convention: a host acting on the observer's own side is not such a scalar, and after the lock
that side offers a centralizer only two real dimensions wide, and two commuting directions are never an
`su(2)`.
*Not:* a settling of the **module**. The local state's internal action has two candidate modules on the
books, and the commuting identity is an identity of the algebra acting on itself, which is what makes it
realization-blind; on the even-subalgebra reading an observer boost realized as a vector — how §2.2
realizes it — does not preserve that module at all, so there the invariance is inherited from the
algebra rather than tested on the module. The side is settled; the module, and the realization in which
the test is non-vacuous, are not. What the side does *not* touch is the discriminator above: the two
chiral factors sit inside the two central ideals of the even subalgebra, so that discriminator returns
the same table whether the generators act from the left or from the right — side-independent.

**The fourth fence, on the level rather than on the construction.** Everything above is a statement
about *labels and selection rules*: which states sit in which doublet slot, which chirality couples,
which generation the coupling is blind to. **There is no gauge boson anywhere in this family.** What is
classified is the host algebra of a label carried by the local state, not a chiral *spectrum*: `V−A`
here means the chirality structure of a current, not the interaction that current would enter, and the
gauge sector sits on §4.4's field-reclamation debt, un-reclaimed. So the lattice no-go a field theorist
reaches for first does not bind this construction. Nielsen and Ninomiya's theorem quantifies over
lattice theories with a free quadratic fermion action and a conserved chiral phase; no fermion field is
defined on this substrate at all — matter here is a quantized soliton, and the engine carries no
anticommuting structure anywhere — so **the hypotheses have no referent rather than being evaded**.
That is a statement that the family has not yet reached the place where the theorem applies, since no
chiral spectrum has been exhibited from the substrate either; the passage that would reach it is
unwritten, and it is the same debt §4.4 names as field reclamation. A member that introduces a
fundamental lattice fermion field inherits the theorem in full and owes one of its known evasions.

**On the accounting.** Self-dual versus anti-self-dual is not a bit at all, since the two are related by
a relabelling, and chiral versus diagonal is not a free choice, since measurement settles it. What the
sector costs is the named structural premise plus one empirical bit, and the bit is one the family reads
rather than tunes.

## 2.5 Lorentz protection: what one field buys, and what an arrangement buys

**C9. The dimension-four relative-boost Lorentz violation is structurally zero rather than tuned.** All
matter species inherit the substrate's one light cone exactly because they are defects of one medium.
Matter is not `N` independent fundamental fields each with its own kinetic term, so there is no
independent coefficient in which a relative-boost violation between two species could live: different
rest masses, one light cone.
*Given:* S4 — and **one substrate assumption that is not engine-checkable**: that one medium generates
all the radiative corrections, so the induced coefficient really is common to every species. The
family's own picture argues against it. A defect is defective on several independent axes at once
(§1.1), and species differing along those axes generically couple differently to the medium's modes; one
medium supplies one *source* of corrections, not one *coefficient*. A universal shift needs a further
symmetry argument — a Ward-type identity forcing the leading correction to be independent of a defect's
internal structure — and no such identity is exhibited here; that is the shape of what is missing, not a
demonstration that nothing else could do the work. The nearest worked substrate programme in the
literature reaches the opposite conclusion for its own medium (*Related work*).
*Not:* a proof that the substrate is exactly Lorentz-invariant under its interacting dynamics; that
stays open. And not a closure of the dimension-six residual either way. What C9 does is collapse a
generically fatal problem about `N` fields into one tractable question about one medium: programmes
treating Lorentz invariance as emergent from a preferred-frame substrate face a radiative-naturalness
problem — with a hard, frame-dependent cutoff, loops feed dimension-six violation down into
dimension-four marginal operators at order `10⁻³`–`10⁻²`, missing the matter-sector bound by seventeen
orders. That obstacle presupposes `N` independent fields with `N − 1` relative-speed observables, and
this family denies the precondition. So the dimension-four half is closed **conditional on a universality
claim about substrate self-energies**, and the obstacle is deferred rather than defused.

**C10. On a D4 arrangement, the leading rotational anisotropy of the polarization-averaged dispersion
sits at dimension eight — reached, not merely bounded.** The automorphism group of the D4 root system
has order 1152 — it is `W(F4)`, invariant degrees `{2, 6, 8, 12}` — so its space of degree-four invariant
polynomials is one-dimensional, spanned by `(k²)²` alone: for any dispersion kernel invariant under that
point group and analytic in `k` there is no anisotropic quartic at all, and the degree-six invariant
space is two-dimensional, which places the anisotropy. This is not generic to lattices — the
simple-cubic lattice admits a two-dimensional degree-four invariant space containing `Σ kᵢ⁴`. **Two
countings run together here: degrees are polynomial degrees in the dispersion relation, dimensions are
operator dimensions in Lorentz-violating effective field theory, and the correspondence is degree four ↔
dimension six, degree six ↔ dimension eight.**
*Given:* an **arrangement**, which is a candidate pick and not a commitment of the family — and five
premises, each of which restores dimension-six anisotropy or voids the theorem if it fails.
 (i) *That a derivative expansion exists.* A non-analytic driven-dissipative memory kernel — the
 family's own unbuilt object — is not covered by a polynomial-invariant argument at all.
 (ii) *That the full point group including triality acts.* The reflection subgroup alone has a
 three-dimensional degree-four space, and the second shell's two sub-orbits are each anisotropic,
 cancelling only at equal weight, so a coupling weighting triality-related orbits unequally restores the
 anisotropy.
 (iii) *That the ordered state preserves the point group.* The instance's canted vacuum breaks it, and
 what survives is a species-universal part absorbed by rescaling plus a space-fixed, sidereal residual
 that remains an open question.
 (iv) *That the kernel is a scalar in the internal index.* The theorem governs the polarization-averaged
 dispersion and does not cover matrix-valued kernels, which the point group cannot close.
 (v) *That the symmetry operative on the sector the result is quoted for is that full point group rather
 than the subgroup a driven steady state leaves intact.* The theorem is proved in four Euclidean
 variables, while leading rotational anisotropy is a three-dimensional claim and a driven medium singles
 out its advance axis; the stabilizer of that axis has order 48 and restricts faithfully onto the full
 octahedral group, whose degree-four *spatial* invariant space is **two**-dimensional and contains
 `Σᵢ kᵢ⁴`. At the driven group an anisotropic spatial quartic is therefore *permitted*, and what excludes
 it is not the driven symmetry but a full-group property of the coupling: the bonds form a single
 equal-weight orbit of the full point group, which forces the spatial fourth moment isotropic on every
 3-plane. Any driven-sector coupling whose bond weighting fails to be constant on the full orbit would
 restore dimension-six spatial anisotropy. **This is a permission, not a demonstrated term** — no kernel
 written down in this programme exhibits it — but it is the premise on which the headline generality
 rests.
*Not:* novel. That the D4/F4 lattice suppresses rotational-symmetry-breaking cutoff effects relative to
the hypercubic lattice is established lattice field theory, and **any claim of novelty for the result
does not survive contact with that literature** (*Related work*). What is claimed is narrower: the
generality of the proof — one-dimensionality of the degree-four invariant space for *every* analytic
point-group-symmetric kernel at once, via the `W(F4)` invariant degrees, with the triality premise named
— and one transfer, that Lorentz-violation effective field theory already uses point-group protection at
dimension four but appears not to have carried the observation that the argument fails at dimension six
for the hypercubic lattice and holds for D4.

**What neither reaches** is the rotationally invariant dimension-six residual: not a relative-boost
observable, so C9 does not apply; not an anisotropy, so C10 does not apply; and at dimension six a
species-universal coefficient is not removable by any rescaling, because the induced velocity shift is
momentum-dependent. Its coefficient is set by the substrate's own strain-mode dispersion, an object the
engine gates. It is this programme's sharpest empirical exposure, and §5.3 states it as one.

## 2.6 Three prohibitions from one conservation law

**C11. `B − L` is exactly conserved, and its carrier is two independent integer windings.** The same
`3 × 1/3 = 1` arithmetic that makes §2.1's hypercharge bracket vanish makes the gauge-trace anomalies of
`B − L` vanish across one generation: three quarks at `B − L = 1/3` plus one lepton at `B − L = −1` sums
to zero per generation, and `Tr[T_a T_b · (B − L)] = 0` on the corresponding generators. That is not a
tuning of quantum numbers; it follows from the orbit's structure. Stated precisely, because the engine's
own provenance note is sharper: the singlet-inclusive sums are **insensitive to the colour multiplicity**
— the quark and conjugate contributions cancel pairwise — so what they consume is the *pattern*, not the
number three. **The colour count and the anomaly arithmetic are therefore not two independent loads on
the orbit; they are one structural feature used twice.**

The carrier: the local state is a four-dimensional orientation, and `π₃` of that state class is `ℤ ⊕ ℤ`
— **two independent integer windings**, each a homotopy invariant and therefore each conserved
separately under any smooth deformation. The count is the chiral one — the orientation class factorizes
into two `su(2)` factors, one winding integer per factor — and the family's working basis is a change of
basis of that pair, into a subgroup winding (leptons wind into the diagonal `Spin(3)`) and a coset
winding (baryons wind into `Spin(4)/Spin(3)`). The count is **blind to the family's undecided `ℤ₂`
clause**, because a double cover is an isomorphism on `π₃`, so it reads the same on both branches of
§1.2's LS note and costs nothing there. The *source* of the protection differs from the incumbent's: the
Standard Model keeps `B − L` exact and gets `B` and `L` separately as accidental symmetries of the
renormalizable Lagrangian — real structural earnings — but they are accidents of the dimension-four
truncation, and the higher-dimension operators an effective theory admits break them, while here they
are homotopy invariants surviving any smooth deformation whatever operators are present. What is *not*
different is the non-perturbative channel: **this family's `ΔB = ΔL = 3` selection rule is the
incumbent's own rule.**

**C12. Three Standard-Model "extras" collapse into one substrate fact.** *No proton decay* — baryon
number is one of those two integer windings, non-perturbative violation respects `ΔB = ΔL = 3`, so a
channel taking one baryon to none is forbidden, and **the proton is absolutely stable in the smooth
sector** at any lifetime: the family's one distinctive forward bet against grand unification, which
expects decay at *some* level. *Dirac neutrinos* — with `B − L` exactly conserved a Majorana mass term
is forbidden, carrying `Δ(B − L) = −2`. *No neutrinoless double beta decay* — the same conservation law
forbids the signature.
*Given:* the defect class, a preferred direction and not an axiom; and the instanton-plus-index-theorem
pair, **a registered external import applied at the effective level**, with the *rate* face gated.
*Not:* obtained from substrate topology. **That selection rule is the incumbent's, quoted.** It is the
standard instanton / index-theorem result, and the objects the theorem needs — a gauge field to be
self-dual, a Dirac operator coupled to it — are exactly the objects §2.4 argues have no referent on the
substrate, so the family cannot both decline the lattice chirality no-go for want of a referent and
claim this rule from substrate topology. What is the family's own is the *carrier*: baryon number is an
integer winding, and the incumbent's rule then says what a violating process must do to it. The
conservation law is the family's; the topological carrier is endorsed; the counting theorem is borrowed
and marked as borrowed.
*Not, second:* unconditional in a grainy member. Homotopy invariance is a statement about continuous
maps; in a grainy member — and grain discreteness is one of the family's preferred directions — a
configuration whose core shrinks toward the grain spacing leaves the space of admissible maps, and the
winding number is not defined through the transition. The programme's own lattice flows have recorded
unwinding events at under-resolved cores. **So the prohibition is exact in a continuum member and carries
a resolution condition in every grainy one.** That condition is parametrically enormous in the first
candidate — a hadronic core against a Planckian spacing — but that is an estimate and not a computation:
converting it into a rate is a dynamical statement, and the rate face is gated exactly as the
non-perturbative channel's is. The suppression that estimate would give is not used, to keep the
prohibition unconditional. **The family forbids the decay channel; it does not compute the unwinding
rate of the member it endorses.**

**One residue inside the carrier.** The coset winding is canonical; the subgroup winding is not. Reading
a *general* configuration in the subgroup/coset basis requires a splitting of the exact sequence
relating the two bases, and while such a splitting always exists it is not canonical and the family has
not named one. Nothing above turns on it — each prohibition is argued at a configuration whose sector is
fixed by its own construction — and the residue closes if the sector assignment is ever derived rather
than assumed.

**C13. Magnetic monopoles are absent — by the source identification, not by algebra.** The grade-three
slot in the field equation is not empty as a matter of Clifford structure: grade three here is
four-dimensional, and that slot is exactly how geometric-algebra electromagnetism *with* monopoles is
written; the engine reports the slot's dimension rather than its vanishing. What this family supplies is
that nothing fills it — its only current is the wavefront projection of grade-two winding to grade one,
and a grade-two-to-grade-one projection cannot produce grade-three content.
*Given:* the winding-as-source identification.
*Not:* an algebraic forbiddance. A different source identification would refill the slot, and that is
the re-attack handle.

## 2.7 The quantum package — a relocation with a gain

**C14. The quantum postulate structure and the Bell sector follow from the axioms plus the package's
registered imports, with no candidate pick.** Delivered: the complex unit as a forced subalgebra rather
than a stipulation, the self-adjointness condition, the Born exponent as a theorem given its named
premises, the Dirac equation, the no-signaling identity, and the Tsirelson bound `2√2` reproduced from
the one-sided rotor half-angle — that last riding the composite state space and the singlet, which this
paper books as imports rather than constructions. Probability is not a primitive of the ontology here:
the substrate is configuration-realist, and the measure over its configurations is what the Born
exponent is a theorem about.
*Given:* imported, registered mathematics — the tensor-product composition rule for composite systems,
the singlet form, Gleason's theorem among them. The composite state space in particular is **assumed**,
not constructed, with five construction routes recorded as failed.
*Not:* quantum mechanics derived from the substrate. Family-clean is a *consumption* classification —
these results use no candidate pick — and not a claim of derivation-completeness. This block is a
**relocation with a gain, exactly as the signature is**. What remains genuinely open: the single-outcome
selection mechanism, which is also one of the Born theorem's named premises.

**The complex unit's two halves have different status.** Impose three conditions on a rotor element
acting on the defect background — that it commute with the advance axis, preserve the soliton
background, and be even-grade — and the intersection is exactly the two-dimensional commutative
subalgebra `{1, B}` with `B² = −1`. That subalgebra is **forced**, and the quantum complex unit is its
consequence rather than its premise; with no defect present the third condition is empty, the
centralizer is four-dimensional, and there is no unique complex line at all — the rotational ambiguity
of free space, broken by a defect. What is **not** forced is the next step: taking the fluctuation field
to lie in that subalgebra is an **ansatz**, and as written it is too strong, since it delivers a
one-dimensional complex state space the Bell sector's own two-state construction does not use. The
subalgebra result stands; the field restriction is an open construction.

**One further debt.** The written argument for why the choice of memory kernel does not disturb quantum
mechanics currently rides a candidate pick, so the family keeps the postulates and, as things stand,
loses its own protection argument until that argument is restated at family level.

---

# §3 — The separator, applied to this family's own list

The sharpest available objection to a programme of this kind is that it has elaborate guardrails against
fabricated *numbers* and none against fabricated *structure* — that relabelling a known result in new
notation and filing it as derived is exactly the failure mode the apparatus cannot see. That objection
is correct as stated, and the answer is a criterion, applied to this family's own list first:

> **A structural fact counts as *obtained* rather than *relabelled* when (i) a named substrate
> feature's deletion breaks it — an exhibited failing counterfactual; (ii) it is independent of the
> framework's free parameters; and (iii) the feature does work it was not selected to do — either
> *structurally*, by carrying a load in a sector it was not introduced for, or *empirically*, by
> having a consequence in a domain not used to fix it which was then independently tested and
> confirmed.**

Clause (iii) does the work the first two cannot: a feature chosen in order to produce a result will
always break that result when deleted, so clause (i) fires automatically in exactly the case the
separator advertises itself against. Clause (ii) has a narrower fate, stated because
the separator is worth more reported honestly than reported strong: **its domain is empty at family
level.** It asks whether a claim is independent of the framework's free parameters, and the family has
none — so it discriminates nothing here, and the work it does is done at the *candidate* level, where
there are four fitted parameters for it to bite on. Clause (i) does strike below — it removes one entry
outright and collapses a pair — but what neither of the first two can do is separate an obtained fact
from a reverse-engineered premise, and clause (iii), the classical demand for excess content, addresses
that. Applied to the family's own claimed list of ten
structural facts, the first two clauses **collapse one pair into a single fact, remove one outright, and
leave eight distinct claims:**

| Grade on clauses (i) and (ii) | Count | Which |
|---|---|---|
| **Pass both** | **2 — one unconditional, one riding a pick** | the **charge arc** (§2.1), and the **weak arc** (§2.4) *conditional on the carrier*: the weak assignment is made on one of two candidate carriers, and on the other the same datum that eliminates the competing class eliminates this one too — the engine returns *refuted by data* there, not merely *different*. So the weak arc's pass is a pass **given that pick**, and a reader who rejects the pick is left without the claim rather than with a weaker version of it. Counted here at that strength |
| Pass with a stated weakening | 4 | the **generation count** (§2.3) — generic-given-four-dimensions, real but not substrate-specific · the **Lorentzian signature flip** (§2.2) — half-chosen: the algebra isomorphism is a theorem, the timelike placement is an axiom · the **monopole absence** (§2.6) — conditional on the winding-as-source identification, whose failing world is named in place · the **`B − L` closure** (§2.6) — narrowed, because the incumbent also obtains `B − L` as an accidental symmetry; what survives is the closure of the Dirac-versus-Majorana question the incumbent leaves open |
| Partial or undecomposed | 2 | the **gauge group** — one factor is obtained, not the group, since colour is not a gauge group in this family at all · the **up/down mirror** — the parity relation is contentful, the SD/ASD label is convention, and no counterfactual was exhibited for it |
| Collapsed into another entry | 1 | proton stability and the absence of neutrinoless double beta decay share the `B − L` root — one fact with three faces (§2.6), so no independent credit |
| **Does not belong on the list** | **1** | the **Tsirelson bound** — the engine itself tiers it as a framing identification, because it rides the composite state space §2.7 books as *assumed* |

**The counterfactuals, exhibited.** Charge arc: delete the trivector factor of three and the neutrality
bracket no longer vanishes — the residue is `2c ≠ 0` in this paper's normalization, where
`Y_lep / Y_Q = −3`, and `−2c/3` in the conventional one with `Y_Q = 1/3`, the two differing by the
overall scale of `Y` and by which orbit is written first. The number is normalization-dependent and the
*point* is not: it is nonzero for **every** value of the free constant. Weak arc: delete the
right-handed-singlet datum and the diagonal class survives the classification, so the menu re-opens and
the assignment reverts to a choice; delete instead the assumption that the host lies in the substrate's
rotation algebra and there is no menu to close at all; and collapse the local state from a full
orientation to a bare direction and no body-frame action exists, so the host could not be an
observer-scalar. None of these touches a fitted parameter — this family has none in either arc. The
entry the separator **strikes** is the Tsirelson bound: reproduced exactly here, and deleting any
substrate feature at all leaves it standing, because it follows from the composite state space §2.7
books as assumed. A correct number that no substrate deletion can break is not an obtained structural
fact, whatever its tier says elsewhere.

**The third clause, on the same ten.** On the **empirical** half — a consequence in a domain not used to
fix the premises, then independently tested and confirmed — **the family scores zero of ten.** The
nucleon charge anchor is the datum the construction enters, with the hydrogen-neutrality bound then
*testing* the identity rather than calibrating it; the absence of fractional charge is the datum
matched; the generation count is the datum matched. One entry is **pending** rather than failed: the
`B − L` closure's excess content is entirely forward — Dirac neutrinos, no neutrinoless double beta
decay, the sterile mass tie — and all of it currently null, which is untested-and-consistent rather than
corroborated. On the **structural** half — a load carried in a sector the feature was not introduced for
— the passing entries share one root, and counted honestly they collapse to **one structural pass**. The
trivector orbit's loads are not four: the charge unit's *one third* and the colour count's *three* are
one fact about one orbit stated twice, and the `B − L` anomaly sums are insensitive to the colour
multiplicity (§2.6). What remains is one root — the orbit's three-plus-one split with its sign opposition
— carried into the charge arc and into the `B − L` closure. That is one structural pass reused, not two,
and this section applies to itself the same collapse it applies to the proton-decay,
neutrinoless-double-beta and Dirac-neutrino trio.

**The input side of the same worry, measured.** What clause (iii) is afraid of is a premise introduced
only to make a result work. The comparative ledger prices every banked result's premises as free, cheap,
costly, or **convoluted** — the last being a premise whose only motivation is the result it enables —
and run over the audited corpus that instrument returned **zero convoluted premises**, both demotion
slots empty. It is not an instrument that declines to fire: the same campaign returned five
double-billed findings and one under-billed, four of the six against this programme, and refuted the
author's registered expectation on one line. **So the honest pair is: zero convoluted premises on the
input side; zero empirical passes and one structural pass on the output side.** The named route to a
first empirical pass is §4.1's finite-grain / bounded-amplitude higher-order-interference deviation law.

**The honest outcome.** On the debt-structure criterion — are the debts named, in-principle payable, and
carrying a named and unblocked route to payment — this family's position is `PARTIALLY SUPPORTED, NOT CONFIRMED`. The **unconditional**
residue of §2 is a set of correct facts about a sixteen-dimensional real Clifford algebra together with
an identification dictionary assembled with the Standard Model in view. The **conditional** residue is a
reconstruction of quantum numbers — labels, slots and selection rules — not of interactions: there is no
gauge boson anywhere in this family. The **empirical** posture is four null forward bets, two wounds
belonging to the first candidate, one live internal rework, one family-level structural exposure in the
incumbent's best-tested sector, and **one live confrontation with a measured non-zero number**: the
baryon asymmetry, `η ≈ 6×10⁻¹⁰`, which this family's own topological protection makes harder to produce
than the incumbent does (§4.4). A null one has not yet failed and a measured number one cannot yet
produce are different kinds of debt, and only the second is already on the board.

One debt is discharged by computation: the weak sector's assignment is not an input and not a preference
— given the endorsed hosting premise and one datum read from experiment, it is forced (§2.4). That is
one discharge, on the cheapest of the debts, and it does not generalize: the method closes menus that
are finite and algebraic, and the largest open item is a space of constructions, which no such
enumeration reaches.

**The comparison, priced.** The debt-structure criterion just applied to this family applies to every
framework in the comparison: is the debt **named**, is it **in-principle payable**, and is there a
**named and unblocked route** by which it could be paid. Nothing in it counts entities.

That is not a preference. Posit counts do not survive contact with individuation — re-describing a
structural commitment moves any such count by roughly a factor of two either way, which is why §5.2
forbids quoting a bit-inclusive count against a continuous-parameter one. But the decisive objection is
sharper. **Under a posit count, the best available position is to decline to have an ontology at all**: a
framework that says nothing about what exists carries no entities and wins. Under debt structure the same
position is the worst available, because a debt declared not to be a debt is the one kind that can never
be paid. That inversion is the whole argument for the criterion, and this family sits on the exposed side
of it — it carries the largest structural inventory in the comparison (§5.2) and says so.

**What the incumbent earns, first, because the comparison is worthless without it.** The Standard Model
is not a description with the explanation missing. Anomaly cancellation is a structural earning on a
chosen representation content. Baryon and lepton number arise as accidental symmetries of the
renormalizable Lagrangian rather than being imposed, and proton stability follows at dimension four; the
absence of tree-level flavour-changing neutral currents follows from the GIM structure; custodial
symmetry delivers `ρ ≈ 1`; asymptotic freedom is derived, not fitted. And it holds **the one earned
dimensionful scale in the comparison** — the strong scale, by dimensional transmutation from a
dimensionless coupling. This family has zero.

More: the incumbent's posits were **forced sequentially by measurement**, each with a discovery record.
Fractionally charged pointlike constituents were not proposed for elegance; deep-inelastic scattering
found them. Colour multiplicity is counted in `R` and in the `π⁰ → γγ` rate. Neutral currents were
predicted and then observed; the `W` and `Z` were predicted with masses and found at them; the scalar was
predicted in 1964 and found in 2012 at a mass consistent with the electroweak fits. A posit extracted
from data under protest is not the same object as a posit adopted for economy, and no accounting that
treats them alike is honest.

**What the incumbent owes, and does not name.** With that said, several of its entries are not carried as
debts at all. Nineteen continuous parameters — twenty-six to twenty-eight with neutrinos — whose values
are inputs the framework does not claim to explain, which under debt structure is a declaration rather
than a discharge. The scalar mass-squared is unprotected: the incumbent's own effective-theory logic says
a relevant operator's coefficient should sit at the cutoff, and it does not — a debt conditional on the
ultraviolet completion coupling to the scalar at all, which is a generic expectation rather than a
theorem. The cosmological constant, once gravity is admitted, on the same footing and worse. `θ_QCD` is
bounded near `10⁻¹⁰` by the neutron electric dipole moment with no mechanism requiring it to be small.
The generation count is an input. Charge quantization is obtained only in specific completions, and the
surviving flat direction is closed by nothing but the measurement itself (§2.1). And read as an effective
field theory — which is how it must be read where these debts live — it is explicitly incomplete above a
scale it does not name.

Two of those, the scalar mass and the cosmological constant, are the incumbent's tunings, and the
comparison against this candidate's dimension-six ceiling (§5.3) runs on four axes that do not net: the
incumbent's tunings are **consistent with all data** where the ceiling is a **constraint already in
force**; an input can be tuned and a prediction cannot, so the smaller debt here is **harder in kind**;
the incumbent's repayment route requires leaving the Standard Model where this one's is internal; and a
relevant operator must be re-tuned at every scale where an irrelevant one stays small once set. **Two
axes against this family, two for. Neither side's debt absorbs the other's.**

**What this family's structure claims, and at what price.** The claim is not fewer entities; it is a
different debt *shape*. Where the incumbent's charge quantization is a condition on a chosen
representation content, this family's is an integer; where its baryon number is an accident of a
dimension-four truncation that higher-dimension operators break, this family's is a homotopy invariant
surviving any smooth deformation; where its generation count is an input, this family's is a dimension.
Each is protection of a different kind rather than of a greater amount, and each is stated at its
conditional strength in §2.

The price is stated in the same breath, because it is larger: seven axioms and one refusal, eight
preferred directions, fifteen recorded choices in the first candidate, a driven medium whose two
suppressions are owed from an axiom rather than from a pick, a colour sector that is not a gauge group
and does not reach the short-distance data, zero earned dimensionful scales, and one unbuilt object on
which every magnitude waits.

**The fence, and it governs every line above.** No item in this subsection is offered as evidence that
the family is true, and none of it compensates for the two wounds (§5.3) or for §4.4's exposure; against
the separator's third clause this family has produced no empirical pass at all, which is the count
recorded above. What the accounting establishes is narrower and worth exactly what it says: that the
incumbent's economy is not free either, that the two frameworks' debts differ in kind rather than only in
size, and that the comparison becomes evidential only if and when the kernel delivers magnitudes this
family cannot currently produce. Until then it is a statement about bookkeeping, and bookkeeping is not
physics.

The full accounting is `TWT_COMPARATIVE_LEDGER.md`; its ledger-level findings 5, 20, 22, 34 and 41 are
the load-bearing adverse ones and the fastest route to this subsection's weak points.

Three things this section does not do. It does not decide whether the theory is true: parsimony is
evidential only between empirically equivalent theories, and this family is not empirically equivalent
to the incumbent — it is behind it in two named places. It does not present a finished picture; every
rival column in the comparative ledger is a photograph of a finished ontology, and this one is an
architect's rendering, conditional on a single unbuilt object delivering the magnitudes the family owes.
And it does not claim that any structural result above has been *confirmed*: every channel in which the
family's §2 results are currently exposed is one in which a detection would break them and a null
confirms nothing (§4.1).

---

# §4 — The falsification surface

## 4.1 The family's kill condition

**If the ordering that Bell-correlation selections follow is measured and found to be a foliation
measurably distinct from the cosmic rest frame, the family is finished** — not one version of it, all of
it. That is what it means for B-6 to sit in the definition rather than in a branch.

**The asymmetry.** The measurement that would fire this is one standard quantum mechanics *also*
forbids. In this channel agreement confirms nothing — it is a consistency check, and the family inherits
quantum mechanics' verdict either way — while disagreement kills. Maximum downside, no matching upside;
that is the price of naming the frame. **The reference class:** a total kill condition **no rival in the
comparative ledger's reference class carries** — Copenhagen, Bohm and Everett, priced there one by one.
That class is the interpretation league; the Standard Model enters that ledger as the target rather than
as a rival ontology, so no such comparison is drawn against it there. It is not a claim to be the most
falsifiable theory in physics, and not a claim that no other programme anywhere accepts a comparable
exposure — GRW-class collapse models carry kill conditions of their own and are ruled into that
reference class without yet being built out in it, so the comparison is not presented as complete. It is
the strongest option **available at family level**, taken rather than declined.

**What that aggregates to.** Of the sixteen falsifier rows the corpus carries, fourteen stand at family
level and two are instance-level — one whose kill number rides a candidate's fitted hadronic
calibration, one riding a candidate's identification of the observed light speed with the meta-time
advance rate. Because this kill channel fires only where quantum mechanics also breaks, and because
every §4.2 prohibition reaches a derivation or a preferred direction rather than an axiom, **aggregated
on the killability side: no measurement anyone can currently make can kill the family** — a positive
detection in any feasible channel forces the next candidate instead of ending it. Said at its truest:
**this is a research programme with one inherited total kill condition, a real set of family-level
prohibitions, and no channel of its own in which agreement would count as evidence.** The asymmetry is
not local to this channel: every row of §4.2 is a *forbiddance* and each is currently null, and a
holding forbiddance is consistency rather than confirmation, so the family's structural content is at
present **breakable but not corroborable**. That is a statement about the *channels* and not about the
*content* — §3's separator exists precisely to test whether a retrodiction was obtained or relabelled —
but the channel fact is what decides what the programme can *earn*.

**The one identified route to a channel of its own** is the finite-grain / bounded-amplitude,
higher-order-interference channel: the Born rule's deviation law — sourced either by the medium's grain
(vanishing with it) or by its amplitude ceiling (present at fixed grain) — would be a structure-derived
number the incumbent inputs as exactly zero, and the triple-slit programme already supplies a bound. The
two sources carry different scaling laws, and which one a positive result would implicate is part of
what the channel's protocol must separate. That deviation law is not derived here; it is a route family,
not a result.

## 4.2 What the family forbids

These are the family-level prohibitions with independent experimental routes. Each follows from the
axioms, or from the axioms plus one stated preferred direction, so a positive detection on any of them
reaches every candidate at once — and none is a total kill, because each reaches a derivation rather
than an axiom.

| What would be observed | Channel | Current bound | What it reaches |
|---|---|---|---|
| **Proton decay**, at any lifetime | Super-Kamiokande, Hyper-K, DUNE | `τ/B(p → e⁺π⁰) > 2.4 × 10³⁴` yr, 90% CL; other channels are weaker — Super-K's own `p → μ⁺η` and `p → e⁺π⁰π⁰` limits sit near `7 × 10³³` yr, so this cell is the strongest single channel and not a bound on the all-channel prohibition beside it | the topological protection of baryon number (§2.6) — **the family's one distinctive forward bet**: grand unification expects decay at *some* level and this family forbids it outright — and, in any grainy member, the resolution condition under which the winding is defined at all, a condition this family states and does not compute |
| **Neutrinoless double beta decay** | KamLAND-Zen, LEGEND, nEXO, CUPID | `T₁⁄₂(¹³⁶Xe) > 3.8 × 10²⁶` yr, 90% CL | exact `B − L` conservation, and with it the Dirac neutrino character that conservation forces. What does *not* die with it: anomaly cancellation is a trace identity on the charge assignment, untouched by a broken conservation law |
| **A sterile neutrino at any mass far above the active scale** | KATRIN's kink search, extended into the keV range by the TRISTAN detector upgrade | none observed | the Dirac-partner mass tie `m_sterile = m_active` at the sub-tenth-eV cosmological scale (`≲ 0.12 eV` at the older bound, `≲ 0.064 eV` under ΛCDM at the current one, and `≲ 0.16 eV` once the dark-energy equation of state is freed — the literature is model-split here and the figure must not be quoted flat) — the same `B − L` root as the row above, probed through the right-handed partner's mass rather than through `0νββ`; the tie's *number* is value-gated on the candidate's neutrino-mass machinery, so what a detection reaches is the Dirac character itself |
| **A fourth fermion generation** | LHC; neutrino-oscillation precision | none observed | the dimension count of §2.3, together with its identification and associativity premise — **and the reach is *contested*, not merely unproved**: §2.3 records that the same anti-self-dual triple is claimed by two readings at once (generation seats, or a second weak factor gripping the complementary half), and nothing at the level of the local algebra separates them, so under the second reading this prohibition has no subject at all |
| **A magnetic monopole** | direct searches | none observed | the winding-as-source identification of §2.6 — not a pure algebraic forbiddance, and the slot exists |
| **Fractional charge outside `{±1/3, ±2/3, ±1}`** | direct searches | none observed | the trivector charge spectrum of §2.1; the spectrum does not ride any arrangement |
| **Tree-level flavour-changing neutral currents** | precision flavour physics | no tree-level signal; the strangeness-changing neutral-current decays sit at `B(K_L → μ⁺μ⁻) = 6.8 × 10⁻⁹` and `B(K_L → e⁺e⁻) ≈ 9 × 10⁻¹²`, the smallest measured branching fraction of any particle decay — rates the incumbent generates at loop level, so what they bound is the tree-level contribution on top of them | the weak host of §2.4 — either its structural premise or its empirical leg |
| **A non-zero proton–electron charge sum** | neutrality-of-matter and bulk-matter charge tests | `\|Q_p + Q_e\|/e ≲ 10⁻²¹` | the four premises of §2.1; the family reverts to an empirical charge anchor. *Shared prohibition:* the incumbent's anomaly structure protects the same sum (§2.1), so this row is a self-test, not a discriminator — the discriminating neighbour is the **neutron charge**, exactly zero under §2.1's native closure where the incumbent leaves it a bounded free parameter. That neighbour carries its own caveat: the tightest neutron-charge input is carried over from this very neutrality measurement by an assumed charge-conservation identity in neutron beta decay, so the independent leg is the weaker cold-neutron deflection one |
| **A gravitational-wave / photon speed difference** beyond the multimessenger interval | multimessenger astronomy | `−3 × 10⁻¹⁵ ≤ (c_GW − c)/c ≤ +7 × 10⁻¹⁶` — two-sided and asymmetric, and conditional on the assumed gamma-ray/gravitational-wave emission-time offset and on the conservative distance taken | one substrate, one light cone. The claim is family-*eligible* — it should follow from S1a with S4 — but the re-grounding is **owed, not performed** (§4.4), and it does **not** rest on §2.5's matter-species argument, which covers the matter sector only and not the gravitational mode. A detection here would reach an expectation this paper has not derived, a weaker reach than the other rows |

**One channel this table does not carry, entered as a proposal rather than a row.** The `ΔB = ΔL = 3`
rule that forbids proton decay does *permit* a three-nucleon transition into three antileptons, and no
experiment has searched that channel. So it is **not a bound this family has survived and not a
discriminator**: this family's own rate for it is gated on the unbuilt dynamics, and nothing here
predicts a level at which it should be seen. What it is, is a proposable experiment in a channel the
incumbent's own selection rule shares.

**Two readings of that table, cutting in opposite directions.** Several rows would falsify the Standard
Model too, because they test predictions the two share — the charge ladder and tree-level
flavour-changing currents among them — so they are not discriminators. The genuinely discriminating rows
are the smaller set where this family forbids what the incumbent permits: no proton decay at any level —
and the reading matters, because at the renormalizable level the incumbent forbids it too, so what this
row discriminates against is the Standard Model read as an effective theory, whose higher-dimension
operators break `B` and `L`, and grand unification, which expects decay at *some* level — no Majorana
neutrino and hence no neutrinoless double beta decay, no fourth generation, no monopole. Those four are
where a measurement could separate the two, and all four are currently null. The sterile-neutrino row is
not a fifth: it and the `0νββ` row are two experiments on one underlying derivation, the `B − L` closure
of §2.6, reached through different mechanisms — the same non-independence §3's grading books as a
collapse.

## 4.3 Knowability — the classification every open question carries

Not every open question in this programme is one effort can close, and pretending otherwise is how a
research programme spends years distinguishing descriptions rather than theories. Every open item
carries one of three tags.

- **PINNABLE** — some inside-frame observable can decide it. These are the docket.
- **UNPINNABLE** — in-principle inaccessible from inside the lock, by the theory's own structure. These
  are **family freedom**: recorded, never expanded on. Candidates differing only in unpinnable choices
  are **one member with many descriptions**. The orientation convention naming the two chiral factors
  (§2.4) is the worked example: nothing in the corpus pins the substrate's orientation, so "SD" and
  "ASD" are one assignment with two names.
- **UNKNOWN-KNOWABILITY** — tagging it is itself the first task.

This is why the family's deliverable is **a list of surviving candidates** — self-coherent, empirically
plausible members — rather than one maximally pinned version. A second candidate is a new table beside
the first one's, not a rewrite of this paper.

## 4.4 What the family does not claim, and what a candidate must deliver

**No scales.** The family has **zero earned dimensionful scales**. Every one of the seven axioms and the
refusal is a sign, an integer or count, a relation, or an ontological kind; not one is a length, a time,
an energy or a rate. A scale-free axiom set cannot output a dimensionful constant, so **no family-level
derivation of a dimensionful coupling exists, and the obstruction is in the axioms rather than in the
effort spent** — within the charter as it stands; a member adding a Core-level scale axiom would be
defining a different family, since the charter's own rule is that adding or dropping an axiom makes a
different theory. That is §2's shape read from the other side: charge quantization works because winding
is an **integer**; the Weinberg ratio works because it is a **ratio** — one riding §2.4's weak
assignment, and a normalization identity rather than a prediction of the measured value (§5.3); the
kinematic bridge works because a signature is a **sign pattern**; the generation count works because it
is a **dimension**. Gravity's headline number has units.

**No gravity results today.** Every gravity result in the corpus rides a candidate pick. The
*structural, dimensionless* facts — one medium so one light cone, the equivalence principle, the
Newtonian limit with the right sign, compatibility with general relativity — are family-**eligible** and
are owed as a re-grounding on the axioms rather than inherited; the *coefficient* is family-**ineligible**
by the scale argument above. This paper does not claim the re-grounding has been done.

**No magnitudes.** Couplings, running, absolute masses and decoherence rates all wait on the one unbuilt
object: the driven-dissipative substrate dynamics. **The family owns the kernel programme; it owns no
kernel.** What it holds at its own level is a **constraint class** — the conditions any admissible kernel
must satisfy, each entered as a boundary on the object rather than a piece of it, one of them empirical
and already binding (§5.3's dimension-six ceiling). The demand made of this programme most often is
recorded here as ill-formed at family level: an exact microscopic kernel for the four-dimensional medium
is not what a theory written from inside the lock is in a position to hand over. **The success criterion
the family accepts instead is a compatible effective kernel class, on the order of four to six
constants, from which the quantities the programme currently gates could be extracted.** That is a lower
bar than the one usually demanded, it is a real one, and nobody has cleared it.

**One exposure, and it is the family's rather than a candidate's.** Colour is not a gauge group in this
family at all, and that reaches every member. It buys something real — §2.1's charge spectrum and the
confinement reading with it — and it owes **the short-distance response**. Deep-inelastic scattering
resolves pointlike, fractionally charged constituents inside the nucleon; the structure functions
exhibit Bjorken scaling and violate it logarithmically, as a pointlike-constituent description requires;
jet production and its angular distributions are measured phenomena of the same class. Those are among
the best-measured structural facts in physics, and every one is dimensionless — so the scale argument
gives this exposure no shelter whatever. A defect picture must reproduce that behaviour as the
short-distance limit of its own structure, and this one has not. The programme's own engine ranks it as
the **make-or-break empirical falsifier** and is wired to raise rather than return there. **It is the
family's sharpest structural exposure.** Two fences belong with it. The exposure is against the data and
not against a rival's bookkeeping: the incumbent's strong sector is priced, not assumed debt-free — it is
credited with the one earned dimensionful scale in the comparison, the strong scale by dimensional
transmutation, and the comparative ledger prices the rest item by item, including the asymmetry that its
lattice machinery works precisely because a lattice there is a **regulator** whose artifacts are removed
in a continuum limit, the opposite of the ontological status a grain has in a grainy member here — an
asymmetry booked against this family, not for it. And the family's own picture supplies a stance and not
a discharge: a defect's spatial extent is configuration-dependent, so pointlike scattering off a lepton
is not by itself an embarrassment for a defect ontology, but the nucleon's internal short-distance
response is a different object and nothing in §2 reaches it.

**Two family-level debts in physics rather than in bookkeeping, neither with an attempt on record.**
Neither displaces the exposure above in rank, but both are owed at family level and both are the kind of
question a physicist asks first.

*The baryon asymmetry, and no baryogenesis.* The observed baryon-to-photon ratio is `η ≈ 6×10⁻¹⁰` — a
measured number the family owes, and what makes owing it hard here is the family's own protection
argument rather than anything inherited. Baryon number in §2.6 is a homotopy invariant, surviving *any*
smooth deformation whatever operators are present, strictly stronger protection than the incumbent's
accidental symmetries. The only violating channel available is the incumbent's own `ΔB = ΔL = 3` rule,
which carries `Δ(B − L) = 0` identically, so it cannot generate a `B − L` asymmetry at all; its rate is
gated on the unbuilt dynamics in any case. Of the three standard conditions for generating an asymmetry,
the family has one for free and has never used it — departure from equilibrium, since the medium is
driven by axiom; baryon-number violation exists only as that one selection rule; and no substrate
mechanism for CP violation is banked, the standing candidate being parity-violating but a gauge singlet,
a located obstruction rather than a route. **This is a live empirical confrontation**: a measured number
stands against a protection argument this family advertises as a strength.

*Two suppressions owed from an axiom.* The medium is driven and dissipative — S5, an axiom and not a
pick — and a driven dissipative medium generically exchanges energy with its drive and decoheres what it
carries. The world exhibits neither: energy conservation holds to the precision of every test, and
macromolecule interferometry sustains coherence with no observed substrate floor, a floor this programme
cannot compute. So the family owes two suppressions, **from an axiom rather than from a pick — which is
why no candidate can discharge them on the family's behalf.** §2.7 records the adjacent half only. §4.3's
unpinnable class does not cover this: these are not knowability questions about a convention, they are
questions about what the driven medium is observed to do, and they stay open at family level whatever a
candidate picks.

*One forfeit belongs with the first of them.* Because `B − L` is exactly conserved here, Majorana masses
are forbidden (§2.6) — which forfeits leptogenesis, the incumbent literature's leading route to the
asymmetry above, and forfeits the seesaw with it. **The seesaw is the standard explanation of why
neutrino masses are small, and this family does not have it and has nothing in its place.** That is a
cost of the prohibition; nothing here proposes a mechanism as the fix.

**The field-reclamation debt.** The refusal demotes the field to instance-level description, which
creates a duty the demotion does not discharge. Fields won historically by doing work a medium could not
be shown to do: retardation, radiation reaction, local conservation of energy and momentum in transit,
and gauge structure. Every item is now work the *medium* must be shown to do instead, and naming the
list item by item and tracking which entries have been reclaimed is a standing duty — finite and
concrete. If gauge structure proves to be on the un-reclaimed list, that is family-relevant knowledge,
not a candidate's detail.

**So what must a candidate deliver?** Four things, and the first candidate delivers the first three.
(i) A grain structure, with the local-state axiom re-witnessed on it rather than inherited. (ii) Numbers
— a member that declines every calibration does not thereby carry a smaller parameter count; it carries
no numbers at all, which is a different thing and a worse one. (iii) The picks that buy those numbers,
each recorded with the menu it came from and what un-picks it, so a branch point is visible as a branch
point rather than as a result. (iv) The kernel, or an explicit inheritance of the gate. Nobody has
delivered (iv).

---

# §5 — The first candidate

## 5.1 What V3 is, and what it pins

V3 is the family's first complete leaf, and what it proves is an existence result and nothing more: **a
member of this family can be built all the way down to numbers.** It can be dismantled entirely without
a line of §1 changing. It pays for that with **eleven pinned choices, three of them carrying recorded
sub-choices (one of them two) — so fifteen rows below**, the individuation this paper counts by throughout.

| # | The pick | The menu it came from |
|---|---|---|
| 1 | Substrate arrangement = a **regular D4 lattice**, at the back-fit (Planckian) size | regular lattices / irregular-discrete arrangements / a continuum medium with a cell scale |
| 1a | Drive-axis alignment = the advance axis is a **lattice symmetry axis** — the choice every driven-group object below spends | aligned (the banked apparatus) / misaligned-generic (trivial stabilizer — the driven-group machinery collapses) / lower-symmetry alignments |
| 1b | **Two-rate defect rotor, drive-referenced** — the twist generator carries a second, wave-parallel plane rate, told apart from the transverse one by the drive axis of row 1a and standing or falling with that alignment; the mass stays the observer's winding-plane angle, and the rate ratio is an open kernel-level quantity | the simple (one-rate) restriction / the drive-referenced two-rate form / a free-standing two-rate form, which has no invariant referent without row 1a |
| 2 | Bond structure = the **`{J, D}` truncation** | the ten-constant bilinear menu allowed on D4 under the driven point group |
| 2a | Chiral-bond support = the twelve advance-axis bonds only | the two-dimensional allowed space, which no substrate argument separates |
| 3 | `f_π` = the fitted cell-scale value | any cell-scale anchoring |
| 4 | `D/J ≈ 0.79` — a ratio of bond totals, lepton-calibrated | any calibration channel |
| 5 | The Skyrme stabilizer value | the stabilizer determinations |
| 6 | Gravity route = **Sakharov induced gravity**, in one banked action class | thermodynamic / entropic / gauge-gravity routes — all taxed by the analogue-gravity caution |
| 7 | Cost pairing | a four-option menu; the no-invariant-pairing theorem survives any re-pick |
| 8 | The vacuum carrier is **costed** | costed / costless / other densities |
| 9 | Kernel branch = the **driven-hysteretic** class | the full kernel-class menu — this is the unbuilt object itself |
| 10 | Hadron machinery = the **semiclassical Skyrme toolbox** | soliton-quantization toolboxes |
| 9a | **Cell-scale target space = the same target as the grain state** — the assumption the Skyrmion sector rests on | the same target / the Goldstone coset of the grain vacuum / an unrelated emergent target. **What rides it: the entire hadron sector** — a soliton needs a target carrying `π₃ = ℤ`, so the calibration table below has a carrier only if the surviving manifold is three-dimensional. If the surviving target is lower-dimensional the Skyrmion sector has no carrier and the hadron calibrations fall with it; if it is three-dimensional the Skyrme construction is licensed from below rather than assumed. **Open, and the deciding computation is docketed** |
| 11 | Fermionic quantization = the **Finkelstein–Rubinstein** scheme | fermionic-quantization schemes for solitons |

The full table — each node with the named result that required it, what rides it, and its complete revert
clause — is `TWT_FAMILY_TREE.md`, authoritative where the two differ.

**What those picks write down.** With the arrangement and bond truncation fixed, this candidate has an
explicit energy on the lattice. Each bond carries the relative orientation of the two sites it joins,
`W_b = O_j O_iᵀ`, and the bond energy is the bilinear `E_b = Tr(K_b W_b)`, summed over the twenty-four
bonds of the D4 root system. The couplings that structure allows under the group a drive along the
advance axis leaves intact are computed **exhaustive at ten** — two of scalar character, two
antisymmetric, six symmetric-traceless — and pick 2 keeps the first two families and zeroes the six.
Expanding about the canted vacuum gives a six-band stiffness spectrum, and with the antisymmetric
coupling set to zero the stiffness operator collapses to an exact identity,
`H(k) = 12 · J · k̃²(k) · 𝟙₆`, with `k̃²(k)` the bond-average of `1 − cos k·b` over those bonds: six
degenerate bands, isotropic at leading order — §2.5's arrangement-level protection seen in the spectrum
itself. Switching the antisymmetric coupling on splits that into **two gapless modes and four exactly
fourfold-degenerate gapped ones**, on both computed vacuum branches. The split and its fourfold degeneracy
are branch-robust; the gap *value* is not — at the ratio pick 4 calibrates it is `0.4121 J` on the
body-diagonal branch against `0.4060 J` on the axis branch, about one and a half percent apart. **A gap
from this spectrum is never to be quoted without its branch label and that ratio**, and which branch a
driven dynamics selects is a kernel question this candidate does not answer.

That question is now sharper than a preference between two minima, because **neither computed branch is
one**. Both are stationary points of the bond energy, and on both the lowest band turns negative at long
wavelength in a direction perpendicular to the helix — on one branch this is a transverse instability the
candidate already recorded, on the other it is a mode outside the family that was scanned. The effect is
confined to wavelengths of order a thousand lattice spacings and beyond, and is shallow enough that the
short-distance response is unaffected: continuing the same stiffness operator to imaginary wavevector
gives the length over which a disturbance in a gapped direction heals, and it runs from about five lattice
spacings to a few tens, diverging along each branch's own helix axis. So static energetics select neither
branch, and what either reconstructs into is unscanned. Placing a defect core at the hadronic scale would
need a length some eighteen orders larger than any of these — a tension between two *entered* scales,
the lattice spacing and the fitted cell scale, with no computation carrying either into the other, and so
not a derived contradiction.

**Three conditions travel with that display.** The bilinear form is itself a class pick: taking a bond's
energy to depend only on the *relative* frame of its two sites restricts a much larger space of
couplings, so the exhaustiveness above is exhaustiveness *within* that restriction and never "at bilinear
order" in general. The two-family truncation is pick 2, counted as one, with the discarded directions the
live rework of §5.3. And these are **stiffnesses of a static energy** — an energy curvature about a reference state (and, per the paragraph above, not about a
vacuum, not a dynamical kernel and not a Bogoliubov spectrum, which is a different operator; the memory
kernel that would turn them into dynamics is pick 9, the unbuilt object itself. The display establishes
that this candidate has written something down at grain level. It does not open the magnitude sector.

## 5.2 What the numbers are worth

| | **Standard Model** | **This candidate** |
|---|---|---|
| Continuous parameters fitted to data | **19** (26–28 with neutrinos) | **4** — the cell mass scale, the chirality ratio, the measured Newton constant, and one hadron-sector stabilizer counted **provisionally** |
| Of the 19, pinned at their measured values | — (they are its inputs) | **0 unconditional; 1 conditional** — a candidate reading of the Gatto–Sartori–Tonin mass-ratio relation, which is not this programme's — **and 2 more only if a route this programme itself records as currently refuted is repaired.** *This candidate does not reproduce the nineteen from four.* The four buy a different and smaller set of outputs, and **this row is not separable from the one above it** |
| Exact values read as one bit | — | the Koide amplitude; the right-handed fermions' weak-singlet character |
| Counted structural premises | not counted, by convention | the soliton-mass identification |
| Structural commitments *(SURVEYED for the incumbent)* | ~10 fine / ~6 coarse (the comparative ledger itemizes both readings) | the family's 8, **plus 8 preferred directions, plus the eleven picks of §5.1 (fifteen recorded choices with their sub-choices) — the largest structural inventory in the comparison** |
| Earned dimensionful scales | 1 of 5 scale classes | **0** — one scale is a back-fit of measured gravity, the other a fit, and the ratio between them is neither derived nor protected |

**One fence on that table.** A bit-inclusive input count may never be quoted against a rival's
continuous-parameter count: the two kinds are reported on separate rows and never summed, because
structural choices have no canonical individuation — re-individuating moves any structural count by
roughly a factor of two either way. More than one count of about ten appears near this table; they are
different lists, and none is evidence for another.

**The provisional entry.** The hadron-sector stabilizer is counted as the **hadron-sector determination
of an object** a substrate relation predicts from the lepton-calibrated chirality ratio, the two agreeing
at about 1.1–1.5%. That agreement is a **hedged** cross-check, not a blind one: the baseline scheme was
itself chosen partly on this agreement, the substrate relation carries no scheme label, and the two legs
are readings of different functionals rather than two measurements of one constant. Both retirement
conditions are on the record: if the legs converge, the stabilizer retires and the count drops to three
plus the measured constant; if they split, the bridge relating them dies and the convergence claim with
it.

**Calibration performance, at earned strength.**

- **The charged-lepton triple** — three amplitudes fitted to three measured masses is a one-parameter fit
  in the generation phase, landing under 0.01% residual. This candidate's tightest empirical fit, and it
  is a **fit**: the forward derivation was attempted and refuted at the bridge, so the structural content
  is the Koide form and its geometric characterization, not the magnitudes. **What the displayed residual
  measures is Koide's imported empirical relation working.** The amplitude ratio is entered at its Koide
  value rather than derived, leaving two free reals against three measured masses, hence one residual
  direction, and the number reports that direction and nothing else. **And the digits are not
  scheme-stable at the precision they are printed to**: the relation's accuracy is mass-definition
  dependent, and this programme does not fix which renormalized mass its frequency identification refers
  to.
- **The cross-sector chirality ratio** — the lepton sector calibrates it at ≈ 0.787 through the
  generation phase; the baryon sector reads ≈ 0.778 from the Skyrme stabilizer, independently. **The two
  converge to about 1.1% with nothing fitted between them** — at the on-shell mass definition the
  bullet above says this programme does not fix; under the alternative definition the figure tightens
  rather than loosens — the strongest cross-sector consistency signal this candidate banks. What each leg measures is a **ratio of totals** — the parity-odd bond
  amplitude over the parity-even one — and the two legs' parity-even totals belong to *different*
  functionals, the generation amplitude and the helix pitch, which are the same substrate number only if
  the symmetric-traceless bond admixture vanishes. So the agreement is evidence that two different
  readings of the chirality cohere; it is **not** a second reading of one pinned parameter and not an
  independent over-determination. Read that way the 1.1% becomes sharper than a near-miss: on a reading
  of the generation phase as a rational arc ratio — held as a candidate and not as a result — the lepton
  leg fixes the ratio exactly, and the baryon leg then demands a Skyrme stabilizer of 5.392 against the
  literature's 5.45. That residual is a statement about one constant rather than a scatter between two
  fits, and as a test it is **not yet discriminating**: the historical stabilizer is itself a fit whose
  spread across determinations exceeds the deviation, so the test would bite only against a determination
  at or below about one percent. The chain also has one acknowledged geometric coincidence at the
  relating link.
- **The nucleon band** — the static soliton mass lands about 8% below the measured nucleon mass; adding
  the collective-rotation term with both coefficients from the *same* exact boundary-value profile gives
  936.4 MeV for the nucleon (−0.3%), 1229.8 MeV for the Δ (−0.2%), and a splitting of 293.4 MeV (+0.1%).
  **The two couplings were historically fitted to those two masses, so this is a pipeline consistency at
  no new parameter, not a new prediction. This sector inherits the semiclassical Skyrme model's
  performance and adds nothing to it.** The rows are here because a pipeline that failed to reproduce
  them would be refuted by them.
- **A recorded candidate convergence, not banked as a result** — the lepton-sector scale and the nucleon's
  per-rotor share agree to 0.28% between two measured quantities with no parameter between them,
  **against the nucleon average; against the proton the same number reads 0.35%, and the engine's own
  over-determination scan books it as not a passed test because the lepton amplitude scale is a free
  calibration**. The naive
  derivation route is blocked, the floor reading of the same object does not converge, and the
  look-elsewhere caveat is carried.

**What this candidate does not derive:** any coupling magnitude, individual quark masses (the programme
abstains from them by rule — only hadrons and leptons have masses here), the Higgs vacuum expectation
value and mass, the CKM hierarchy, the PMNS matrix, and neutrino masses. All are downstream of the
unbuilt kernel.

## 5.3 The two wounds

Both belong to this candidate. Both are already measured against. The family's sharpest structural
exposure is not here but in §4.4 — the short-distance response of a colour sector that is not a gauge
group — and it outranks both of these; it is not in this section because it is not this candidate's.

**The dimension-six Lorentz-violation ceiling.** The rotationally invariant dimension-six coefficient
escapes both protections of §2.5. Its coefficient is gated on the unbuilt dynamics, so the programme
asserts no value for it; what existing cosmic-ray and gamma-ray limits exclude is its **natural** value
at this candidate's own lattice scale — **unconditionally by about one order** (one model-independent
analysis, superluminal branch), **and by six to seven orders only under the pure-proton composition
assumption that observatory's own data disfavours**; a nine-order corner rests on a projected bound whose
triggering observation has not occurred. Those limits bind every future completion — natural, not naive;
direct gamma-ray limits contribute nothing at this operator magnitude.

What "natural" means here is now computed, and it cuts both ways. For the **conservative scalar**
nearest-neighbour part of the symbol the natural value is **zero**, not order one (scalar is
load-bearing: the matrix-valued internal-index sector is outside this computation, by its own rider):
with the coupling constant on the full 24-bond orbit, *both* quartic coefficients — isotropic and
anisotropic together — vanish identically, the emergent dispersion is exactly isotropic through that
order, and the orbit-constant point is the unique root of either coefficient. What genuinely carries this
exposure is therefore the orbit-*splitting* channel — the instance's chiral-bond support sits on a
sub-orbit, and at that extreme the coefficients are of order `10⁻²` in the substrate's own normalization;
converted to the bound's variable they *straddle* the unconditional limit across the lattice-scale band,
and sit about five orders above the composition-conditional corner — together with the
**driven-dissipative sector**, which no conservative computation reaches. Its leading lattice face is
named: the drive's one-way character permits a forward/backward asymmetry on the advance-axis bonds — a
non-reciprocal channel, odd in the advance frequency, invisible to every even symbol and outside any
polynomial-invariant argument on the even part — so the driven weight space is three-dimensional, and an
even-sector answer alone does not settle it. Whether the dressed couplings sit at the orbit-constant
point is a finite, named computation the programme owes, and the suppression the limits demand remains
owed in the dissipative sector regardless.

**If the substrate dynamics deliver a coefficient of order one, this candidate is dead — not evolved.**
And "this candidate" is exact rather than a hedge: what dies is killed at three pinned choices in series
— a *regular* arrangement, its *back-fit* size, and *one* induced-gravity chain to denominate that size
in Planck units at all. **Those three are not three independent escapes; they are one vise.** The size
the dimension-six bound excludes is the size the gravity route needs, because the grain's Planckian size
is itself the gravity back-fit — fitted from the measured Newton constant through that chain, not an
independent commitment. So a member that moves the grain to escape the bound moves the very number the
gravity chain was denominated against and owes that chain again; and a member that holds the chain holds
the grain where the bound bites. **The exposure and the gravity route grip the same pinned choice from
opposite sides, and loosening either tightens the other.** A member proposed at the irregular-discrete
branch inherits a different constraint rather than a lighter one: no finite-valency graph can be
associated to a sprinkling consistently with Lorentz invariance, so such a member must say which of
discreteness, Lorentz invariance and finite valency it gives up.

**The electroweak crossing scale.** `sin²θ_W = 3/8` is a **normalization identity** at the scale where
the two electroweak stiffnesses coincide — not a prediction of the measured value. The crossing scale
itself is not derived at all, and this candidate's one computable reading of it lands 0.154–0.158 against
a measured 0.2312: a 33% miss of a five-digit number, with the four standard escape routes computed and
closed — descent and closures alike inside an imported elementary-field renormalization-group frame that
this candidate's own emergent / composite gauge sector does not itself license, and if that premise fails
the reading is not refuted but gated. What the miss indicts is this candidate's arrangement and its
calibrations.

**A third exposure, live and internal.** One of this candidate's own picks is under rework and the result
is not yet in. The bond truncation keeps two of the symmetry-allowed constants; the discarded directions
were shown to be a six-parameter family the corpus had never enumerated, and while the survivor of the
Lorentz cut is quadratically inert and exactly zero on both computed vacuum branches, the **second
chirality dial is a leading-order actor**. It can cancel the canting near a ratio of about one half — a
cancellation line that exists independently of normalization, though its location does not — and on that
line the chiral-symmetry-breaking spine goes away. It also moves the vacuum's preferred direction, and
the survivor's exact vanishing is a property of that direction being high-symmetry, so the two findings
travel together. **The numerical spine is therefore live — and what the calibration measures is in any
case a ratio of totals, a parity-odd bond amplitude over a parity-even one, so the ratio is not to be
quoted as a pinned single-parameter measurement of the two constants separately.** §2's family-level
structural results are untouched by it.

**A fourth exposure, and it is not yet discharged.** Priced on this candidate's own banked stiffness
and branch gap, a soliton core exploring the gapped directions of the cell-scale order-parameter
space would be a few lattice spacings across, against the vastly larger scale a hadron requires. The
topology of that target space is separately open and is registered as a pick. The pricing is an own
estimate rather than a banked computation, which is why no size ratio is quoted here; neither
question is settled, and either could remove this candidate's hadron sector using its own machinery.

## 5.4 What the family-and-candidate split does not buy

**The family is not vindicated by carrying neither wound.** It carries neither because it makes no
numerical claim at either place, and a family that has not yet said a number cannot be wrong about one.
The wounds are the price of being the only member that says numbers at all, and the family-and-candidate
architecture is a bookkeeping fact.

**The family does not yet have a candidate it would call very good. The first one is published in full**
— its picks, its calibrations, its mass and mixing material, its wounds at full technical depth, its
result index and its engine map — in the instance dossier `TWT_foundational_paper.md` and its companion,
at the repository. A reader who wants to attack this programme should attack there, and §5.3 says where.

---

# §6 — Method

## 6.1 How a claim gets in

No load-bearing claim is banked on the developer's say-so. Each is attacked by an independent reviewer in
a fresh context, briefed to argue against the submitted conclusion; verified on the substrate engine
where applicable; and graduated only when developer and reviewer agree on its tier and its scope. Two
further roles run beside the reviewer with deliberately different information: a referent checker,
starved of the derivation, which asks whether a claim is *about* what it says it is about — the class of
error where the mathematics is entirely correct and the result is still wrong; and a coherence keeper,
saturated with the whole admitted result set, which asks whether the corpus now asserts one consistent
thing. The keeper adjudicates symmetrically: dismantling an old banked result is a legitimate and
expected outcome, and recency is not evidence.

**What "independent" means here, and what it does not.** The reviewers are AI instances in fresh
contexts, and so is the developer. That buys independence of *context* — no memory of the submission, no
stake in it, an adversarial brief — and not independence of *priors*: instances of the same or a related
class share training and therefore share blind spots. This programme measures that rather than assuming
it away. Same-class review was measured near-useless over a month of it, and a cross-class pass over the
identical corpus then surfaced real defects in one session; and an external round put two different
classes onto the same material and recorded them making one identical error in the incumbent's favour,
which is exactly the correlation cross-class separation cannot reach. The guards are therefore structural
rather than demographic: every verdict-bearing review is briefed to argue against the conclusion, a clean
bill returned with no adversarial brief is recorded as carrying little information, and every verdict
later overturned by arbitration is logged against its role and its class in a calibration ledger. **A
correlated reviewer is a weaker instrument than an uncorrelated one, and the claim of independence above
is to be read at that strength.** One assumption sits on top of that bound, and this programme made the
mistake before it wrote the sentence: *the same reviewer returned twice* and *two fresh instances of one
class returned once each* are different objects, and the second is the weaker. A returning instance with
no memory supplies no incremental independence — only the same priors sampled again — so a record that
keys accumulated review to a persisting reviewer identity credits a continuity it does not have. What
accumulates here is the **record**, not the reviewer.

Three mechanisms do the work the roles cannot. Every algebraic claim has an **engine primitive with a
check**, and quantities the programme cannot compute are wired to **raise** rather than return, so an
unearned number cannot be used by accident. Every **new check ships with its failure demonstration** —
run against a deliberately broken tree and shown to fail for the named reason, because a check banked
without a demonstrated failure mode is an assertion about a check. And every **external theorem is
registered** with its premises, the level it is applied at, its status on the ontology and the handle
that would retire it, so a wrong import can be excised precisely: strike the row, fire the listed revert
clauses, and the dependent results fall back to their pre-import tiers rather than collapsing ambiguously.

## 6.2 How a claim gets out

Every dead end is recorded as **tried X → failed because Y → would change if Z**, never as an
impossibility; `TWT_NEGATIVES_LEDGER.md` carries sixty-plus of them, including closed routes through this
programme's own favoured constructions. The mirror rule binds the other direction: every necessity claim
— "the only route", "forced", "no alternative" — carries its **conditioning class in the same sentence**,
exactly as every impossibility carries its would-change-if. Every load-bearing choice enters a **family
tree** in the same pass it is made, with the menu it came from, the named result that required it, and
what un-picks it — which is what makes §5.1's table a table of branch points rather than of conclusions.
Every ruling that governs the corpus carries its dependents and its **revert list**, so a reversal is
executable rather than editorial.

## 6.3 The failure mode this method has

The magnitudes are not undone for want of trying. They are **gated, for a stated reason of
knowability**: the exact microscopic kernel of a driven medium is underdetermined from inside the lock,
in principle and not merely in practice — nobody derives a fluid's transport coefficients from its
molecules either, and Navier–Stokes is not thereby a placeholder. What is reachable from inside is a
**compatible effective kernel class with a small counted constant set**, and the accomplishment on offer
is parameter compression: a configuration→mass map rather than a list of fitted numbers. That boundary is
stated here at the front rather than discovered by a reader at the back, and it is why the engine raises
on a gated quantity instead of returning an estimate.

**And the deliverable is a family, not a winner — which is the honest form and not a hedge.** A single
kernel presented as *the* kernel would assert an exclusion the programme cannot make: nothing in hand
rules out the other members that would have worked too. So what is owed is a **list of surviving
candidates**, each self-coherent, and the list is **empirically bounded** — members are removed by
measurement, not by preference. At this stage that is probably the only honest way to hold the question
open, and stating it as a family is what keeps the programme from quietly converting an unforced choice
into a claim.

The apparatus exists to make both of those checkable rather than assertable: tiers, an executable suite,
an import registry with revert clauses, and §3's separator — which is there because structure, unlike
arithmetic, is not caught by running the code. **The risk this design actually carries is different from
the one it was built against, and is worth naming precisely:** an instrument that generates findings
about itself faster than the physics moves. The counter is not another instrument; it is the ratio the
programme reports against — premises interrogated versus premises discharged — and that number is
published rather than described. This paper is developed with AI assistance under that protocol.

One measured instance cuts both ways. The two family-level physics debts named in §4.4 entered the record
after an external cold review asked for them — and this programme's own internal probe had already
recorded the same absence, in writing, before that review returned. The apparatus had produced the
observation and had not filed it. **The fair reading is that the apparatus works, later than one would
want.**

The apparatus is a separate artifact from the theory, **built to be rigorous** rather than described as
such, and it is published — the rules, the roles with their deliberately different information
diets, the manuals, the gates and their generators — in the `apparatus/` directory of
**https://github.com/yaerhf/TWT**, beside the engine it governs,
so a reader can audit not only the results but the process that admitted them. The measured incidents the
design rests on, and the honest caveat that a ratchet can be emptied, are in its own documentation.

---

## Related work

Credit for the constructions this family converges on. Neither side of any convergence below is evidence
for the other.

**The weak host as a chiral half of a four-dimensional rotation algebra.** Nesti and Percacci note that
chiral fermions couple to gravity through only the self-dual `SU(2)` subalgebra of the complexified
`SO(3,1)` algebra, identify the anti-self-dual subalgebra with `SU(2)_L`, and build a graviweak
unification on that identification (*J. Phys. A* **41**, 075405 (2008); arXiv:0706.3307); their later
work obtains one chiral `SO(10)` family from a Majorana–Weyl representation of a unifying `SO(3,11)`,
continuing that programme in the GraviGUT direction rather than redeveloping the `SU(2)_L` identification
(*Phys. Rev. D* **81**, 025010 (2010); arXiv:0909.4537). Alexander, Marcianò and Smolin join the weak
`SU(2)` gauge fields to a chiral half of the space-time connection and read the chirality of the weak
interaction off that joining (*Phys. Rev. D* **89**, 065017 (2014)). Anyone meeting §2.4 should meet that
literature with it. **The construction here was not built from those papers.**

**Where the constructions part, in one algebraic sentence.** Both graviweak lines must **complexify**
before they have a split at all: real `so(3,1)` is simple, in Lorentzian signature the duality operator
squares to `−1` with eigenvalues `±i`, and no real `su(2) ⊕ su(2)` decomposition exists there — which is
why `SU(2)_L` appears there as a compact real subgroup cut out of an `SL(2,ℂ)` factor, with the chirality
selected by an assumed vacuum expectation value of the soldering form. The split used here is a **real**
one: in Euclidean signature the duality operator squares to `+1`, both halves are compact real forms
already, no complexification and no symmetry-breaking vacuum expectation value enters anywhere, and the
halves are distinguished by which side of the local state they act on — body frame against space frame —
rather than by one half *being* the spacetime connection. **Two fences ride that delta, so it is not
quotable alone.** The real split is bought with Euclidean signature — the same purchase whose unpaid
reconstruction debt §2.2's first fence registers; the advantage and the debt are one fact seen from two
sides. And "no vacuum expectation value" means no *mechanism*: where the graviweak line selects its
chiral half dynamically, this family **dissolves** half the selection and **reads** the other half —
self-dual against anti-self-dual is a relabelling with nothing banked to pin the orientation, and chiral
against diagonal is settled by the right-handed-singlet datum. A dissolution and a datum are legitimate
moves, and they are different moves from an answer. What §2.4 adds beyond the identification is that the
menu of hosts is computed closed rather than chosen inside one.

**Other credits, by the section that uses them.**

- *§1.2's `ℤ₂` branch* — sign-even orientation bilinears producing a local `ℤ₂` gauge structure with the
  physics relocating to the covering sector: Lammert, Rokhsar & Toner, *Phys. Rev. Lett.* **70**, 1650
  (1993); *Phys. Rev. E* **52**, 1778 (1995).
- *§2.1's charge-quantization literature* — Foot, Lew & Volkas, *J. Phys. G* **19**, 361 (1993); Geng &
  Marshak, *Phys. Rev. D* **39**, 693 (1989); Minahan, Ramond & Warner, *Phys. Rev. D* **41**, 715
  (1990) for the anomaly-plus-Yukawa route; Babu & Mohapatra, *Phys. Rev. Lett.* **63**, 938 (1989) and
  *Phys. Rev. D* **41**, 271 (1990) for the Majorana closure of the `B − L` flat direction; Pati &
  Salam, *Phys. Rev. D* **10**, 275 (1974) for the fourth colour, whose internal `U(1)` direction is the
  one later usage calls `B − L`.
- *§2.2's third fence* — Gomes & Koslowski's shape-dynamics treatment answers the preferred-foliation
  objection, offered as a citation rather than as a derivation of our own; and the programme that
  historically *recovered* reflection positivity in a Euclidean quantum-gravity setting did so by
  reintroducing a distinguished causal structure (causal dynamical triangulations; Ambjørn, Jurkiewicz &
  Loll) — external precedent for the necessity of something like the lock, not a derivation of it.
- *§2.3's non-associative alternative* — Furey's division-algebraic programme builds one generation's
  representation content from exactly the non-associative factor (arXiv 1611.09182; *Eur. Phys. J. C*
  **78** (2018) 375; Furey & Hughes, *Phys. Lett. B* **827** (2022) 136959), developed independently and
  reaching related conclusions by different means.
- *§2.4's fourth fence* — Nielsen & Ninomiya, *Phys. Lett. B* **105**, 219 (1981), cleanest proof in
  Friedan, *Commun. Math. Phys.* **85**, 481 (1982).
- *§2.5's radiative-naturalness obstacle* — Collins, Perez, Sudarsky, Urrutia & Vucetich, *Phys. Rev.
  Lett.* **93**, 191301 (2004).
- *§2.5's D4/F4 point-group protection* — Neuberger proposed F4 lattices for exactly this reason
  (*Spinless fields on F(4) lattices*, *Phys. Lett. B* **199**, 536 (1987)); Chow (1999) states the
  group-level form, that D4 is exactly isotropic at order `a²` and is the only unexceptional root lattice
  with the property, protected by the accidental threefold Dynkin-diagram symmetry; the two-sided
  sharpness is established in the lattice-kinetic-theory literature (Chen, Goldhirsch & Orszag, 2008);
  the 24-cell's spherical 5-design property is classical (Delsarte, Goethals & Seidel, 1977); and the
  formulation remains live (Katz & Nográdi, arXiv:2512.10604).

**The substrate-realist company.** The Stueckelberg–Horwitz–Piron tradition has held an evolution
parameter distinct from observed time for eighty years. Volovik's quantum-vacuum-as-medium programme
holds the substrate-realist premise outright and in print, obtaining from a worked microscopic model
emergent Lorentz invariance in a low-energy corner, chiral fermions, gauge fields as collective modes,
topological defects, and an inner observer who cannot see the substrate's own geometry (*The Universe in
a Helium Droplet*, Oxford, 2003) — and it is his medium that yields species-dependent effective metrics
generically, recovering a single one only where a vacuum symmetry connects the species, the opposite
conclusion to C9's for its own medium. A third, smaller literature reformulates special relativity on a
four-dimensional Euclidean space with proper time as the fourth axis. **Matter-as-defect remains this
programme's own**, as does the conjunction: that the medium's motion *is* the second time's advance,
which a defect's phase must match. Five corrections bind these kinships and none of them is optional, so
each travels with every use of the kinship it binds: the quadratic map between their meta-time frequency
and mass; their gravitational extension's frame cost; the scope of Volovik's inner-observer blindness;
the limits on his emergent `SU(2)`; and the circular-boost distinction against a Euclidean **rotation**
reading of a boost — a fact about constructions; which papers in that literature carry the circular
reading is not answered here.
**Kinship moves the family from isolated to a member of a small, respectable tradition. It is not
evidence that the family is true.**

---

## Misreadings

Readings this paper does not support, listed so they can be checked against the text.

- *"Quantum mechanics is derived from the substrate."* §2.7 is a relocation with a gain; the composite
  state space is assumed and the single-outcome mechanism is open.
- *"The Lorentzian signature is derived."* §2.2 relocates it onto an axiom and derives what follows.
- *"Charge values are derived."* Integer-valuedness and the `c`-free neutrality identity are; the
  per-state values are assigned (§2.1).
- *"Hydrogen neutrality distinguishes this family from the incumbent."* It does not, and this paper does
  not claim the incumbent permits a charged hydrogen atom; the neutron's charge is what would separate
  them (§2.1).
- *"The `ΔB = ΔL = 3` selection rule is a substrate result."* It is the incumbent's rule, imported at the
  effective level (§2.6).
- *"Colour is a gauge group here."* It is not, anywhere in the family — which is what §4.4's sharpest
  exposure is about.
- *"This is a claim to be the most falsifiable theory in physics."* §4.1's kill condition is the
  strongest option available at family level, not a claim about the whole literature.

---

## Closing

This paper states a family, what it derives, what that costs, what would kill it, and where its first
candidate is wounded. The strongest thing in it is a discrete charge spectrum obtained from topology
without a unifying group, together with a neutrality identity that holds for every value of the
normalization constant — earned, conditioned, and checkable in one line. The weakest is that every
magnitude in the programme waits on one object nobody has built.

We would rather be shown wrong on a specific claim than credited on a general one, and the place to start
is §5.3.
