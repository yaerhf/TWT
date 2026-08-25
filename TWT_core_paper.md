# TWT-Core — a family of substrate theories, what it derives, and its first candidate

*Yaer Aharon Haddad Fennech · Independent Researcher · hfyaer@gmail.com*

*Engine, verification suite, and the instance dossier — `TWT_foundational_paper.md` with its*
*companion `TWT_foundational_paper_companion.md`: **https://github.com/yaerhf/TWT** —*
*`pip install -r requirements.txt && python twt_test.py` reproduces every algebraic claim below.*
*The research apparatus this programme runs on — its rules, roles, gates and telemetry — is*
*published separately at **https://github.com/yaerhf/research-ratchet** (§6).*

---

## Abstract

**Reference class.** This is a structural-derivation programme with one named unbuilt object, not a
completed unified theory. It defines a **family** of theories — TWT-Core, seven axioms and one
refusal — and it publishes the family's **first candidate member**, V3, which is built all the way
down to numbers. The family says which Standard-Model structural facts follow from which premises.
It says no magnitudes, and it says why: every coupling, absolute mass and absolute scale in the
programme is downstream of the driven-dissipative substrate dynamics, which is unbuilt and named as
such throughout.

**What the family derives, with each condition stated once.** Electric charge takes values in a
discrete lattice because winding number is an integer — consuming the matter-as-defect axiom and the
winding character of the endorsed defect class, and nothing more of that endorsement — so there is no
continuous parameter available by which a proton and an electron could come to differ. Hydrogen neutrality is an
identity in the charge functional's normalization constant — it holds for every value of that
constant, so nothing was tuned to make the two cancel — given four named structural premises, an
entered anchor, and the weak-sector assignment those premises consume. Lorentz kinematics is a
four-axiom result: `Cl(4,0) ≅ Cl(1,3)` is a theorem, the timelike placement is an axiom of the
family, and a wavefront-locked observer inside a positive-definite substrate therefore reads its own
kinematics as Lorentzian — kinematics, not relativistic field theory. Four-dimensional space carries
exactly three anti-self-dual planes, so the family makes exactly three generation seats available,
given the identification of those planes with generation seats and an associativity premise. The
complete list of three-dimensional subalgebras that could host weak isospin inside the substrate's
rotation algebra is computed closed at three conjugacy classes, one of which is the same assignment
mirrored and one of which is refuted by the observed weak-singlet character of the right-handed
fermions — so the weak assignment is forced given one endorsed premise and one datum read from
experiment, and generation-blindness, the doublet structure and the up-sector's chirality follow
from it — as does V−A, named last because it is the entered datum in Dirac-bilinear form rather than
a fourth output.

**The exposures, stated by us and first.** Both belong to the first candidate, not to the family.
The isotropic dimension-six Lorentz-violation coefficient's natural value at that candidate's own
lattice scale is excluded by existing cosmic-ray and gamma-ray limits by three to nine orders of
magnitude. The electroweak crossing scale is not derived at all, and the candidate's one computable
reading of it lands a third below the measured `sin²θ_W(M_Z)`, with the four standard escape routes
computed and closed — descent and closures alike inside an imported elementary-field
renormalization-group frame this candidate's own emergent gauge sector does not itself license. The
family carries neither wound because it makes no numerical claim at either
place, and that is not a defence.

**How to check it.** The algebraic content is backed by an executable public suite in which the
quantities the programme cannot compute raise exceptions rather than return numbers. A passing suite
is a statement about Clifford identities and bookkeeping, not evidence about physics; every section
below says where its conclusion outruns what its engine primitive asserts. The first candidate's
full technical development — its picks, calibrations, mass and mixing material, and its wounds at
full depth — is the instance dossier `TWT_foundational_paper.md` and its companion, both at the
repository above, and it is cited by section from here: the section-for-section map is the last
block of *How to read this paper*.

---

## How to read this paper

Six sections. §1 states the family: seven axioms, one refusal, and the wave picture told once. §2 is
what the family derives with no candidate at all, one condition per result. §3 is what that costs
measured against what it is competing with, at family level only. §4 is the falsification surface:
the family's one total kill condition, what it forbids and where those prohibitions are being
tested, the classification of its open questions, and what any candidate must deliver. §5 is the
first candidate — what it pins, what its numbers are worth, where it is
wounded. §6 is the method.

**Where the bookkeeping lives.** This paper carries no inline tier tags and no result numbers. Every
claim's recorded tier, its engine primitive, its dependency edges and its premise rows live in
`TWT_foundational_paper_companion.md`, the bookkeeping volume that ships with the dossier; the
dossier `TWT_foundational_paper.md` is authoritative for the first candidate's technical detail
wherever it and this paper differ. Pointers here are invitations, not dependencies: this paper is
meant to be read on its own.

**Four checks, five minutes each.**

1. `git clone https://github.com/yaerhf/TWT && cd TWT && pip install -r requirements.txt && python twt_test.py`
   — expect `ALL CHECKS PASSED` (on Windows, set `PYTHONUTF8=1` first).
2. `weak_su2_menu_exhaustion()` — the finite classification sweep behind §2.4. Its only mathematical
   input is the engine-exact structure constants of the substrate's rotation algebra; it returns
   three conjugacy classes and the residuals of the candidates that fail to close.
3. `charge_normalization_anchor_free()` and `charge_sector_provenance()` — the first returns the
   neutrality identity together with the counterfactual that breaks it; the second returns, machine
   readably, which primitives in the charge block compute and which assign. The suite asserts that
   every primitive in that block sits on exactly one side, so an unclassified addition fails.
4. `alpha_em_value()`, `texture_tetrad()`, `qcd_collider_phenomenology()` — confirm they raise rather
   than return. Where the programme cannot compute, it is wired to fail loudly.

**Where the detail is — this paper's sections against the dossier's.** The dossier is
`TWT_foundational_paper.md` (Parts A–E, the first candidate's full technical development); the
bookkeeping volume is `TWT_foundational_paper_companion.md`; both ship at the repository above,
with the ledgers named in the right-hand column. Nothing in this paper depends on following a row.

| here | in the dossier (and the ledgers) |
|---|---|
| §1.1 the picture | §A.1–§A.5 |
| §1.2 axioms and refusal · §1.3 preferred directions | §A.6.1 · §A.6.3 |
| §2.1 charge | §C.2.1, §C.2.2, §C.2.7, §C.2.8 |
| §2.2 Lorentz kinematics | §B.1.1–§B.1.4, §B.2.2 |
| §2.3 generation seats | §D.2.4, §C.3.8 |
| §2.4 the weak host | §C.4.2 |
| §2.5 Lorentz protection | §B.1.5, and the standalone note `D4_lattice_quartic_isotropy.md` |
| §2.6 the `B − L` triad · the two-winding carrier · the monopole boundary | §C.5.4, §C.5.5, §C.5.6 · §A.2, §A.5.2, §C.1.3 · §B.5.2 |
| §2.7 the quantum package | §B.3, §B.4 |
| §3 the comparative accounting | `TWT_COMPARATIVE_LEDGER.md` |
| §4.1 the kill condition · §4.2 the prohibitions · §4.3 knowability · §4.4 what is not claimed | §A.6.2 · §E.3.1 · §A.6.5 · §D.5, §E.2.3 |
| §5.1 the picks | §A.6.4, and `TWT_FAMILY_TREE.md` |
| §5.2 the numbers | §E.2.1, §E.2.3, §C.1.2, §C.3.5, §C.3.11 |
| §5.3 the wounds | §E.3.5, §C.4.5, §D.4.3 |
| §6 the method | companion Section 6, and `TWT_NEGATIVES_LEDGER.md` |

---

# §1 — The family

## 1.1 The picture, once

Time is a wave, and we are riding it.

The substrate is a four-dimensional Euclidean material medium. It carries a wavefront that advances
along one distinguished axis, and an observer is not a thing that watches the front go by — an
observer is mechanically locked to it, and can only ever see a slice. That lock is what makes `c` a
property of the medium rather than a coincidence of the observer: `c` is the front's advance rate.
Applied once it converts winding-per-length into oscillations-per-second; applied twice it is the
`c²` of `E = mc²`, and the universality of that factor is the monism of the substrate — one medium,
so one conversion, so inertial and gravitational mass are one quantity rather than two that happen
to agree.

Matter is not a substance sitting in the medium. It is a **defect** of the medium — a protected
pattern, stabilized by topology rather than by a binding energy, and a defect has several
independent axes on which it can be defective: its winding, its deficit of carrier rotation, an
internal rotation perpendicular to the advance, a notch in the amplitude. Collapsing those into one
scalar is the recurring error in reading this picture, and the picture is not to be read that way.

Mass is the frequency of the defect's rotation in meta-time. From inside the wavefront — the frame
every measurement is made in — matter reads as something positive over a vacuum at zero. From
outside, the vacuum is the full carrier and matter is where the carrier is missing. Both readings
are appearances of one thing, and the one thing is the defect. The hole is a picture and so is the
positive; neither is a premise, and no argument in this paper reasons from either.

Two consequences of the lock bind everything that follows. **The inside frame is where data comes
from; the outside frame is where derivations are done.** Reasoning *from* the inside view is the same
trap as reasoning from the Standard Model's own frame: it imports what is supposed to be explained.
And **the medium has two scales that must never be collapsed into each other** — the grain layer,
whose constituents are the medium's smallest parts, and the emergent cell layer, where solitons and
hadrons live. The two-layer architecture is a commitment of the family. The *value* of the grain
scale is not: in the first candidate it is back-fitted from the measured Newton constant, and that
is a fitted number, not an axiom.

## 1.2 Seven axioms and one refusal

A theory that has all seven is a member of the family. A theory that drops any one of them is a
different theory, however much else it shares. The seven are stated here in the form the family
charter fixes them, verbatim.

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

Four notes belong with the list and nowhere else.

**On S2.** The axiom's *"squares to −1"* clause is easy to misread as placing the observer's
Lorentzian signature, and it does not: the observer's time is the advance axis, which squares to
`+1`, and §2.2's arc is independent of S2 outright. **What the clause places is a complex structure.**
The four-dimensional substrate algebra is central simple over the reals — its centre is the scalars,
so no *central* element of it squares to `−1`, however many non-central ones do. Adjoining a
generator of negative square is what makes the extended algebra carry a central copy of the complex
numbers rather than splitting into a real direct sum, and the resulting central unit `E = I₄e₅`
satisfies `E² = e₅²` exactly — the axiom's sign is that unit's sign, so the clause is genuinely
consumed rather than decorative. What it buys is the substrate's **one global phase**: a single phase
circle every configuration can carry, on which the colour carrier, the carrier structure along the
advance direction and the mass floor are all built. Negating it in the engine is a measured
experiment rather than an argument — eighteen primitives and four of the suite's ten modules change
their answers, and nothing in §2 does. **So S2 is a phase placement and not a signature placement**:
it earns its axiom cost, and it earns it entirely outside the list §2 publishes, which is why §2 read
alone appears not to need it.

**On LS.** The axiom is stated witness-free: it fixes the size of the local state for any grain
structure, and each member re-witnesses it on its own grain. Its `ℤ₂` clause is deliberately not
decided. Both branches deliver identical windings and identical fermionic-quantization structure, so
the observed fermionic character of matter cannot pay for the choice; the discriminators, if any
exist, are the substrate's own bond energetics, the sign-defect sector, and the emergent covering
construction. The general shape of the second branch — sign-even orientation bilinears producing a
local `ℤ₂` gauge structure with the physics relocating to the covering sector — is prior art
(Lammert, Rokhsar & Toner, *Phys. Rev. Lett.* **70**, 1650 (1993); *Phys. Rev. E* **52**, 1778
(1995)), credited here rather than in a bibliography.

**On B-6.** The safe option was available and was declined: leave the foliation unnamed. A theory
with an unnamed preferred foliation cannot be caught, because "there is a frame, somewhere" survives
every measurement. Naming it as the comoving frame turns a metaphysical posture into a target, and
that target is the family's kill condition (§4.1).

**On the refusal.** Its consequence binds every reader of the technical corpus: the rotor field that
runs through the first candidate's development and through the engine is **instance-level
description** of the medium — a way of writing down what the medium is doing — and is not the
ontology. An argument that needs the field to *be* the world is not a family-level argument. The
refusal is scoped, and the scope matters: a field is refused only as a *fundamental description of
what the world is made of*, never as a mathematical description of an **emergent property** of the
medium, the way temperature is a field-description of molecular motion — which is why the field
formalism works as well as it does. Two things ride that reading as commitments rather than
conveniences: the grain-to-cell map is a real physical relation, plausibly driven by the wave,
rather than a bookkeeping device between two levels of description; and the cell's first description
is an emergent pattern. Note also what the refusal does not say. It is about what the substrate
*is*, not about whether it is grainy. Graininess is a preferred direction, not an axiom.

## 1.3 Preferred directions, and what they are not

Eight further commitments are endorsed as highly plausible and are **not** part of the definition. A
candidate that goes the other way on any of them is still a member of the family:

grain discreteness · Skyrmion-class defects · carrier structure along the advance direction ·
the practice of anchoring on a measured constant and back-fitting · the Koide amplitude `c = √2` ·
the identification of a defect's mass with its vacuum-subtracted rest cost · generations as the
anti-self-dual triple with an associativity premise · and the **weak-hosting premise**: that weak
isospin is hosted by a three-dimensional `su(2)` inside the substrate's own rotation algebra at all.

The distinction between an axiom and an endorsement is load-bearing in one direction in particular.
A large block of what follows in §2 is derived *given* one of these endorsements, and those results
are family property only in that conditional sense: they stand or fall with the endorsement they
consume. Where that is the case below, it is said in the same sentence as the result.

---

# §2 — What the family derives with no candidate

Six results, and one package. Each is scale-free: the family has zero earned dimensionful scales,
and everything in this section is a sign, an integer, a dimension, a ratio or an algebra identity.
That is not an accident of what has been attempted. It is the shape of what a scale-free axiom set
can deliver, and §4.4 states the corresponding limit.

## 2.1 Charge: a discrete spectrum, and a neutrality identity

**Charge is quantized because winding number is an integer.** `π₃(S³) = ℤ` gives a discrete charge
lattice and protects it against drift: there is no continuous parameter available by which a proton
and an electron could come to differ. **This half is family property**: it consumes the
matter-as-defect axiom together with the winding character of the endorsed defect class — that much
of the endorsement and no more, since integer-valuedness is what any winding-class defect supplies —
and it consumes no candidate pick at all. It is exact, and a re-anchored or re-arranged candidate
inherits it unchanged.

**The two algebraic facts the rest of this subsection runs on.** Both are one-line computations in
the substrate algebra, and both are worth doing rather than reporting.

*Hypercharge is a bilinear sign.* For a grade-three blade `B` of the substrate algebra, direct
computation gives

> `B̃ · e₄ · B = (±1) · e₄`,

the bilinear mapping each grade-three blade onto the advance axis with a sign that depends on the
blade. The advance-bearing trivectors — `e₁₂₄`, `e₁₃₄`, `e₂₃₄` — return `+e₄`; the purely spatial
trivector `e₁₂₃` returns `−e₄`. **The two orbits carry opposite signs**, and that opposition is the
whole content of the hypercharge bracket below. Hypercharge is then constant across each weak
doublet, forced by Schur's lemma, since it must commute with the doublet's generators.

*The orbit of three is what makes a three-facet decomposition available.* The three advance-bearing
trivectors compose to the advance axis,

> `e₁₂₄ · e₁₃₄ · e₂₃₄ = e₄`,

and the product is **alternating**: the three even orderings return `+e₄` and the three odd ones
`−e₄`, so the sign belongs to an *oriented* triple rather than to an unordered set of facets, and an
orientation convention has to be named wherever that sign is used. What the orbit supplies is a
structure with exactly three advance-bearing members and one spatial member carrying the opposite
bilinear sign. **The step from that to a charge is an assignment and not a computation**: blade
composition is multiplicative and charge is additive, so passing between them requires a
homomorphism, and the homomorphism — one third of the integer winding per facet — is entered, as the
provenance paragraph below records. The fractional values `±1/3, ±2/3` follow from that assignment
together with the per-blade bilinear signs, and **no per-defect value outside `{0, ±1/3, ±2/3, ±1}` is reachable in
the algebra at all**. Composite charges are integer sums of those units and are not confined to the
list: the engine's own three-facet table returns `+2` for `uuu`, the `Δ⁺⁺`. What the algebra fixes is
the unit, not the total.

**And hydrogen neutrality is an identity in the charge functional's normalization constant.** Write
the functional in the standard form `Q = T₃ + c·Y` with `c` left free. Then

> `Q_p + Q_e = [2T₃(u) + T₃(d) + T₃(e)] + c·[3Y_Q + Y_lep] = 0 + c·0 = 0`

**identically in `c`.** Both brackets vanish separately. The isospin bracket vanishes because `uud`
plus the electron is one complete quark doublet plus an up-versus-down-opposed pair; the hypercharge
bracket vanishes because the `e₄`-bilinear gives the two orbits opposite signs and the trivector
orbit supplies the factor of three — the `3 × 1/3 = 1` arithmetic, **written throughout in the
normalization `Y_lep / Y_Q = −3`, three times the conventional hypercharge scale**. Nothing was tuned to make
the proton and the electron cancel, and the same computation returns the neutron-neutrino
cancellation and singles out `uud` uniquely: of the four three-facet composites only `uud` lands at
minus the electron's charge. This is what turns the `10⁻²¹` neutrality measurement from the datum
that calibrates the theory into a test of it.

**The condition, stated here once.** The identity rides **four named structural premises plus an
entered anchor**, and the four are these: that measured electric charge is the eigenvalue of *one*
universal linear generator across all sectors (P4); that the charge is chirality-independent per
defect (P5); the inside-frame identification of the proton with the three-facet composite `uud`
(P6); and the cross-sector weak-isospin alignment placing the charged lepton in the slot opposite
the doubly-represented quark (P7). P7 is posited, and it is posited in the engine's own literal:
flipping the lepton slot alone gives `+1`, the quark slots alone `−1`, and only the global flip is a
convention — the engine computes those three counterfactuals rather than asserting them.

**And it inherits the weak assignment.** The isospin bracket is an assertion about which doublet slot
each state occupies, and that reading is supplied by §2.4's weak-host result — which is itself forced
*given* the endorsed weak-hosting premise. So the neutrality identity is family property in the
conditional sense of §1.3: a candidate that hosts weak isospin outside the substrate's rotation
algebra re-derives this identity on its own host or loses it. The discreteness above inherits
nothing and stands either way. Those are two different claims with two different levels, and this
paper does not merge them.

**What is not derived here.** The *spectrum of charge values* — which state carries `+2/3` and which
`−1/3` — is an assignment, not a computation. The winding chain supplies integer-valuedness and
protection; the charge functional supplies the normalization; the values are entered. The engine
marks that boundary explicitly and machine-readably (`charge_sector_provenance`), the anchor is a
parameter of the assignment primitive rather than a frozen literal so the counterfactual is
runnable, and the primitive that performs the assignment is named for what it does
(`charge_assignment_from_anchor`; `winding_charge` survives only as a labeled legacy alias, so that
earlier citations resolve — no winding is computed in it). Two of those counterfactuals are worth
running: requiring one universal `c` across both orbits forces `Q_p − Q_n = 1` exactly and leaves
the absolute anchor free; and deleting the factor of three, the only anchor admitting one universal
`c` is a half-charged proton with a negatively charged neutron. That factor is what makes an integer
nucleon anchor compatible with the premise at all — substrate-specific, not generic.

**One consequence of the same orbit structure, because it is the first question the picture raises.**
If charge comes in thirds because a configuration decomposes into three facets, a single facet in
isolation is not a configuration with a third of the charge — **it is not a valid configuration at
all.** A lone facet is one orthogonal component of one circular winding, and the three are not three
objects bound together; they are one object. The topological reading is the formal shadow of that:
there is no smooth map `S³ → S³` of degree one third. So the absence of free fractional charges in
this family is not a force holding something in — it is a statement about what shapes exist, and it
is the same fact as the charge spectrum above. What that reading does *not* supply is the
short-distance behaviour of the same sector, which is the family's sharpest structural exposure and
is stated at that rank in §4.4.

**Against the incumbent, at equal depth.** The Standard Model postulates both halves. Its
hypercharge assignments are chosen — anomaly-constrained, but chosen — and within the gauge group
alone nothing forbids a proton and an electron whose charges fail to cancel. A grand-unified
embedding or a Dirac monopole would supply it, and one member of that class is a much closer cousin
than the rest: Pati and Salam's fourth colour reads lepton number as the fourth value of the colour
index, extending the group of the three baryonic colours to a four-colour group whose internal `U(1)`
direction is the one later usage calls `B − L` — the same 3+1 arithmetic the two facts above run on
(Pati & Salam, *Phys. Rev. D* **10**, 275 (1974)). The honest framing is therefore not that this
family uniquely earns the 3+1 split, but that it **joins a class of structures that furnish it and is
the only member of that class that furnishes it without buying a group**: that scheme pays with an
enlarged gauge group, a breaking sector, and quark-to-lepton gauge vertices whose flavour-violating
meson decays are experimentally constrained. What is distinctive here is the price, not the
possession — and the price has a matching cost, stated in §4.4: no gauge dynamics is delivered with
it. The point against the incumbent is unchanged: the Standard Model as such does not supply the
cancellation, and this family gets the discreteness from topology without buying a larger group. It is
not the only Standard-Model fact this family obtains from structure rather than postulate — the
generation count, the weak-host closure, the monopole absence and the `B − L` triad are others, each
with its own stated conditions — and the conditioning class matters more than the ranking does.

## 2.2 Lorentz kinematics from four axioms

Take the observer's gamma matrices to be specific elements of the substrate algebra:

> `γ⁰ := e₄`, `γʲ := e₄ e_j`  (`j = 1, 2, 3`),

built from the only ontologically distinguished multivector — the wave's advance axis — plus the
three spatial generators. Direct computation gives `(γ⁰)² = +1`, `(γʲ)² = −1`, and all the
anticommutators vanish, so these four elements satisfy the `Cl(1,3)` Dirac relations with
`η = diag(+1, −1, −1, −1)`. The map extends to a real-algebra homomorphism between two
sixteen-dimensional simple algebras, hence an isomorphism:

> **`Cl(4,0) ≅ Cl(1,3) ≅ M₂(ℍ)` as real associative algebras.**

The neighbouring algebras `Cl(3,1)` and `Cl(2,2)` are `≅ M₄(ℝ)`, a different real algebra — so the
wavefront construction lands on a nondegenerate Lorentzian partner and not on the split one. What is
convention-independent in that statement is the *pattern*: one generator squaring one way and three
the other, rather than two and two.

**And the Lorentz algebra comes with it.** In the same embedding the boost and rotation generators
are `K_j = ½ e_j` and `J_i = −½ e_{jk}` — grade-one and grade-two elements of the *same* substrate
algebra, the first non-compact and the second compact — and they close on `so(1,3)` with the correct
signs. That the boost generator is a grade-one element and not a plane is what makes it hyperbolic
rather than circular: the isomorphism is not grade-preserving at the boost planes, so rapidities add
and velocities compose by Einstein's rule exactly, rather than by the wrong-signed and unbounded law
a rotation of a Euclidean plane would give (§3.4). The commutator of two boosts returns a rotation rather than a boost,

> `[K_i, K_j] = −ε_{ijk} J_k`,

which is Thomas precession: not an added relativistic correction here but a closure sign of the
algebra the observer's frame already is. One consequence worth naming, because it is the reason the
substrate's own geometry is not visible from inside: an observer's three spatial axes are
`γʲ = e₄ e_j`, i.e. **bivectors** of the substrate, each a plane containing the advance direction.
The observer's "space" is literally built out of the direction of travel.

**The scope, stated once.** What is derived is the **emergence of observer-frame Lorentz structure
given the family's wavefront lock**, not the signature itself. The lock is what puts the observer's
timelike direction on the wave's advance axis `e₄`; that is an axiom — S3 — and every theory must
locate its signature somewhere. Note which generator carries the observer's time here: `γ⁰ = e₄`,
and `e₄² = +1`. The meta-time generator does not enter this construction at all, and none of the
five primitives named below computes with it; the arc is therefore independent of S2, which places
the meta-time square. Read strictly, the family *relocates* the signature and gets a theorem in
exchange: given the lock, a wavefront-locked observer inside a positive-definite substrate reads
its own kinematics as Lorentzian, and that reading is forced rather than separately chosen. One
axiom, two facts. It is never to be quoted as a derivation of the signature.

**Why this is the family's cheapest result.** The arc's complete premise set is `{S1a, S3}`, plus
`{S4, S5}` for its matter-sector extension — four axioms, no endorsement, no candidate pick, no
fitted number. The only external mathematics is the real classification of the Clifford algebras
`Cl(p, q)` at `p + q = 4`, which is direct at that dimension. The corresponding primitives take
no empirical arguments at all: `gammas()`, `so13_closure_signs()`, `thomas_KK(1,2)`,
`boost(1)`, `rotation(1,2)` are parameterless algebra calls returning exact multivectors, and the
Lorentz generators, the `so(1,3)` closure signs, Thomas precession and the mass shell come out of
them. That is a machine-checkable difference from every gravity route in the corpus, each of which
takes a fitted default or raises.

**Three fences travel with the result, and none is optional.**

1. **This is kinematics, not relativistic field theory.** The construction delivers signature, the
   Lorentz generators, Thomas precession and the mass shell. It does not deliver a relativistic
   quantum field theory. The Osterwalder–Schrader debt is registered and unpaid: the family has not
   exhibited a reflection positivity for its substrate, so any statement that the Euclidean
   substrate *inherits* a Hilbert space, a vacuum and a self-adjoint Hamiltonian by virtue of being
   Euclidean is asserted, not derived. There are exactly two discharges — exhibit the positivity, or
   say so at every inheritance site — and the second is what is done here.
2. **The antecedent is an axiom, not an endorsement.** This result's conditionality is S3, the
   lock, and it sits inside the definition. It does not sit in §1.3's conditional class, and
   applying that clause to it would demote an axiom to a preference — an error in the opposite direction from the one this paper is
   mostly guarding against.
3. **The family is Lorentz-covariant in the reading, not Lorentz-invariant in the ontology.** S3 and
   B-6 put a preferred foliation under everything. The standing objection that a preferred foliation
   violates relativity is answered here by a published reply with no load-bearing use in the corpus
   (Gomes & Koslowski's shape-dynamics treatment), not by a derivation of our own; that is a citation
   and is offered as one. Worth recording on the other side of the same question: the programme that
   historically *recovered* reflection positivity in a Euclidean quantum-gravity setting did so by
   reintroducing a distinguished causal structure (causal dynamical triangulations; Ambjørn,
   Jurkiewicz & Loll). That is external precedent for the necessity of something like the lock. It
   is not a derivation of it, and it is not offered as one.

## 2.3 Exactly three generation seats

The grade-two part of the substrate algebra is six-dimensional, spanned by the planes
`{e₁₂, e₁₃, e₁₄, e₂₃, e₂₄, e₃₄}`. Left multiplication by the pseudoscalar `I₄ = e₁e₂e₃e₄` is an
involution on that space — `I₄² = +1`, a real duality and not a complex unit — so grade two splits
into its `+1` and `−1` eigenspaces, the self-dual and anti-self-dual planes. Taking the trace of the
projector `(1 − I₄·)/2` on grade two gives the dimension of the anti-self-dual half directly:

> `dim Λ²₋(ℝ⁴) = 3`,

**computed rather than asserted over a hand-written list** — the same six-dimensional space that
supplies the local state of §1.2, read through its own duality. Four-dimensional space carries
exactly three anti-self-dual planes, so the family makes exactly **three seats available by its own
geometry**, and a fourth generation is structurally forbidden rather than excluded by a tuning of
mass scales.

Three conditions, stated once. Reading the three anti-self-dual planes as **generation seats** is a
preferred direction, not an axiom. And the count runs through an **associativity premise** the
family must own: drop associativity and the octonions offer seven imaginary units, which is not an
outside objection but the family's own named alternative — Furey's division-algebraic programme
builds one generation's representation content from exactly the non-associative factor (arXiv
1611.09182; *Eur. Phys. J. C* **78** (2018) 375; Furey & Hughes, *Phys. Lett. B* **827** (2022)
136959), developed independently and reaching related conclusions by different means. Frobenius's
theorem enters as a structural remark through that premise, not as the operative exclusion.

The third condition is about the seat's **carrier** rather than about the count. Read as an internal
action rather than as a bare index set, the anti-self-dual triple is claimed by at least two
candidate readings at once — three generation seats, or a second weak factor gripping exactly the
half of the even algebra that the first one annihilates, and it may be both or neither — and nothing
at the level of the local algebra separates them; the computation that would is the quantization of
the defect's collective coordinates, and it is not built. What the count is actually read through is
not the triple but the meta-time phase, with the three planes as its index set, so the count does
not sit directly on the carrier question. Whether an index set survives being gauged is a passage
this candidate owes and has not written, so the insulation is a claim about where to look, not a
result.

What the family does not derive at either level is which seat nature occupies, or why. The count is
a fact about four-dimensional space; the occupancy is not addressed.

## 2.4 The weak host: a menu computed closed

Ask which three-dimensional Lie subalgebras of the substrate's grade-two rotation algebra `so(4)`
exist at all. **The answer is exactly three, up to conjugacy, and it is computed rather than
surveyed:**

> **SD** — the self-dual chiral factor · **ASD** — the anti-self-dual one · **the diagonal `so(3)`
> class** `{Stab(v) : v a unit vector}`, of which the `e₄`-free spatial-rotation triple is one member.

The classification's only mathematical input is the structure tensor, which on an orthonormal basis
of either chiral factor is exactly `c·ε_{ijk}`. Total antisymmetry alone forces three facts about
each factor — it has no two-dimensional subalgebra, it is simple, and all its automorphisms are
inner — and Goursat's lemma then reduces the classification of three-dimensional subalgebras of a
sum of two such factors to a finite sweep over projection and kernel dimensions. The sweep returns
those three cases and no others. Two structures the geometry might seem to offer are not on the list
because they are not subalgebras at all: the parity-odd `e₄`-bearing triple, and every proper
"handed" mixture of the two chiral factors, which fails to close because the factors carry opposite
structure-constant signs. The engine returns the failing residuals alongside the classification.

**ASD is not a rival; it is the same assignment mirrored.** The two chiral factors are distinguished
only by the sign of the pseudoscalar, and an orientation-reversing frame reflection exchanges them
exactly while fixing the diagonal class and flipping that sign — verified on three inequivalent
reflection vectors, including a non-basis one, so the exchange is generic rather than an artefact of
the basis. Counted up to the automorphisms of `so(4)` the menu has two entries, not three, and a
candidate that "assigns weak isospin to ASD" is this assignment under the opposite orientation
convention: one member, two descriptions. If some independent object ever pins the substrate's
orientation, this paragraph reverts and ASD becomes a real branch. Nothing in the corpus pins it.

**The diagonal class is excluded by data — and not by the datum one would expect.** Every grade-two
element commutes with the pseudoscalar, so every candidate on the menu preserves both Weyl halves of
the spinor module. Restricted to the half a single-Weyl neutrino occupies, the diagonal class and SD
span the **same** three-dimensional algebra: a left-handed single-Weyl neutrino cannot tell them
apart, and any argument that it can is mistaken. The discriminator is the *other* half. SD
annihilates it outright — that half is a weak singlet sector — while the diagonal class charges it
exactly as strongly as the first, which would make the right-handed fermions a second weak doublet
sector at full strength. They are not: the right-handed fermions are weak-isospin singlets, and
no right-handed charged current is observed at any accessible energy — a datum read, not tuned, and
reversible: an observed right-handed charged current reverses it. The family supplies the occupancy
this argument needs
from its own structure, since the charged lepton occupies both Weyl ideals and that two-ideal
occupancy is its Dirac-mass channel — so the other half is not empty and the datum bites.

**Which side the host acts on is computed, not assumed.** The local state is a full
four-dimensional orientation, so an algebra can act on it from either of two sides, and the two are
not interchangeable. The observer's rotations and boosts act from one side — the space frame. Weak
isospin acts from the other — the body frame, an internal reorientation of the state relative to
itself — and the two actions commute identically, by associativity alone and for every realization
of the lock. That is what makes the weak label a Lorentz scalar rather than something a boost of the
apparatus could turn, and it is why the side is not a free convention: a host acting on the
observer's own side is not such a scalar, and after the lock that side offers a centralizer only two
real dimensions wide, and two commuting directions are never an `su(2)` — so no internal `su(2)`
survives there at all. What the side does *not* touch is the discriminator above: the two chiral
factors sit inside the two central ideals of the even subalgebra, so that discriminator returns the
same table whether the generators act from the left or from the right — an ideal fact, and
side-independent. Three fences travel with that, and a fourth — on the level rather than on the
construction — closes the subsection below. The argument covers a label carried by the local
state; a label carried instead by a defect's collective coordinates is a different construction, and
it is unbuilt. The classification above sweeps the *three-dimensional* subalgebras of the rotation
algebra, so a candidate hosting weak isospin in a larger structure — a two-scale host, say — is
outside its scope rather than refuted by it. And the module the host acts on is itself an open
question for this family: the local state's internal action has two candidate modules on the books,
and the commuting identity is an identity of the algebra acting on itself, which is what makes it
realization-blind. On the even-subalgebra reading, an observer boost realized as a vector — which is
how §2.2 realizes it — does not preserve that module at all, so there the invariance is inherited
from the algebra rather than tested on the module. The side is settled; the module, and the
realization in which the test is non-vacuous, are not.

**What this leaves standing, exactly.** With both alternatives closed, the assignment is not a choice
the family makes. Two things are consumed and both are named. The first is the **weak-hosting
premise** — that weak isospin is hosted by a three-dimensional `su(2)` inside the substrate's own
rotation algebra at all. It is not derived anywhere; it is one of the family's preferred directions,
and a candidate that hosts weak isospin somewhere else is untouched by anything above. The second is
the **datum**: no right-handed charged current is observed at any accessible energy, so the
right-handed fermions are read as weak-isospin singlets — read from experiment rather than tuned.
Given those two, the self-dual host is forced, and generation-blindness, the doublet structure and
the up-sector's chirality follow from it — as does V−A, which is worth naming last rather than
first, because purely-left-handed coupling is what the entered datum says and `V − A` is that same
statement in Dirac-bilinear form. The first three are consequences in domains the datum did not fix;
V−A is the datum wearing different notation, and the arc is stronger stated that way. Divergence at
this node therefore happens one level down, at the endorsement, exactly as it may at any other
preferred direction.

**And the fourth fence, which is on the level rather than on the construction.** Everything above is
a statement about *labels and selection rules*: which states sit in which doublet slot, which
chirality couples, which generation the coupling is blind to. **There is no gauge boson anywhere in
this family.** What is classified above is the host algebra of a label carried by the local state,
not a chiral *spectrum*: `V−A` here means the chirality structure of a current, not the interaction
that current would enter, and the gauge sector sits on the field-reclamation debt of §4.4,
un-reclaimed. The lattice no-go a field theorist reaches for first therefore does not bind this
construction, and the reason is worth stating exactly, because it is easy to mistake for an escape.
Nielsen and Ninomiya's theorem quantifies over lattice theories with a free quadratic fermion action
and a conserved chiral phase (Nielsen & Ninomiya, *Phys. Lett. B* **105**, 219 (1981); the cleanest
proof is Friedan, *Commun. Math. Phys.* **85**, 481 (1982)); no fermion field is defined on this
substrate at all — matter here is a quantized soliton, and the engine carries no anticommuting
structure anywhere — so the hypotheses have no referent rather than being evaded. **That is not an
evasion of the theorem; it is a statement that the family has not yet reached the place where the
theorem applies**, since no chiral spectrum has been exhibited from the substrate either. The
passage that would reach it — exhibiting the observed chiral content as the low-energy spectrum of
the substrate's own solitonic sector — is unwritten, and it is the same debt §4.4 names as field
reclamation. A member that instead introduces a fundamental lattice fermion field inherits the
theorem in full and owes one of its known evasions.

**On the accounting.** This sector's cost was formerly booked as one free input bit — "the choice of
SD". That reading does not survive the classification. Self-dual versus anti-self-dual is not a bit
at all, since the two are related by a relabelling; and chiral versus diagonal is not a free choice,
since it is settled by measurement rather than selected. What the sector costs is the named
structural premise plus one empirical bit, and the bit is one the family reads rather than tunes.
The economy is unchanged in number and changed in kind.

## 2.5 Lorentz protection: what one field buys, and what an arrangement buys

**Family level, from S4 alone.** All matter species inherit the substrate's one light cone exactly
because they are defects of one medium. Matter is not `N` independent fundamental fields each with
its own kinetic term, so there is no independent coefficient in which a relative-boost Lorentz
violation between two species could live: different rest masses, one light cone, and the
dimension-four relative-boost violation is structurally zero rather than tuned.

That defuses a well-known obstacle rather than proving a theorem, and the distinction is kept.
Programmes treating Lorentz invariance as emergent from a preferred-frame substrate face a
radiative-naturalness problem: with a hard, frame-dependent cutoff, loops feed dimension-six Lorentz
violation down into dimension-four marginal operators with coefficients of order `10⁻³` to `10⁻²`,
missing the matter-sector bound by seventeen orders (Collins, Perez, Sudarsky, Urrutia & Vucetich,
*Phys. Rev. Lett.* **93**, 191301 (2004)). The obstacle presupposes its precondition — `N`
independent fields with `N − 1` relative-speed observables — and this family denies the
precondition. What that argument does *not* show is that the substrate is itself exactly
Lorentz-invariant under its interacting dynamics; that question is open and stays open. It collapses
a generically fatal problem about `N` fields into one tractable question about one medium.

**And the whole of it rides one substrate assumption that is not engine-checkable**: that one medium
generates all the radiative corrections, so the induced coefficient really is common to every
species. That assumption is registered as an import rather than carried at a flat derived tag, and
it is stated here as the load-bearing premise it is rather than as a rider — because the family's
own picture argues against it. A defect is defective on several independent axes at once (§1.1), and
species that differ along those axes generically couple differently to the medium's modes; one
medium supplies one *source* of corrections, not one *coefficient*. Getting a universal shift needs
a further symmetry argument — a Ward-type identity forcing the leading correction to be independent
of a defect's internal structure — and no such identity is exhibited here; that is the shape of what
is missing, not a demonstration that nothing else could do the work. The nearest worked substrate
programme in the literature (§3.4) reaches the opposite conclusion for its own medium, obtaining
species-dependent effective metrics generically and recovering a single one only where a vacuum
symmetry connects the species. And the premise has a second face inside this paper: it is the same
proposition as the gauge entry on §4.4's field-reclamation list, so it becomes payable — without the
unbuilt dynamics — the moment the photon is exhibited as a collective mode of the substrate with
universal coupling. So the dimension-four half is closed **conditional on a universality claim about
substrate self-energies**, and the obstacle above is deferred rather than defused. It does not close
the dimension-six residual either way.

**Arrangement level, and said as such.** A member that realizes the grain as a **D4 lattice** gets a
second, sharper protection — but that is a property of the arrangement, which is a candidate pick
and not a commitment of the family. The automorphism group of the D4 root system has order 1152 —
it is `W(F4)`, whose invariant degrees are `{2, 6, 8, 12}` — so its space of degree-four invariant
polynomials is one-dimensional, spanned by `(k²)²` alone. For any dispersion kernel invariant under
that point group and analytic in `k`, there is no anisotropic quartic at all. The degree-six
invariant space is two-dimensional, so the leading rotational anisotropy of the polarization-averaged
dispersion sits at **dimension eight** — reached, not merely bounded. **The two countings run
together throughout this subsection and the convention is worth naming once: degrees are polynomial
degrees in the dispersion relation, dimensions are operator dimensions in Lorentz-violating effective
field theory, and the correspondence is degree four ↔ dimension six, degree six ↔ dimension eight.**
This is not generic to lattices: the simple-cubic lattice admits a two-dimensional degree-four invariant space containing
`Σ kᵢ⁴`.

**Four premises carry that inference and are stated rather than buried.** That a derivative
expansion exists — a non-analytic driven-dissipative memory kernel, which is the family's own unbuilt
object, is not covered by a polynomial-invariant argument at all. That the *full* point group
including triality acts — the reflection subgroup alone has a three-dimensional degree-four space,
and the second shell's two sub-orbits are each anisotropic, cancelling only at equal weight, so a
substrate coupling weighting triality-related orbits unequally would restore dimension-six
anisotropy. That the kernel is a scalar in the internal index: the theorem governs the
polarization-averaged dispersion and does not cover matrix-valued kernels, which the point group
cannot close. And that the symmetry **operative** on the sector the result is quoted for is that
full point group rather than the subgroup a *driven* steady state leaves intact — the premise the
first three did not state. The theorem is proved in four Euclidean variables, while leading
rotational anisotropy is a three-dimensional claim and a driven medium singles out its advance
axis; the stabilizer of that axis has order 48 and restricts faithfully onto the full octahedral
group, whose degree-four *spatial* invariant space is **two**-dimensional and contains
`Σᵢ kᵢ⁴`. At the driven group an anisotropic spatial quartic is therefore *permitted*, and what
excludes it is not symmetry but interaction content: the bond set's spatial fourth moment computes
to zero — and does so by cancellation between the axis-bearing and in-hyperplane bonds, not by a
property of either. Any driven-sector term populating that permitted invariant would restore
dimension-six spatial anisotropy. **This is a permission, not a demonstrated term** — no kernel
written down in this programme exhibits it — but it is the premise on which the headline
generality rests, and it is named here rather than left to be found.

**The prior art here is not ours, and the credit comes before the argument.** That the D4/F4 lattice
suppresses rotational-symmetry-breaking cutoff effects relative to the hypercubic lattice is
established lattice field theory. Neuberger proposed F4 lattices for exactly this reason (*Spinless
fields on F(4) lattices*, *Phys. Lett. B* **199**, 536 (1987)); Chow (1999) states the group-level
form, that D4 is exactly isotropic at order `a²` and is the only unexceptional root lattice with the
property, protected by the accidental threefold Dynkin-diagram symmetry; the two-sided sharpness is
established in the lattice-kinetic-theory literature (Chen, Goldhirsch & Orszag, 2008); the
24-cell's spherical 5-design property is classical (Delsarte, Goethals & Seidel, 1977); and the
formulation remains live (Katz & Nográdi, arXiv:2512.10604). **Any claim of novelty for the result
does not survive contact with that literature.** What is claimed here is narrower: the generality of
the proof — one-dimensionality of the degree-four invariant space for *every* analytic
point-group-symmetric kernel at once, via the `W(F4)` invariant degrees, with the triality premise
named — and one transfer, that Lorentz-violation effective field theory already uses point-group
protection at dimension four but appears not to have carried the observation that the argument fails
at dimension six for the hypercubic lattice and holds for D4.

**What none of it reaches** is the rotationally invariant dimension-six residual. It is not a
relative-boost observable, so the one-medium protection does not apply; it is not an anisotropy, so
the point group does not apply; and at dimension six a species-universal coefficient is not
removable by any rescaling, because the induced velocity shift is momentum-dependent. Its
coefficient is set by the substrate's own strain-mode dispersion, an object the engine gates. It is
this programme's sharpest empirical exposure, and §5.3 states it as one.

## 2.6 Three prohibitions from one conservation law

The same `3 × 1/3 = 1` arithmetic that makes the hypercharge bracket of §2.1 vanish also makes the
gauge-trace anomalies of `B − L` vanish across one generation:

> three quarks at `B − L = 1/3` plus one lepton at `B − L = −1` sums to zero per generation, and
> `Tr[T_a T_b · (B − L)] = 0` on the corresponding generators.

That is not a tuning of quark and lepton quantum numbers. It is forced by the colour count and the
per-blade hypercharge signs — the same two facts that produced the neutrality identity.

**The topological carrier, named.** `B` and `L` are not two labels on one winding here. The local
state of this medium is a four-dimensional orientation, and `π₃` of that state class is `ℤ ⊕ ℤ`:
**two independent integer windings**, each a homotopy invariant and therefore each conserved
separately under any smooth deformation. The count is the chiral one — the orientation class
factorizes into two `su(2)` factors and there is exactly one winding integer per factor — and the
family's working basis is a change of basis of that pair, into a subgroup winding (leptons wind
into the diagonal `Spin(3)`) and a coset winding (baryons wind into `Spin(4)/Spin(3)`). Two
features of the count are load-bearing below. It is **blind to the family's undecided `ℤ₂`
clause**, because a double cover is an isomorphism on `π₃`, so it reads the same on both branches
of the LS note in §1.2 and costs nothing there. And the **source** of that protection differs from the incumbent's. The Standard Model keeps
`B − L` exact and gets `B` and `L` separately as accidental symmetries of the renormalizable
Lagrangian — real structural earnings, credited as such in §3.2 — but they are accidents of the
dimension-four truncation, and the higher-dimension operators an effective theory admits break
them. Here they are homotopy invariants, so they survive any smooth deformation of the
configuration whatever operators are present. What is *not* different is the non-perturbative
channel: this family's `ΔB = ΔL = 3` selection rule is the incumbent's own rule. The prohibitions
below rest on the protection's source, not on a stronger conservation law.

Between them, the anomaly arithmetic and the carrier collapse three separate Standard-Model
"extras" into **one** substrate fact, which is why they are stated together here rather than in
three places:

- **No proton decay.** Baryon number is one of those two integer windings. Non-perturbative
  violation respects `ΔB = ΔL = 3`, so a channel taking one baryon to none is forbidden — and the
  selection rule is itself obtained rather than assumed, from the substrate's instanton topology
  together with the index theorem's zero-mode count, at three generations. **The proton is absolutely
  stable in the smooth sector**, at any lifetime — which is the family's one distinctive forward bet
  against grand unification: unification expects decay at *some* level, and this family forbids it
  outright. What "in the smooth sector" carries is the paragraph below.
- **Dirac neutrinos.** With `B − L` exactly conserved, a Majorana mass term is forbidden, because it
  would carry `Δ(B − L) = −2`.
- **No neutrinoless double beta decay.** The same conservation law forbids the signature.

**The condition.** The winding argument rides the defect class — a preferred direction, not an axiom
— and the instanton-plus-index-theorem pair is a registered external import applied at the effective
level, with the *rate* face gated. The conservation law is the family's; the topological carrier is
endorsed; the counting theorem is borrowed and marked as borrowed. One residue inside the carrier
belongs here rather than in a footnote: the coset winding is canonical, the subgroup winding is not.
Reading a *general* configuration in the subgroup/coset basis requires a splitting of the exact
sequence relating the two bases, and while such a splitting always exists it is not canonical and
the family has not named one. Nothing above turns on it — each prohibition is argued at a
configuration whose sector is fixed by its own construction — and the residue closes if the sector
assignment is ever derived rather than assumed.

**And it rides the arrangement, not only the defect class.** Homotopy invariance is a statement about
continuous maps. In a grainy member — and grain discreteness is one of the family's preferred
directions, so that is the endorsed reading — a configuration whose core shrinks toward the grain
spacing leaves the space of admissible maps, and the winding number is simply not defined through the
transition. This is not a hypothetical: the programme's own lattice flows have recorded unwinding
events at under-resolved cores, and its own lattice charge measurements are faithful only as the
core-to-spacing ratio grows, with a measured deficit falling as the inverse square of that ratio. **So
the prohibition is exact in a continuum member and carries a resolution condition in every grainy
one.** The condition is parametrically enormous in the first candidate — a hadronic core against a
Planckian spacing — but that is an estimate and not a computation: converting it into a rate is a
dynamical statement, and the rate face is gated exactly as the non-perturbative channel's is. The
suppression that estimate would give is deliberately not used to keep the prohibition
unconditional, because this programme refused the natural-value estimate where it ran against it, at
the dimension-six coefficient of §5.3. **The family forbids the decay channel; it does not compute the
unwinding rate of the member it endorses.**

**One prohibition of a different kind, so the boundary is visible.** Magnetic monopoles are absent
here **by the source identification, not by algebra**, and the difference matters. The grade-three
slot in the field equation is not empty as a matter of Clifford structure: grade three in this
algebra is four-dimensional, and that slot is exactly how geometric-algebra electromagnetism *with*
monopoles is written. The engine reports the slot's dimension rather than its vanishing. What this
family supplies is that nothing fills it: its only current is the wavefront projection of grade-two
winding to grade one, and a grade-two-to-grade-one projection cannot produce grade-three content. So
the honest statement is that *given* the winding-as-source identification the monopole term does not
arise — and a different source identification would refill the slot. That is the re-attack handle,
and it is stated as one.

## 2.7 The quantum package — a relocation with a gain

One block is family-clean in its consumption and must nevertheless be quoted carefully. The quantum
postulate structure and the Bell sector come out of the axioms plus the package's registered imports,
with no candidate pick: the complex unit as a forced subalgebra rather than a stipulation, the
self-adjointness condition, the Born exponent as a theorem given its named premises, the Dirac
equation, the no-signaling identity, and the Tsirelson bound `2√2` reproduced from the one-sided
rotor half-angle — that last one a **framing identification** in the engine's own tier, because it
rides the composite state space and the singlet, which this paper books as imports rather than as
constructions. Probability is not a primitive of the ontology here: the substrate is
configuration-realist, and the measure over its configurations is what the Born exponent above is a
theorem about — on the same named premises, one of which is the single-outcome mechanism this section
leaves open.

**The complex unit is worth stating precisely, because the two halves of it have different status.**
Impose three conditions on a rotor element acting on the defect background — that it commute with
the advance axis, that it preserve the soliton background, and that it be even-grade — and the
intersection is exactly the two-dimensional commutative subalgebra `{1, B}` with `B² = −1`. That
subalgebra is **forced**, and the quantum complex unit is its consequence rather than its premise;
with no defect present the third condition is empty, the centralizer is four-dimensional, and there
is no unique complex line at all — which is the rotational ambiguity of free space, broken by a
defect. What is **not** forced is the next step: taking the fluctuation field to lie in that
subalgebra is an **ansatz**, and as written it is too strong, since it delivers a one-dimensional
complex state space that the Bell sector's own two-state construction does not use. The subalgebra
result stands; the field restriction is an open construction, and this paper says so at the claim
site rather than at the back.

**The rider is part of the claim.** Family-clean is a *consumption* classification — it says these
results use no candidate pick — and it is not a claim of derivation-completeness. The package buys
its structure with imported, registered mathematics: the tensor-product composition rule for
composite systems, the singlet form, Gleason's theorem among them. The composite state space in
particular is **assumed**, not constructed, with five construction routes recorded as failed. So
this block is a **relocation with a gain, exactly as the signature is**, and it is to be quoted that
way; a referee who reads "quantum mechanics derived from the substrate" has read more than is
written here. What remains genuinely open and is named as open: the single-outcome selection
mechanism. And one debt is owed and cheap to say — the written argument for why the choice of memory
kernel does not disturb quantum mechanics currently rides a candidate pick, so the family keeps the
postulates and, as things stand, loses its own protection argument until that argument is restated
at family level.

---

# §3 — What this costs, measured against what it is competing with

A parsimony claim is worth nothing unless the same knife is used on both sides. What follows is an
audited debt statement at **family level only**: what the family buys, what it owes, and what the
alternatives buy and owe for the same explananda. Nothing is netted, and where the family is behind
it is recorded as behind. The first candidate's own ledger — its counted inputs, its calibration
performance, its wounds — is §5, and the two are not to be merged.

**A note on labels, carried with every quotation of this section.** Lines marked AUDITED were
decomposed item by item. Lines marked SURVEYED were not. Where a count appears below for the
incumbent's structural commitments, it is SURVEYED.

## 3.1 The separator — the answer to "how do you know this structure isn't fabricated"

The sharpest available objection to a programme of this kind is that it has elaborate guardrails
against fabricated *numbers* and none against fabricated *structure* — that relabelling a known
result in new notation and filing it as derived is exactly the failure mode the apparatus cannot
see. That objection is correct as stated, and the answer is a criterion applied to this family's own
list first:

> **A structural fact counts as *obtained* rather than *relabelled* when (i) a named substrate
> feature's deletion breaks it — an exhibited failing counterfactual; (ii) it is independent of the
> framework's free parameters; and (iii) the feature does work it was not selected to do — either
> *structurally*, by carrying a load in a sector it was not introduced for, or *empirically*, by
> having a consequence in a domain not used to fix it which was then independently tested and
> confirmed.**

**Clause (iii) does the work the first two cannot, and the reason it is here is worth stating before
the grading.** A feature chosen in order to produce a result will always break that result when it is
deleted, so clause (i) fires automatically in exactly the case the separator advertises itself
against. That the first two clauses are not vacuous is visible in their own application below — they
strike one entry outright, leave two partial and collapse a pair — but what they cannot do is
separate an obtained fact from a reverse-engineered premise, and clause (iii), the classical demand
for excess content, is what addresses that.

Applied to the family's own claimed list of ten structural facts, the first two clauses **collapse one
pair into a single fact, remove one outright, and leave eight distinct claims** — graded as follows,
and every entry named so the grading can be checked rather than taken:

| Grade on clauses (i) and (ii) | Count | Which |
|---|---|---|
| **Pass both** | **2** | the **charge arc** (§2.1) and the **weak arc** (§2.4) — each with an exhibited failing counterfactual and each independent of the framework's free parameters |
| Pass with a stated weakening | 4 | the **generation count** (§2.3) — generic-given-four-dimensions, real but not substrate-specific · the **Lorentzian signature flip** (§2.2) — half-chosen: the algebra isomorphism is a theorem, the timelike placement is an axiom · the **monopole absence** (§2.6) — conditional on the winding-as-source identification, whose failing world is named in place · the **`B − L` closure** (§2.6) — narrowed, because the incumbent also obtains `B − L` as an accidental symmetry; what survives is the closure of the Dirac-versus-Majorana question the incumbent leaves open |
| Partial or undecomposed | 2 | the **gauge group** — one factor is obtained, not the group, since colour is not a gauge group in this family at all · the **up/down mirror** — the parity relation is contentful, the SD/ASD label is convention, and no counterfactual was exhibited for it |
| Collapsed into another entry | 1 | proton stability and the absence of neutrinoless double beta decay share the `B − L` root — one fact with three faces (§2.6), so no independent credit |
| **Does not belong on the list** | **1** | the **Tsirelson bound** — the engine itself tiers it as a framing identification, because it rides the composite state space §3.3 books as *assumed* |

**Two facts pass the first two clauses.** The charge arc, with
the caveat of §2.1 — the discreteness unconditional, the neutrality identity conditional on the
endorsement it inherits. The weak arc, with the endorsed hosting premise and the right-handed-singlet
datum travelling with it wherever it is quoted — and with the side of the hosting action computed
rather than assumed, carrying its own failing counterfactual: collapse the local state from a full
orientation to a bare direction and no body-frame action exists at all, so the host could not be an
observer-scalar and the arc would fail where it now passes. Everything else is graded, including two entries the
decomposition leaves partial or undecomposed and which are recorded as such rather than counted as
passes; stating the tail as a tail is the point of the exercise, and the decomposition itself is in
the comparative ledger `TWT_COMPARATIVE_LEDGER.md`, shipped with the dossier.

**And the third clause, applied to the same ten, with the harsher half reported first.** On the
**empirical** half — a consequence in a domain not used to fix the premises, which was then
independently tested and confirmed — **the family scores zero of ten.** That is not a new admission.
It is §4.1's sentence, that this programme has no channel of its own in which agreement would count
as evidence, arriving where it belongs; the nucleon charge anchor is the datum the construction
enters — the hydrogen-neutrality bound then *tests* the identity rather than calibrating it (§2.1) —
the absence of fractional charge is the datum matched, and the generation count is the
datum matched. One entry is **pending** rather than failed: the `B − L` closure's excess content is
entirely forward — Dirac neutrinos, no neutrinoless double beta decay, the sterile mass tie — and all
of it is currently null, which is untested-and-consistent rather than corroborated. On the
**structural** half — a load carried in a sector the feature was not introduced for — three entries
pass and they share one root, so they collapse to **two structural passes, sharing that root**: the
charge arc, whose trivector orbit carries four separate loads (the charge unit, the hypercharge sign
opposition, the `ℤ₃` colour count and the `B − L` anomaly arithmetic), none of which it was installed
to carry, and the `B − L` closure, which carries the same root into a second sector's closure.

**The input side of the same worry is measured too, by an instrument this programme already runs, and
the two numbers belong in one sentence.** What clause (iii) is afraid of is a premise introduced only
to make a result work. The comparative ledger prices every banked result's premises on a four-point
scale — free, cheap, costly, or **convoluted**, the last being a premise whose only motivation is the
result it enables, and a convoluted reading is grounds for demotion however correct the mathematics —
and run over the audited corpus that instrument returned **zero convoluted premises**, with both of
its demotion slots empty. It is not an instrument that declines to fire: the same campaign returned
five double-billed findings and one under-billed, four of the six against this programme, and refuted
the author's registered expectation on one line. **So the honest pair is: zero convoluted premises on
the input side; zero empirical excess and two structural passes on the output side.** A programme with
two structural passes, no convoluted premises, zero empirical passes and a named route to a first one
is a coherent position stated honestly. A programme claiming two clean passes on a criterion that
cannot fail is not. The named route is §4.1's: the finite-grain / bounded-amplitude higher-order-interference deviation
law.

**The separator is not an announcement; here is it applied, with both counterfactuals exhibited.**
For the charge arc: delete the trivector factor of three of §2.1 and the neutrality bracket no longer
vanishes — the residue is `2c ≠ 0` in this paper's hypercharge normalization, the one in which
`Y_lep / Y_Q = −3`; in the conventional normalization with `Y_Q = 1/3` the same residue reads
`−2c/3`, the two differing by the overall scale of `Y` and by which orbit is written first. The
number is normalization-dependent and the *point* is not: it is nonzero for **every** value of the
free constant. So the identity is broken by deleting a named substrate feature, and it is broken for
every value of the free normalization rather than for a special one. That is the first two clauses
satisfied by one deletion, and the deletion is runnable. For the weak
arc: delete the right-handed-singlet datum and the diagonal class survives the classification, so the
menu re-opens and the assignment reverts to a choice; delete instead the assumption that the host
lies in the substrate's rotation algebra and there is no menu to close at all. Both deletions change
the answer, and neither touches a fitted parameter — this family has none in either arc.

For contrast, the entry the separator **strikes**: the Tsirelson bound is reproduced exactly here,
and deleting any substrate feature at all leaves it standing, because it follows from the composite
state space that §3.3 books as *assumed*. A correct number that no substrate deletion can break is
not an obtained structural fact, whatever its tier says elsewhere — and the family's own engine
already tiers it as a framing identification. That is the separator doing the work it exists for,
against this family's own list.

That is what "structure without a unifying group" means here, and its price is stated with it: the
incumbent postulates the charge assignments; the grand-unified route *derives* quantization and pays
with a larger group, a breaking sector and a proton decay that has not appeared; **this family
obtains less of the structure than the unified route does, on premises that are named rather than
paid, and it is the only one of the three that obtains any of it without buying a larger group.**

## 3.2 The economy, on two axes that must not be added together

The Standard Model's parameters are continuous dials fitted to data. This family's inputs — at family
level — are structural only, and structural choices have no canonical individuation: re-individuating
moves any structural count below by roughly a factor of two in either direction. **The two kinds are
therefore reported on separate rows and never summed.** A count that mixed them would flatter
whichever side it was built to flatter.

| | **Standard Model** (the target) | **The family** |
|---|---|---|
| **Continuous parameters fitted to data** | **19** (26–28 with neutrinos) | **0** — the family names no number |
| **Structural commitments, same basis** *(SURVEYED for the incumbent)* | **~10** on a fine individuation: the gauge group; the chirality assignment; the fifteen-Weyl representation content; the hypercharge assignments; three generations; colour in the fundamental; one Higgs doublet; the sign of the Higgs mass term; the dimension-four truncation; four-dimensional field theory on a fixed background. Three of these are components of the representation content, so a coarse individuation gives **~6** — and the finer reading is the one that flatters the challenger, which is why the coarse figure is stated here too | **8**: seven axioms and one refusal |
| **Structural facts obtained rather than chosen** *(graded by §3.1)* | **anomaly cancellation**, constraining the hypercharges given the chosen representation content — and, at the same depth, the accidental-symmetry earnings of renormalizability: baryon and lepton number, hence proton stability at the renormalizable level; the absence of tree-level flavour-changing neutral currents; the custodial relation given one Higgs doublet; asymptotic freedom given the gauge choice. **These are real structural earnings and several of them overlap what this family claims on its own side of this row** | of ten claimed: **two pass the first two separator clauses, four weakened, two partial, one collapsed into another, one struck** — and on the third clause, the demand for excess content, **two structural passes and zero empirical** (§3.1) |
| **Earned dimensionful scales** | **1 of 5 scale classes** — the QCD scale, by dimensional transmutation | **0** |
| **Load-bearing items outside the count** | the 19 exclude the structural column and the neutrino sector | the driven-dynamics placeholder and the grain-to-cell transfer, both **high**; and six of the eight preferred directions sit off any parameter ledger |

**Three fences on that table, and they are not decoration.** A bit-inclusive input count may never be
quoted against a rival's continuous-parameter count. The
interpretations compared in §3.3 are **uncounted** in this table, so no rival-facing count comparison
is licensed against them anywhere. And **three different counts of about ten appear near this
table** — the incumbent's structural commitments, its parameters, and this family's claimed
structural facts — and they are three different lists; none is evidence for another.

## 3.3 Five lines, itemized at equal depth

Each line asks the same three questions of every framework: is the debt **named**, is it
**in-principle payable**, and is there a **named and unblocked route**? Effort is recorded inside the
cells, never as the question — person-hours track community size, which tracks incumbency. GRW-class
collapse models and causal sets are in the reference class and are not built out here; any comparison
presented as complete is not.

**1 — The measurement problem and the Born rule.** One phrase — *everyone has a measurement problem*
— hides three different debts. Copenhagen **postulates** single outcomes and the Born rule,
terminally. Bohm gets single outcomes **free**, the particle configuration being the outcome, and
**derives** the Born form from equivariance, on a configuration space he pays for in ontology; what
he owes is the distribution, named and worked for three decades. Everett **denies** single outcomes
and inherits a contested probability programme. This family **owes** the single-outcome mechanism
outright and holds the Born exponent as a **theorem conditional on three coupled premises** —
statistical noncontextuality, the composite state space, and the single-outcome mechanism itself. A
conditional theorem beats a postulate; it does not beat a delivered derivation. **Position: ahead of
Copenhagen, behind Bohm on delivery, a genuine trade against Everett.**

**2 — The composite state space.** Copenhagen postulates it; Bohm and Everett **pay** for it with a
field on high-dimensional configuration space, a bill that is settled and framed on the wall; this
family **assumes** it, with five construction routes recorded as failed and one external theorem —
the complex-geometry condition making complex-linear tensor products of quaternionic modules
possible — as a named handle. Three debts under one symbol: unpayable by design, paid in ontology,
open with a route. **This is the single largest uninvoiced item in the ledger, and it is the named
mechanism by which the comparison could reverse against this family.**

**3 — Preferred structure.** Copenhagen has a movable cut; Bohm has a preferred foliation; Everett has
none. This family carries **a foliation and, in any grainy member, a lattice** — the largest
preferred-structure bill of the four, and the lattice is its genuine excess over Bohm. Against that:
it is the only one of the four that **names** its foliation, identifying it with the cosmic rest
frame, and thereby accepts a **total kill condition no rival in this comparison carries**. The safe
option was available and was declined. The condition is downside-only: it fires only where quantum
mechanics also breaks, so agreement confirms nothing. **An honesty asset with no evidential upside,
and the bill above it stands.**

**4 — Lorentz invariance. This is the line the framework is behind on, and no gain elsewhere is
offered as compensation.** Everett wins it outright: its ontology raises no sub-quantum scale at
which a Lorentz-violating coefficient could arise. **One theorem and one conditional counterweight
exist here, and they are not the same kind of thing.** A lattice member's point group pushes
rotational anisotropy to dimension eight — that is a representation-theoretic theorem, valid for any
analytic point-group-symmetric kernel, and it is the harder of the two — though it too is
conditional, and §2.5 names its four premises, including the one that matters most for a *driven*
substrate: that the operative symmetry is the full point group and not the subgroup the drive
leaves intact, at which an anisotropic spatial quartic is permitted rather than forbidden. The one-medium light cone of
§2.5 would make dimension-four relative-boost violation structurally zero rather than tuned, **but
it rides an unexhibited universality claim about substrate self-energies, so it is a conditional
defusal and is counted as one.** **Neither reaches the isotropic dimension-six residual, whose
natural coefficient is excluded by existing limits by three to nine orders.** The programme asserts no value there and cannot
presently compute one, so what the data has fixed is a **ceiling its unbuilt dynamics must deliver
beneath** — the harder position, since the rivals have nothing here a measurement could address, and
not a refutation. **The exposure belongs to the first candidate, not to the family — and the family
is clean here only because it says no number, which is exactly the credit this ledger refuses the
rivals for the identical purchase.**

**5 — The floor, and what a substrate costs.** Every framework's debts bottom out somewhere. For the
three interpretations the floor is the quantum formalism plus the Standard Model's parameters, brute
and unexplained; they attempt nothing below it, so they accrue no substrate-transfer debt **and
deliver no substrate-scale explanation** — abstention, which is neither discharge nor debt. This
family's floor is the substrate itself, and it therefore owes a transfer from that floor to tested
physics that **no computation in the corpus performs**. It owes it in a currency the world has partly
collected in: two exposures already measured against, both belonging to the first candidate. The
incumbent is not spotless on this axis either — its floor carries an unprotected electroweak scale
and, once gravity enters, a vacuum energy off by some hundred and twenty orders, and the same
naturalness criterion this family is held to is violated in both places. **That constrains the
comparative sentence and relieves nothing:** the exposure here is against **data**, not against a
rival, and no rival's silence weakens it by one order.

## 3.4 Whose company the family keeps

The family is not alone in its central premise. The Stueckelberg–Horwitz–Piron tradition has held an
evolution parameter distinct from observed time for eighty years, with a founding paper pair, a
textbook, a review literature, and a conference series that has met biennially for twenty-eight
years. Read against it, this family decomposes as: **their two-time kinematics, plus substrate
realism, plus the Euclidean signature with the wavefront lock, plus matter-as-defect.** The first
block has an eighty-year formalization behind it; of the remaining three, two are held outright and
in print elsewhere — the second kinship below — so what is this programme's own is the conjunction
rather than the blocks.

Four corrections bind every use of that kinship. Their meta-time frequency goes as mass *squared*,
so the correspondence with mass-as-frequency holds only up to a quadratic map — say so at every use
or drop the twin language. They do not escape the frame cost where it matters: in flat space their
parameter is a genuine scalar with no preferred frame, but their own gravitational extension elects
the parameter as the preferred time direction and expects no general diffeomorphism invariance, so
their gravity sector lands inside the same trilemma this one does. Their mass-stability result is a
precedent for the *shape* of this family's debt, not for its payment — two proposals by two authors,
neither claimed as a solution, with a non-unique equilibrium. And their fifth-direction constant is a
late addition, free and unmeasured, so both sides of the resemblance to this family's meta-time speed
are unpinned.

**A second kinship, and it is closer on two of the four blocks.** Volovik's
quantum-vacuum-as-medium programme holds the substrate-realist premise outright and in print — the
vacuum as a real structured medium whose excitations are the particles — and obtains from a worked
microscopic model a list this family recognizes: emergent Lorentz invariance in a low-energy corner,
chiral fermions, gauge fields as collective modes, topological defects as analogues of cosmic
strings and monopoles, and an inner
observer who cannot see the substrate's own geometry (*The Universe in a Helium Droplet*, Oxford,
2003). Two of those parallels are close enough to state individually. His inner observer is made of
the liquid's low-energy quasiparticles, so its rods and clocks are set by the effective metric those
quasiparticles themselves define; such an observer cannot measure the motion of the superfluid
vacuum, cannot register its anisotropy, and reads the ground state as empty space — which is the same
shape of argument as §2.2's remark that an observer's spatial axes here are bivectors containing the
advance direction. He scopes that blindness explicitly to the low-energy corner and to purely local
measurement, and makes it observer-relative rather than absolute: what the inner observer cannot
separate, an external observer separates without difficulty. And in the A-phase the Fermi point is
doubly degenerate through the *ordinary* nuclear spin of the atom; perturbing that `ℤ₂` symmetry
splits it into two elementary Fermi points whose independent motion is carried by a collective
variable coupling to that spin as a **local and dynamical `SU(2)` gauge field** — he derives its
Yang–Mills action by integrating out the fermions and finds its coupling equal to the emergent
electromagnetic one, with the atomic spin in the role of weak isospin. **Two limits travel with that
citation and neither is optional.** That emergent `SU(2)` governs the Fermi-point degeneracy and
**not** the quasiparticles' chirality, which is carried by a different index, so he nowhere claims it
reproduces the Standard Model's left-handed factor; and he states plainly that the A-phase is not a
perfect system for a complete simulation of relativistic quantum field theory — its gauge invariance
approximate, its analogue `W` massive beyond the model it is derived in, its charge screening rather
than antiscreening. What the correspondence is, on his own account, is a shared universality class
fixed by momentum-space topology, not an exact mapping.

**So substrate realism is not this programme's own risk. Matter-as-defect remains this programme's
own:** his matter analogue is the fermionic quasiparticle, with defects playing the cosmic-string
and monopole roles, whereas here the defect *is* the matter. What is also
this programme's own is the conjunction — that the medium's motion *is* the second time's advance,
which a defect's phase must match, welding the carrier to the drive. Two corrections bind the kinship
in the opposite direction, and both are ours to state. His protection mechanism is momentum-space
topology at a Fermi point, and this family's first candidate has measured that route **closed on its
own substrate**: the banked grain dynamics sit in the real symmetry class, with no node at finite
momentum and the only available invariant valued in `ℤ₂` rather than `ℤ`. And his own accounting has
the Standard Model's node marginal, the two halves cancelling, so that mechanism protects nothing at
the target even where it is formulable. The kinship is on the premise; the mechanisms diverge, and
this family's runs through real-space topology throughout.

**A third and smaller kinship, where the news runs the other way.** A separate small literature
reformulates special relativity on a four-dimensional Euclidean space with proper time as the fourth
axis and Lorentz transformations read as `SO(4)` rotations. It is closer to §2.2's *starting point*
than the two-time tradition is, and it is a different kind of thing: those are reparametrizations of
an existing theory, with no medium and no dynamics, and this family should not be filed with them.
One structural remark is worth making, because it is checkable in one line and it distinguishes the
constructions rather than the ambitions. **A boost realized as a rotation of a Euclidean plane is
circular: its parameters add, but the induced velocity composes with the wrong sign and is unbounded
and periodic, so there is no invariant speed.** In the construction of §2.2 the observer's boost
generator is not a plane of the substrate at all: the lock puts the observer's time on the advance
axis, so `γ⁰γʲ = e_j` is a substrate **vector** with square `+1`, the exponential is hyperbolic,
rapidities add, and `v = tanh w` reproduces Einstein velocity addition identically — collinearly
exact, with the Wigner rotation appearing for non-collinear composition exactly as relativity
requires. **What that shows is where the two constructions part, not that either is more
ambitious**; whether any particular paper in that literature carries the circular reading is a
question about that literature, and this paper does not answer it.

**Precedent, not validation.** Kinship moves the family from isolated to a member of a small,
respectable tradition. It is not evidence that the family is true.

## 3.5 The honest outcome

> **On the debt-structure criterion — are the debts named, in-principle payable, and being worked —
> this family's position is `PARTIALLY SUPPORTED, NOT CONFIRMED`.** It is best-placed on two lines,
> mixed on two, **behind on the empirical one**, and its largest single item is still uninvoiced.

Its debts are enumerated rather than absorbed into silence, and **one of them is discharged by
computation**: the weak sector's assignment is not an input and not a preference — given the endorsed
hosting premise and one datum read from experiment, it is forced (§2.4). **That is one discharge, on
the cheapest of the debts, and it does not generalize:** the method closes menus that are finite and
algebraic, and the largest item above is a space of constructions, which no such enumeration reaches.

**The same verdict, in plainer words, because the accounting above is easy to read as more than it
is.** The **unconditional** residue of §2 is a set of correct facts about a sixteen-dimensional real
Clifford algebra together with an identification dictionary assembled with the Standard Model in
view — of which two entries survive a separator this paper applies to its own list first, each with a
deletion that breaks it and neither touching a fitted parameter, one entry of which that separator
**strikes**, and on whose demand for excess content the empirical score is zero (§3.1). The
**conditional** residue is a reconstruction of quantum numbers — labels, slots and selection rules —
not of interactions: there is no gauge boson anywhere in this family. The **empirical** posture is
four null forward bets, two wounds belonging to the first candidate, one live internal rework, and
one family-level structural exposure in the incumbent's best-tested sector. And the **entire**
magnitude sector is mortgaged to one object nobody has built.

Nothing in that sentence rivals the incumbent anywhere the incumbent is testable, and this paper does
not claim otherwise. What the programme has that its reference class rarely has is an audit trail
that makes the sentence above reachable in an afternoon by someone who did not write it — which is a
real achievement and is not yet physics progress. §6.3's confessed failure mode is, on the evidence
of this paper, **partially realized**.

Two things this section does not do. It does not decide whether the theory is true: parsimony is
evidential only between empirically equivalent theories, and this family is not empirically
equivalent to the incumbent — it is behind it in two named places. And it does not present a finished
picture. Every column here for the rivals is a photograph of a finished ontology; this one is an
architect's rendering, conditional on a single unbuilt object delivering the magnitudes the family
owes. **No entry above is evidence that it will be built.** And a third: it does not claim that any
structural result above has been *confirmed*. Every channel in which the family's §2 results are
currently exposed is one in which a detection would break them and a null confirms nothing (§4.1).
Parsimony is what this section measures; corroboration is what the programme does not yet have a
channel for.

---

# §4 — The falsification surface

## 4.1 The family's kill condition

**If the ordering that Bell-correlation selections follow is measured and found to be a foliation
measurably distinct from the cosmic rest frame, the family is finished** — not one version of it, all
of it. That is what it means for B-6 to sit in the definition rather than in a branch.

Two riders belong with it and neither is optional.

**The asymmetry.** The measurement that would fire this is one that standard quantum mechanics *also*
forbids. In this channel, therefore, agreement confirms nothing — it is a consistency check, and the
family inherits quantum mechanics' verdict either way — while disagreement kills. Maximum downside,
no matching upside; that is the price of naming the frame, and it was paid deliberately.

**The reference class.** This is a total kill condition **no rival in the comparison of §3.3
carries** — Copenhagen, Bohm, Everett, the Standard Model read as an effective theory. It is not a
claim to be the most falsifiable theory in physics, and it is not a claim that no other programme
anywhere accepts a comparable exposure. It is the strongest option that was **available at family
level**, taken rather than declined.

Of the sixteen falsifier rows the corpus carries, fourteen stand at family level and two are
instance-level — one whose kill number rides a candidate's fitted hadronic calibration, one riding a
candidate's identification of the observed light speed with the meta-time advance rate.
**Because this kill channel fires only where quantum mechanics also breaks, the family has no independent empirical
exposure *in it*** — and §4.2's prohibitions, which do have independent experimental routes, each
reach a derivation or a preferred direction rather than an axiom, so a positive detection there
forces the next candidate rather than ending the family. Said at its truest: **this is a research
programme with one inherited total kill condition, a real set of family-level prohibitions, and no
channel of its own in which agreement would count as evidence.**

**And the asymmetry is not local to this channel.** Every row of §4.2 is a *forbiddance*: the family
says what cannot be observed, and each row is currently null. A holding forbiddance is consistency,
not confirmation — so the reading above applies to the structural results of §2 and not only to the
kill condition. The family's structural content is, at present, **breakable but not corroborable**: a
positive detection anywhere in §4.2 reaches a derivation or a preferred direction, and no null
anywhere in §4.2 is evidence that any of them is right. That is a statement about the *channels* and
not about the *content* — §3.1's separator exists precisely to test whether a retrodiction was
obtained or relabelled, and it is applied to this family's own list first, which is why its empirical
half reads zero — but the channel fact is the one that decides what the programme can *earn*, and it
is why the finite-grain / bounded-amplitude interference law below is not one docket item among many.

**The one identified route to building the last of those** is the finite-grain / bounded-amplitude,
higher-order-interference channel: the Born rule's deviation law — sourced either by the medium's
grain (vanishing with it) or by the medium's amplitude ceiling (present at fixed grain) — would be
a structure-derived number the incumbent inputs as exactly zero, and the triple-slit programme
already supplies a bound. The two sources carry different scaling laws, and which one a positive
result would implicate is part of what the channel's protocol must separate. That deviation law is
not derived here. It is named as a route family, not as a result.

## 4.2 What the family forbids

These are the family-level prohibitions with independent experimental routes. Each follows from the
axioms, or from the axioms plus one stated preferred direction, so a positive detection on any of
them reaches every candidate at once — and none of them is a total kill, because each reaches a
derivation rather than an axiom.

| What would be observed | Channel | Current bound | What it reaches |
|---|---|---|---|
| **Proton decay**, at any lifetime | Super-Kamiokande, Hyper-K, DUNE | `τ/B > 2.4 × 10³⁴` yr, 90% CL | the topological protection of baryon number (§2.6) — **the family's one distinctive forward bet**: grand unification expects decay at *some* level and this family forbids it outright — and, in any grainy member, the resolution condition under which the winding is defined at all, a condition this family states and does not compute |
| **Neutrinoless double beta decay** | KamLAND-Zen, LEGEND, nEXO, CUPID | `T₁⁄₂(¹³⁶Xe) > 3.8 × 10²⁶` yr, 90% CL | exact `B − L` conservation, and with it the Dirac neutrino character that conservation forces. What does *not* die with it: anomaly cancellation is a trace identity on the charge assignment, untouched by a broken conservation law |
| **A sterile neutrino at any mass far above the active scale** | KATRIN's kink search, extended into the keV range by the TRISTAN detector upgrade | none observed | the Dirac-partner mass tie `m_sterile = m_active ≲ 0.12 eV` — the same `B − L` root as the row above, probed through the right-handed partner's mass rather than through `0νββ`; the tie's *number* is value-gated on the candidate's neutrino-mass machinery, so what a detection reaches is the Dirac character itself |
| **A fourth fermion generation** | LHC; neutrino-oscillation precision | none observed | the dimension count of §2.3, together with its identification and associativity premise |
| **A magnetic monopole** | direct searches | none observed | the winding-as-source identification of §2.6 — not a pure algebraic forbiddance, and the slot exists |
| **Fractional charge outside `{±1/3, ±2/3, ±1}`** | direct searches | none observed | the trivector charge spectrum of §2.1; the spectrum does not ride any arrangement |
| **Tree-level flavour-changing neutral currents** | precision flavour physics | tight upper bounds | the weak host of §2.4 — either its structural premise or its empirical leg |
| **A non-zero proton–electron charge sum** | neutrality-of-matter and bulk-matter charge tests | `\|Q_p + Q_e\|/e ≲ 10⁻²¹` | the four premises of §2.1; the family reverts to an empirical charge anchor |
| **A gravitational-wave / photon speed difference** beyond `10⁻¹⁵` | multimessenger astronomy | `\|c_GW/c − 1\| ≲ 10⁻¹⁵` | one substrate, one light cone. The claim is family-*eligible* — it should follow from S1a with S4 — but the re-grounding is **owed, not performed** (§4.4), and it does **not** rest on §2.5's matter-species argument, which covers the matter sector only and not the gravitational mode. A detection here would therefore reach an expectation this paper has not derived, which is a weaker reach than the other rows in this table and is stated as one |

**Two honest readings of that table, and they cut in opposite directions.** Several of these rows
would falsify the Standard Model too, because they test predictions the two share — the charge ladder
and tree-level flavour-changing currents among them — so they are not discriminators. The genuinely
discriminating rows are the smaller set where this family forbids what the incumbent permits: no
proton decay at any level, no Majorana neutrino and hence no neutrinoless double beta decay, no
fourth generation, no monopole. Those four are where a measurement could separate the two, and all
four are currently null. The sterile-neutrino row is not a fifth: it and the `0νββ` row are two
experiments on one underlying derivation, the `B − L` closure of §2.6, reached through different
mechanisms — which is the same non-independence §3.1's grading books as a collapse.

## 4.3 Knowability — the classification every open question carries

Not every open question in this programme is a question that effort can close, and pretending
otherwise is how a research programme spends years distinguishing descriptions rather than theories.
Every open item therefore carries one of three tags.

- **PINNABLE** — some inside-frame observable can decide it. Worth expanding on; these are the
  docket.
- **UNPINNABLE** — in-principle inaccessible from inside the lock, by the theory's own structure.
  These are **family freedom**: recorded, never expanded on. Candidates differing only in unpinnable
  choices are **one member with many descriptions**, and effort spent separating them buys nothing.
  The orientation convention that names the two chiral factors (§2.4) is the worked example: nothing
  in the corpus pins the substrate's orientation, so "SD" and "ASD" are one assignment with two
  names, and the family says so instead of choosing.
- **UNKNOWN-KNOWABILITY** — tagging it is itself the first task.

This is why the family's deliverable is **a list of surviving candidates** — self-coherent,
empirically plausible members — rather than one maximally pinned version. A second candidate is a new
table beside the first one's, not a rewrite of this paper.

## 4.4 What the family does not claim, and what a candidate must deliver

**No scales.** The family has **zero earned dimensionful scales**. Run the seven axioms and the
refusal and every one of them is a sign, an integer or count, a relation, or an ontological kind. Not
one of them is a length, a time, an energy or a rate. A scale-free axiom set cannot output a
dimensionful constant, so **no family-level derivation of a dimensionful coupling exists, and the
obstruction is in the axioms rather than in the effort spent** — within the charter as it stands; a
member adding a Core-level scale axiom would be defining a different family, since the charter's own
rule is that adding or dropping an axiom makes a different theory.

That is the same fact as §2's shape, read from the other side. The family is good at exactly the class
of question that has no units: charge quantization works because winding is an **integer**; the
Weinberg ratio works because it is a **ratio** — one riding §2.4's weak assignment, and a
normalization identity rather than a prediction of the measured value (§5.3); the kinematic bridge
works because a signature is a **sign pattern**; the generation count works because it is a
**dimension**. Gravity's headline number
has units, and that is the structural reason it is not here.

**No gravity results today.** Every gravity result in the corpus rides a candidate pick. The
*structural, dimensionless* facts — one medium so one light cone, the equivalence principle, the
Newtonian limit with the right sign, compatibility with general relativity — are family-**eligible**
and are owed as a re-grounding on the axioms rather than inherited. The *coefficient* is
family-**ineligible** by the scale argument above. That distinction is a work item with a named
deliverable, not a concession, and this paper does not claim the re-grounding has been done.

**No magnitudes.** Couplings, running, absolute masses and decoherence rates all wait on the one
unbuilt object: the driven-dissipative substrate dynamics. **The family owns the kernel programme; it
owns no kernel.**

**One exposure, and it is the family's rather than a candidate's.** Colour is not a gauge group in
this family at all, and that statement reaches every member. It buys something real — the charge
spectrum of §2.1 and the confinement reading that comes with it — and it owes something the
programme has not delivered: **the short-distance response**. The debt is owed to measurements, and
it is stated against them. Deep-inelastic scattering resolves pointlike, fractionally charged
constituents inside the nucleon; the structure functions exhibit Bjorken scaling, and violate it
logarithmically, in the way a pointlike-constituent description requires; jet production and its
angular distributions are measured phenomena of the same class. Those are among the best-measured
structural facts in physics, and every one of them is dimensionless — so the scale argument above
gives this exposure no shelter whatever. A defect picture must reproduce that behaviour as the
short-distance limit of its own structure, and this one has not. The programme's own engine ranks it
as the **make-or-break empirical falsifier** and is wired to raise rather than return there. **It is
the family's sharpest structural exposure, and it is stated here at that rank.**

Two fences belong with it. First, the exposure is against the data and not against a rival's
bookkeeping: the incumbent's own strong sector is priced, not assumed debt-free. §3.2 credits it with
the one earned dimensionful scale in the comparison — the strong scale, by dimensional transmutation
— and the comparative ledger prices the rest of the sector item by item, including the asymmetry that
its lattice machinery works precisely because a lattice there is a **regulator** whose artifacts are
removed in a continuum limit, which is the opposite of the ontological status a grain has in a grainy
member of this family. That asymmetry is booked against this family, not for it, and nothing on the
incumbent's side of the ledger relieves the exposure stated here. Second, the family's own picture
supplies a stance here and not a discharge: a defect's spatial extent is configuration-dependent, so
pointlike scattering off a lepton is not by itself an embarrassment for a defect ontology — but the
nucleon's internal short-distance response is a different object, and nothing in §2 reaches it.

**The field-reclamation debt.** The refusal demotes the field to instance-level description, which
creates a duty the demotion does not discharge. Fields won historically by doing work a medium could
not be shown to do: retardation, radiation reaction, local conservation of energy and momentum in
transit, and gauge structure. Every item on that list is now work the *medium* must be shown to do
instead. Naming the list item by item and tracking which entries have actually been reclaimed is a
standing duty of this section — finite and concrete. If gauge structure proves to be on the
un-reclaimed list, that is family-relevant knowledge, not a candidate's detail.

**So what must a candidate deliver?** Four things, and the first candidate delivers the first three.
(i) A grain structure, with the local-state axiom re-witnessed on it rather than inherited. (ii)
Numbers — a member that declines every calibration does not thereby carry a smaller parameter count;
it carries no numbers at all, which is a different thing and a worse one. (iii) The picks that buy
those numbers, each recorded with the menu it came from and what un-picks it, so that a branch point
is visible as a branch point rather than as a result. (iv) The kernel, or an explicit inheritance of
the gate. Nobody has delivered (iv).

---

# §5 — The first candidate

## 5.1 What V3 is, and what it pins

V3 is the family's first complete leaf, and what it proves is an existence result and nothing more:
**a member of this family can be built all the way down to numbers.** It can be dismantled entirely
without a line of §1 changing.

It pays for that with **eleven pinned choices, one of them carrying a recorded sub-choice — so twelve
rows below**. That individuation is stated here once, and it is the one this paper counts by
throughout. Compressed:

| # | The pick | The menu it came from |
|---|---|---|
| 1 | Substrate arrangement = a **regular D4 lattice**, at the back-fit (Planckian) size | regular lattices / irregular-discrete arrangements / a continuum medium with a cell scale |
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
| 11 | Fermionic quantization = the **Finkelstein–Rubinstein** scheme | fermionic-quantization schemes for solitons |

The full table — each node with the named result that required it, what rides it, and its complete
revert clause — is the programme's family tree `TWT_FAMILY_TREE.md`, shipped with the dossier and
authoritative where the two differ; the dossier's own §A.6.4 carries the same table in prose.

## 5.2 What the numbers are worth

**The parameter ledger, with every cell's condition.**

| | **Standard Model** | **This candidate** |
|---|---|---|
| Continuous parameters fitted to data | **19** (26–28 with neutrinos) | **4** — the cell mass scale, the chirality ratio, the measured Newton constant, and one hadron-sector stabilizer counted **provisionally** |
| Of the 19, pinned at their measured values | — (they are its inputs) | **0 unconditional; 1 conditional** — a candidate reading of the Gatto–Sartori–Tonin mass-ratio relation (1968), which is not this programme's — **and 2 more only if a route this programme itself records as currently refuted is repaired.** *This candidate does not reproduce the nineteen from four.* The four buy a different and smaller set of outputs, and **this row is not separable from the one above it** |
| Exact values read as one bit | — | the Koide amplitude; the right-handed fermions' weak-singlet character |
| Counted structural premises | not counted, by convention | the soliton-mass identification |
| Structural commitments | ~10 fine / ~6 coarse (§3.2) | the family's 8, **plus 8 preferred directions, plus the eleven picks of §5.1 — the largest structural inventory in the comparison** |
| Earned dimensionful scales | 1 of 5 scale classes | **0** — one scale is a back-fit of measured gravity, the other a fit, and the ratio between them is neither derived nor protected |

The provisional entry is the honest one to read twice. The hadron-sector stabilizer is counted as the
**hadron-sector determination of an object** a substrate relation predicts from the
lepton-calibrated chirality ratio, the two agreeing at about 1.1–1.5%. That agreement is a **hedged**
cross-check, not a blind one: the baseline scheme was itself chosen partly on this agreement, the
substrate relation carries no scheme label, and the two legs are readings of different functionals
rather than two measurements of one constant. Both retirement conditions are on the record: if the two
legs converge, the stabilizer retires from the ledger and the count drops to three plus the measured
constant; if they split, the bridge relating them dies and the convergence claim with it.

**Calibration performance, at earned strength.**

- **The charged-lepton triple.** Fitting three amplitudes to three measured masses is a
  one-parameter fit in the generation phase; it lands with under 0.01% residual. That is this
  candidate's tightest empirical fit, and it is a **fit** — the forward derivation was attempted and
  refuted at the bridge, so the structural content here is the Koide form and its geometric
  characterization, not the magnitudes.
- **The cross-sector chirality ratio.** The lepton sector calibrates the substrate chirality ratio at
  ≈ 0.787 through the generation phase. The baryon sector reads ≈ 0.778 from the Skyrme stabilizer,
  independently. **The two converge to about 1.1% with nothing fitted between them**, and that
  convergence is the strongest cross-sector consistency signal this candidate banks. Stated exactly, what
  each leg measures is a **ratio of totals** — the parity-odd bond amplitude over the parity-even one
  — and the two legs' parity-even totals belong to *different* functionals, the generation amplitude
  and the helix pitch, which are the same substrate number only if the symmetric-traceless bond
  admixture vanishes. So the agreement is evidence that two different readings of the chirality
  cohere; it is not a second reading of one pinned parameter, and it is not an independent
  over-determination. Read that way the 1.1% becomes a sharper object than a near-miss: on a reading
  of the generation phase as a rational arc ratio — which this candidate holds as a candidate and not
  as a result — the lepton leg fixes the ratio exactly, and the baryon leg then demands a Skyrme
  stabilizer of 5.392 against the literature's 5.45. That residual is a statement about one constant
  rather than a scatter between two fits, and as a test it is **not yet discriminating**: the
  historical stabilizer is itself a fit whose spread across determinations exceeds the deviation, so
  the test would bite only against a determination at or below about one percent. The chain also has
  one acknowledged geometric coincidence at the relating link, and the candidate says all of this at
  the claim site rather than in a footnote.
- **The nucleon band.** The static soliton mass lands about 8% below the measured nucleon mass;
  adding the collective-rotation term with both coefficients from the *same* exact boundary-value
  profile gives 936.4 MeV for the nucleon (−0.3%), 1229.8 MeV for the Δ (−0.2%), and a splitting of
  293.4 MeV (+0.1%). **The honesty note is inseparable from the numbers: the two couplings were
  historically fitted to those two masses, so this is a pipeline consistency at no new parameter, not
  a new prediction.** Said at the weight the display deserves, rather than at the weight three
  agreeing rows suggest: **this sector inherits the semiclassical Skyrme model's performance and adds
  nothing to it.** The rows are here because a pipeline that failed to reproduce them would be
  refuted by them, not because they are earnings of this candidate.
- **A recorded candidate convergence, not banked as a result.** The lepton-sector scale and the
  nucleon's per-rotor share agree to 0.28% between two measured quantities with no parameter between
  them. The naive derivation route for it is blocked, the floor reading of the same object does not
  converge, and the look-elsewhere caveat is carried. It is a recorded row, not a win.

**What this candidate does not derive**, so the ledger is not read as more than it is: any coupling
magnitude, individual quark masses (the programme abstains from them by rule — only hadrons and
leptons have masses here), the Higgs vacuum expectation value and mass, the CKM hierarchy, the PMNS
matrix, and neutrino masses. All are downstream of the unbuilt kernel.

## 5.3 The two wounds

Both belong to this candidate. Both are already measured against. The family's own sharpest
structural exposure is not here but in §4.4 — the short-distance response of a colour sector that is
not a gauge group — and it outranks both of these; it is not in this section because it is not this
candidate's.

**The dimension-six Lorentz-violation ceiling.** The rotationally invariant dimension-six coefficient
escapes both protections of §2.5. Its coefficient is gated on the unbuilt dynamics, so the programme
asserts no value for it; what existing cosmic-ray and gamma-ray limits exclude is its **natural**
value at this candidate's own lattice scale, by three to nine orders of magnitude, and those limits
bind every future completion — natural, not naive: order one is what a driven-dissipative kernel at a
Planckian grain generically delivers, so the three to nine orders of suppression are a **mechanism
the programme owes**, not a correction it expects. **If the substrate dynamics deliver a coefficient of order one, this
candidate is dead — not evolved.** And "this candidate" is exact rather than a hedge: what dies is
killed at three pinned choices in series — a *regular* arrangement, its *back-fit* size, and *one*
induced-gravity chain to denominate that size in Planck units at all. A member proposed at the
irregular-discrete branch inherits a different constraint rather than a lighter one: no finite-valency
graph can be associated to a sprinkling consistently with Lorentz invariance, so such a member must
say which of discreteness, Lorentz invariance and finite valency it gives up.

**The electroweak crossing scale.** `sin²θ_W = 3/8` is a **normalization identity** at the scale where
the two electroweak stiffnesses coincide — not a prediction of the measured value, and the programme
says so about its own best-known number. The crossing scale itself is not derived at all, and this
candidate's one computable reading of it lands 0.154–0.158 against a measured 0.2312: a 33% miss of a
five-digit number, with the four standard escape routes computed and closed — descent and closures
alike inside an imported elementary-field renormalization-group frame that this candidate's own
emergent / composite gauge sector does not itself license, and if that premise fails the reading is
not refuted but gated. What the miss indicts is
this candidate's arrangement and its calibrations.

**A third exposure, live and internal.** One of this candidate's own picks is under rework, and the
result is not yet in. The bond truncation keeps two of the symmetry-allowed constants; the discarded
directions were shown to be a six-parameter family the corpus had never enumerated, and while the
survivor of the Lorentz cut is quadratically inert and exactly zero on both computed vacuum branches,
the **second chirality dial is a leading-order actor**. It can cancel the canting near a ratio of
about one half — a cancellation line that exists independently of normalization, though its location
does not — and on that line the chiral-symmetry-breaking spine goes away. It also moves the vacuum's
preferred direction, and the survivor's exact vanishing is a property of that direction being
high-symmetry, so the two findings travel together. **The numerical spine is therefore live — and
what the calibration measures is in any case a ratio of totals, a parity-odd bond amplitude over a
parity-even one, so the ratio is not to be quoted as a pinned single-parameter measurement of the two
constants separately, then or now.** The family's structural results of §2 are untouched by it.

## 5.4 The sentence this section exists to make unmissable

**The Core is not vindicated by carrying neither wound.** It carries neither because it makes no
numerical claim at either place, and a family that has not yet said a number cannot be wrong about
one. The wounds are the price of being the only member that says numbers at all, and the
family-and-candidate architecture is a bookkeeping fact, not a defence.

Said plainly, and this is the state of the programme rather than a rhetorical flourish: **the family
does not yet have a candidate it would call very good. The first one is published in full** — its
picks, its calibrations, its mass and mixing material, its wounds at full technical depth, its
result index and its engine map — in the instance dossier `TWT_foundational_paper.md` and its
companion, at the repository. A reader who wants to attack this programme should attack there, and
§5.3 says where.

---

# §6 — Method

## 6.1 How a claim gets in

No load-bearing claim is banked on the developer's say-so. Each is attacked by an independent
reviewer in a fresh context, briefed to argue against the submitted conclusion; verified on the
substrate engine where applicable; and graduated only when developer and reviewer agree on its tier
and its scope. Two further roles run beside the reviewer and are deliberately given different
information: a referent checker, starved of the derivation, which asks whether a claim is *about*
what it says it is about — the class of error where the mathematics is entirely correct and the
result is still wrong; and a coherence keeper, saturated with the whole admitted result set, which
asks whether the corpus now asserts one consistent thing. The keeper adjudicates symmetrically:
dismantling an old banked result is a legitimate and expected outcome, and recency is not evidence.

Three mechanisms do the work the roles cannot. Every algebraic claim has an **engine primitive with a
check**, and quantities the programme cannot compute are wired to **raise** rather than return, so an
unearned number cannot be used by accident. Every **new check ships with its failure demonstration** —
the check is run against a deliberately broken tree and shown to fail for the named reason, because a
check banked without a demonstrated failure mode is an assertion about a check. And every **external
theorem is registered** with its premises, the level it is applied at, its status on the ontology and
the handle that would retire it, so that a wrong import can be excised precisely: strike the row,
fire the listed revert clauses, and the dependent results fall back to their pre-import tiers rather
than collapsing ambiguously.

## 6.2 How a claim gets out

Every dead end is recorded as **tried X → failed because Y → would change if Z**, never as an
impossibility; the negatives ledger `TWT_NEGATIVES_LEDGER.md`, shipped with the dossier, carries
sixty-plus of them, including
closed routes through this programme's own favoured constructions. The mirror rule binds the other
direction: every necessity claim — "the only route", "forced", "no alternative" — carries its
**conditioning class in the same sentence**, exactly as every impossibility carries its
would-change-if. A bare necessity claim is the same failure as a bare impossibility, and this
programme has paid for both.

Every load-bearing choice enters a **family tree** in the same pass it is made, with the menu it came
from, the named result that required it, and what un-picks it — which is what makes §5.1's table a
table of branch points rather than a table of conclusions. Every ruling that governs the corpus
carries its dependents and its **revert list**, so a reversal is executable rather than editorial.

## 6.3 The failure mode this method has, stated by us

The protocol's known failure mode is **apparatus that carries the texture of rigour while
load-bearing calculations remain undone** — registries, tier systems and revert clauses produced
indefinitely without the hard object ever being computed. The tier system, the executable suite and
the import registry exist to counter it, imperfectly, and the separator of §3.1 exists because the
apparatus does not by itself detect *fabricated structure* the way it detects fabricated numbers.
This paper is developed with AI assistance under that protocol, which is why the guard is stated here
and applied to this programme's own list first.

The apparatus itself is published — the rules, the roles with their deliberately different
information diets, the manuals, the gates and their generators — at
**https://github.com/yaerhf/research-ratchet**, so that a reader can audit not only the results but
the process that admitted them. The measured incidents the design rests on, and the honest caveat
that a ratchet can be emptied, are in its own documentation.

---

## Closing

This paper states a family, what it derives, what that costs against the alternatives, what would
kill it, and where its first candidate is wounded. The strongest thing in it is a discrete charge
spectrum obtained from topology without a unifying group, together with a neutrality identity that
holds for every value of the normalization constant — earned, conditioned, and checkable in one line.
The weakest is that every magnitude in the programme waits on one object nobody has built.

We would rather be shown wrong on a specific claim than credited on a general one, and the place to
start is §5.3.
