# VERDICT — REFEREE B: APPLICABILITY OF GOLTERMAN–SHAMIR arXiv:2505.20436 TO A BOSONIC-SUBSTRATE / SOLITONIC-MATTER FRAMEWORK

**Role:** Adversarial referee B, prosecutorial on APPLICABILITY. Joint brief = category error / hidden referential.
**Commission (human coordinator, verbatim):** *"search for an initial category error or a hidden assumption about an SM philosophical referential. It might not apply."*
**Date:** 2026-08-24
**Diet:** Saturated on the primaries + the minimal TWT context supplied. Starved of the rest of the TWT corpus and of every other referee's file in this directory (none opened, none listed).
**Scope of this file:** applicability of the theorem only. This referee takes NO position on whether TWT's chiral spectrum exists, and none on N67's magnitude.

---

## 0. PROVENANCE CAVEAT (read before quoting anything below)

Per the standing provenance-pinning rule, the tier of my own evidence is stated first.

- The primary was read through `WebFetch` extraction over `arXiv:2505.20436v3` HTML (submitted 2025-05-26, v3 2026-01-12). I did **not** hand-transcribe from the rendered PDF. Three fetches truncated (full bibliography, full Conclusions §VII).
- Consequence: quoted strings below are **HIGH-confidence extractions, not hand-verified transcriptions** (credence ~0.85 that each is verbatim to the letter; ~0.95 that each is verbatim in substance). The two load-bearing quotes — assumption (1) and the definition of `H_eff` — were each returned independently by **two separate fetches with different prompts**, which raises those two to ~0.93 verbatim.
- Anything this file recommends N67 assert should carry that caveat, or be re-read against the PDF by hand before banking.
- **Not established here:** the complete reference list of GS. My §3 claim that GS does not engage the bosonic-substrate SMG literature rests on the *body text* and the *scope statements*, not on a verified bibliography. Priced accordingly in §4.

**Sources read (all by my own web tools):**
1. **PRIMARY** — M. Golterman, Y. Shamir, *Constraints on the symmetric mass generation paradigm for lattice chiral gauge theories*, arXiv:2505.20436 (v3, 2026-01-12). Abstract + §I–§III + §VI + partial §VII.
2. M. Golterman, Y. Shamir, *Symmetric mass generation and the Nielsen-Ninomiya theorem*, arXiv:2603.15985 (2026-03-16) — same authors, short/proceedings restatement. Adds nothing to the hypotheses; **restates the conditional form**, which is itself evidence.
3. M. Golterman, Y. Shamir, *Propagator zeros and lattice chiral gauge theories*, arXiv:2311.12790 — the antecedent paper (the propagator-zero/ghost analysis the generalized no-go is built on).
4. **COUNTER-PRIMARY** — Z. Lu, S. Seifnashri, S.-H. Shao, *Lattice chiral symmetry from bosons in 3+1d*, arXiv:2604.06307 (2026-04-07).
5. **COUNTER-PRIMARY** — X.-G. Wen, *A lattice non-perturbative definition of an SO(10) chiral gauge theory and its induced standard model*, arXiv:1305.1045.
6. Located but not load-bearing: ZZWY = Zeng–Zhu–Wang–You, PRL 128 185301 (the 1+1D 3-4-5-0 SMG model GS analyse).

**Own-substrate check performed (not a corpus read):** `grep -rEi "grassmann|fock" knowledge/corpus/*.py` → **0 hits in all six engine files**. The `anticommut` hits (12, across `twt_core.py` / `twt_candidate_v3.py`) are **all** Clifford basis-vector anticommutation — `{e_{i4}, e_{j4}} = 0`, `e_123` anticommuting with `e_4`, `I_4` anticommuting with vectors — i.e. relations among **c-number multivector components in a real Clifford algebra**. There is no Grassmann-odd variable and no fermionic Fock grading anywhere. The supplied premise **holds and holds for the right reason**: Clifford anticommutation is a *bosonic* algebraic fact and must never be mistaken for a fermionic one. (Flagging that confusion explicitly, because it is the single most likely way this verdict gets mis-cited later.)

---

## 1. THE CATEGORY QUESTION — what is the theorem's universe of discourse?

### 1.1 The theorem as stated

GS §III, immediately after Eq. (24b), states the generalized no-go over a **reduced model** with a compact unbroken global symmetry `G` whose generators are discrete-valued conserved charges, under three numbered assumptions:

> **(1)** *"The hamiltonian has a finite range, and depends on fermion fields only"* — GS §III, assumption (1).
> **(2)** The continuum limit is relativistic free massless fermions **with no massless bosons**.
> **(3)** In each charge sector supporting a massless fermion, a complete set of interpolating fields exists with `ℛ(p⃗)` free of zeros.

Conclusion: `H_eff(p⃗)` then satisfies every NN hypothesis and *"the massless fermion spectrum ... is vector-like."*

The authors themselves scope this. GS §I:

> *"...all of its assumptions need to be satisfied, and this must be checked on a case by case basis"* — GS §I.

That sentence is the referee's warrant: GS did not write an unconditional theorem, and reading their abstract's headline as one is the error to prosecute.

### 1.2 The instantiation ladder — where exactly it fails

Ordered by *first encounter*, not by importance. TWT's fundamental variables are a classical bosonic rotor/orientation field on a D4 lattice; matter states are `π₃(S³)` solitons.

| # | Object in GS's hypotheses | Referent in a bosonic-substrate/solitonic theory | Status |
|---|---|---|---|
| **P0** | *"reduced model"* (preamble) — GS define it as what remains when *"we turn off the gauge field"* of a lattice gauge theory with massless Dirac fermions | **None.** There is no parent lattice gauge theory, no gauge field to switch off, and no Dirac fermion whose mirror needs decoupling. The construction has no UV fermion doubler problem because it has no UV fermion. | **NO REFERENT — first failure** |
| **P1** | Assumption (1): Hamiltonian *"depends on fermion fields only"* | **None.** Zero Grassmann variables (verified). The hypothesis is not *false* here — it is **undefined**: it predicates a property of a set of objects the theory does not contain. | **NO REFERENT — first failing *numbered* hypothesis** |
| **P2** | The theorem's central object: `ℛ(p⃗)` = a hermitian **fermion two-point function** at zero frequency, from retarded **anti-commutators** (GS eqs. 18–21); `H_eff(p⃗) = ℛ⁻¹(p⃗)` | **None.** Constructing `ℛ` requires (a) fermion field operators and (b) a canonical anticommutator, i.e. a Fock-graded Hilbert space. Neither exists. **There is nothing to invert.** | **NO REFERENT — the deepest failure** |
| **P3** | Assumption (2): continuum limit = free massless fermions, **no massless bosons** | **Referent exists — and the hypothesis is prima facie FALSE.** A rotor/orientation field on a lattice generically carries massless bosonic modes (Goldstone/phonon-type). GS themselves grant this is fatal to their own construction (§3.1 below). | **INSTANTIATED AND VIOLATED** |
| **P4** | Assumption (3): a *complete set of interpolating fields*, and finite range ⇒ analyticity in a periodic BZ | **Partial referent.** One could try composite operators creating solitonic states — but a `π₃(S³)`-winding-creating operator must rearrange the field over a region and set the winding at infinity; it is **not finite-range**. | **INSTANTIATED AND VIOLATED (locality)** |

### 1.3 Is there ANY reading under which it binds?

I tried three and report each honestly.

**Reading A — "read the theorem as being about the emergent low-energy fermionic sector, whatever its microscopic origin."** This is the strongest pro-applicability reading and it is *not* silly, because GS **explicitly permit composite interpolating fields** — they conjecture *"the SMG interactions generate opposite-chirality bound states"* (GS abstract) and propose adding composite fields to the elementary set. So the naive TWT defence *"our fermions are composite, therefore GS cannot see them"* **FAILS**: GS's framework is built to see composites.
Where Reading A nonetheless breaks: GS's composites are composites **of fermion fields**, in a theory where a global fermion-parity/charge grading already exists at the cutoff and where the interpolating operators inherit finite range from a finite-range fermionic Hamiltonian. Strip the fermionic UV and both properties must be *re-derived*, not inherited. Assumption (1) is precisely the sentence that supplies them. **Reading A does not bind.**

**Reading B — "the ℤ₃/discrete-charge structure is enough; GS only need discrete conserved charges."** True, and this one **cuts against TWT**, so I state it: GS require only *"a compact global symmetry G"* with *"discrete-valued conserved charges"*. A ℤ₃-discrete colour is squarely inside their charge-sector bookkeeping. **A "our colour is discrete, not a continuous gauge group" defence is worthless here.** Anyone drafting N67 should not reach for it.

**Reading C — "the theorem is really a topological index statement and doesn't care about Grassmann."** This is the honest worry and it is *not* an applicability reading — it is a mechanism reading. Treated in full in §3. It does not make the theorem *apply*; it makes the theorem *matter*.

**§1 finding:** the theorem's universe of discourse is **lattice theories whose fundamental variables include fermion fields**. Every object in the hypotheses — reduced model, `ℛ(p)`, `H_eff`, RH/LH assignment — is constructed from those variables. There is no reading under which it binds a theory with none, **as proved**.

---

## 2. THE HIDDEN-REFERENTIAL HUNT

Assumptions carried in from the SM / lattice-QFT frame without argument. Each rated for whether it is **load-bearing for the conclusion**.

**HR-1 — "the massless spectrum" is *defined* by fundamental-fermion correlators.**
Site: *"H_eff(p) is defined by the inverse of a suitable hermitian fermion two-point function"* (GS §III, eqs. 18–21).
**LOAD-BEARING — maximally.** This is not a background assumption, it is the theorem's constructive core. Every subsequent step (hermiticity, periodicity, continuous first derivative, degree counting) is a property of `ℛ⁻¹`. In a theory where "the spectrum" is defined by the *soliton sector's* excitation energies rather than by a field two-point function, the theorem has no object. **This is the category error, located precisely.**

**HR-2 — fermions exist at the cutoff and must be *removed*, rather than *emerging* in the IR.**
Site: the framing throughout — *"one must therefore find a way to decouple all the mirror fermions"* (GS §I).
**LOAD-BEARING for the SMG framing, PARTIALLY defended.** The entire problem GS address is a *subtraction* problem (too many fermions at the cutoff, remove half). TWT's problem is an *addition* problem (none at the cutoff, produce some in the IR). These are not the same problem and a no-go against the first is not a no-go against the second. Partial defence for GS: their allowance of composite interpolating fields shows they anticipated emergence *within* a fermionic theory. But "emergent from fermions" and "emergent from bosons" differ exactly at HR-1.

**HR-3 — the target's gauge structure is a gauged continuous compact Lie group.**
Site: *"Let the gauge symmetry be a compact Lie group G"* (GS §II).
**NOT LOAD-BEARING against a discrete-colour theory** — see Reading B. Recorded so it is not misused as a defence.

**HR-4 — chirality is a *fundamental-field Weyl decomposition*, read off a relativistic linear dispersion at the singularity.**
Site: GS §III require *"a relativistic low-energy spectrum, which implies that every massless fermion is unambiguously either right-handed ... or left-handed"*.
**LOAD-BEARING.** The vector-like conclusion is a *count* of RH minus LH per charge sector. It presupposes (i) an exactly emergent Lorentz symmetry at the fixed point, (ii) a linear dispersion at each node, (iii) a two-valued chirality label attaching to one-particle states. In a solitonic sector, "chirality" would attach to a collective mode / a winding orientation, and its relation to a Weyl label is a *thing to be constructed*, not a given. **A theory that has not yet exhibited a chiral spectrum has, a fortiori, not exhibited the object HR-4 quantifies over.** (Note the two-edged nature: this also means TWT cannot claim to have evaded a count it has not yet performed.)

**HR-5 — the low-energy fermionic sector admits a *one-particle* Hamiltonian.**
Site: GS build *"a suitably constructed one-particle lattice hamiltonian describing the fermion spectrum"* (abstract).
**LOAD-BEARING.** This is a strong structural assumption even inside fermionic QFT — it is what converts an interacting problem into a band-topology problem. A soliton sector's low-energy dynamics is a collective-coordinate problem; that it reduces to a one-particle Bloch Hamiltonian is exactly the thing not established either way. **Undecided, both directions.**

**HR-6 — locality ≡ finite-range hopping ⇒ analyticity on a periodic Brillouin zone.**
Site: GS §III — *"lattice translation invariance, which implies that the momentum takes values in a periodic Brillouin zone"*, plus *"ℛ(p⃗) is an analytic function of p⃗ except at the degeneracy points"*.
**LOAD-BEARING — this is the actual topological engine.** NN is a degree/Poincaré–Hopf argument on a torus; without compactness+smoothness there is no invariant to conserve. This is simultaneously (a) the hypothesis a string-attached or winding-creating operator violates, and (b) the hypothesis a bosonic substrate on a *periodic lattice* most nearly satisfies. It is the hinge of §3.

**HR-7 (meta) — the headline sentence is stated unconditionally while the theorem is conditional.**
Site: the abstract's *"the massless fermion spectrum must be vector-like"* is preceded three clauses earlier by *"If these conditions are satisfied"*.
**Not load-bearing for GS's mathematics; load-bearing for how the paper gets cited.** This is exactly the RUL-049 pattern (a necessity claim honest in its fine print and false as a headline). Round-4 citation of this paper as "a generalized no-go at arbitrary interaction strength" reproduced the headline and dropped the conditioning class. Flagged as a citation hazard for our own record, not as a criticism of GS.

---

## 3. THE HONEST OTHER SIDE — does the mechanism still bite?

Required by the brief, and this is where I argue **against** my own §1.

### 3.1 The strongest form of "it still constrains you morally"

Strip the Grassmann variables from GS's argument and what remains is this:

> Let a gapless sector have (i) lattice translation invariance ⇒ a compact periodic Brillouin zone; (ii) an effective hermitian one-particle Hamiltonian `H_eff(p⃗)` with a continuous first derivative; (iii) a conserved discrete charge grading; (iv) linear relativistic dispersion at each node so that a two-valued chirality label exists. **Then within each charge sector the signed count of nodes is a topological degree of a map from a torus, and it vanishes. The spectrum is vector-like.**

**Nothing in that statement mentions Grassmann variables, Fock space, or fermion fields.** It is a statement about the topology of a smooth section over `T^d`. The Grassmann structure enters GS only in *how they construct* `H_eff` (via `ℛ⁻¹` from a fermion propagator) — i.e. in the *availability* of the object, not in the *argument once you have it*.

**And TWT supplies (i) for free.** A D4 lattice is exactly a periodic Brillouin zone. That is the uncomfortable part: the single most restrictive premise of the whole NN family is one a lattice substrate *volunteers*.

**Pricing it.** This is a genuine constraint on the *shape* of any future TWT chiral-spectrum construction. To deliver a chiral spectrum, TWT must **positively exhibit** at least one of:

- **(E1) Non-locality of the state-creating operator.** A `π₃(S³)`-winding operator is plausibly not finite-range — kills HR-6, kills analyticity, kills the degree argument. **This is TWT's most structurally natural escape and the one it should be able to argue.** *Cost:* "plausibly" is not a derivation. A soliton being a large object is not automatically the same as its interpolating operator being non-local in the sense NN needs; that must be shown, not gestured at.
- **(E2) Massless bosons in the low-energy spectrum.** GS **themselves concede this breaks their theorem**: *"The presence of marginal ... interactions in the reduced model invalidates the requirement that H_eff(p) has a continuous first derivative ... if the reduced model has massless bosonic states."* (GS, extracted). A rotor-field substrate has massless modes almost by construction. **This is the cheapest escape and it is granted by the opposing primary itself.** *Cost:* it is not free — those massless bosons then owe a phenomenological account (why is the world not full of them), and TWT does not get to claim the escape and disclaim the modes.
- **(E3) Non-relativistic or non-linear dispersion at the node** — kills HR-4's two-valued chirality. *Cost:* also kills emergent Lorentz invariance where you want it. Probably worse than the disease.
- **(E4) Absence of a one-particle description** (HR-5). *Cost:* undecided; not currently arguable in either direction.

**The sharpest thing I can say against our own side:** TWT has *already lost* one instance of this class. Per the supplied context, the Volovik/Fermi-point evasion was refuted **on our own substrate by our own spectral-node computation** — real symmetry class, no nodes. That is direct evidence that a band-structure-flavoured reading of the TWT substrate **does** fall to NN-type counting when actually computed. So the moral constraint is not hypothetical here; it has bitten once. **A referee who reports "does not apply" without carrying that forward has under-reported.**

**Verdict on this sub-question:** the mechanism survives as a **binding design constraint**, not as a theorem. It tells you what a successful construction must look like. It does not tell you one is impossible.

### 3.2 Does GS contradict the SMG-from-bosonic-substrate literature?

The positive literature exists and is explicit:

- **Wen, arXiv:1305.1045** claims a Spin(10) chiral gauge theory with Weyl fermions in the **16**, and the induced Standard Model, can be regularized as the low-energy effective theory of a **local 3+1D lattice model of qubits/bosons**. This is a positive claim of exactly the kind GS's headline appears to forbid.
- **Lu–Seifnashri–Shao, arXiv:2604.06307 (2026-04-07)**, in 3+1d, state the point flatly: *"Nielsen-Ninomiya-type no-go theorems are evaded by using lattice bosons rather than fermions."* This is an **independent, recent, 3+1D primary** asserting precisely the category boundary §1 located. It is the single strongest external corroboration of this verdict, and it is not by anyone with a stake in TWT.

**Does GS engage them?** On the body text I could read: **no.** GS's worked target is **ZZWY** — Zeng–Zhu–Wang–You's **1+1D fermionic** 3-4-5-0 model (PRL 128 185301) — and GS confirm its instantiation on fermionic grounds: *"the model depends on fermion fields only, and has a finite-range hamiltonian."* They cite a Wang–You-type review and "You et al." but I could not verify a Wen-1305.1045 entry (bibliography fetch truncated — see §0). GS also devote space to *"the qualitative differences between four-dimensional and two-dimensional theories that limit the lessons"* drawable from 2D models — which is a warning about their own worked example's dimensionality, and cuts *both* ways.

**Plainly stated conflict analysis — three levels, kept separate:**

1. **As theorems: NO CONTRADICTION.** GS's conclusion is conditioned on hypothesis (1) restricting to fermion-field Hamiltonians. Wen's and Lu–Seifnashri–Shao's constructions are outside that hypothesis by construction. Two consistent statements about disjoint domains.
2. **As physics claims: GENUINE, UNRESOLVED TENSION.** GS's *animating thesis* is that the SMG mechanism — gapping mirrors by interactions without symmetry breaking — cannot deliver a chiral massless spectrum. Wen's construction is an SMG-flavoured mirror-gapping argument that claims it can, in a bosonic model. If GS's mechanism-level intuition generalizes past their hypothesis (1), Wen is in trouble; **GS do not attempt that generalization, and until someone does, the tension is open.**
3. **As a defence for TWT: WORTHLESS AS CITED.** Wen's positive result is a *specific* anomaly-free 16-per-generation construction with its own machinery. TWT has not exhibited that construction. Citing Wen as cover would be an unregistered import doing load-bearing work — the §1-disguise failure mode, not a rebuttal. **The most it licenses is the negative, categorical point: the literature does not treat "bosonic substrate ⇒ no chiral fermions" as established, and at least two independent primaries treat the opposite as available.**

---

## 4. VERDICT

### **DOES-NOT-APPLY-AS-PROVED — with a surviving heuristic constraint (i.e. PARTIALLY, at the mechanism level).**

**Failing hypothesis, named, in order of encounter:**
- **First failure (preamble):** the object *"reduced model"* — presupposes a parent lattice gauge theory with fundamental Dirac fermions and a gauge field to switch off. No referent.
- **First failing numbered hypothesis: assumption (1)** — *"The hamiltonian has a finite range, and depends on fermion fields only"* (GS §III). Not false; **undefined**, for want of the objects it predicates over. Independently verified against our own substrate: 0 Grassmann, 0 Fock, all `anticommut` sites Clifford-algebraic.
- **Deepest failure (constructive core):** `H_eff(p⃗) = ℛ⁻¹(p⃗)` with `ℛ` a hermitian **fermion two-point function** from retarded anticommutators. **There is no object to invert.**
- **Additionally instantiated-and-violated, if one insists on an emergent-sector reading:** assumption (2) (no massless bosons — a rotor substrate generically has them, and GS concede massless bosons break the continuous-first-derivative requirement) and the finite-range/analyticity premise (a winding-creating operator is not finite-range).

**Surviving as heuristic:** the topological core (§3.1) — periodic BZ + smooth hermitian one-particle `H_eff` + charge grading + linear nodes ⇒ vector-like — is Grassmann-free and would bind **any** emergent sector that turns out to admit that description. TWT's lattice supplies the BZ. Our own refuted Volovik/Fermi-point attempt is evidence this is a live, not academic, risk.

### 4.1 What N67's wording MAY say about this paper

- That GS 2505.20436 proves a **conditional** generalized no-go, and that its **assumption (1)** — a finite-range Hamiltonian depending on fermion fields only — has **no referent** in a substrate with no Grassmann variables; and that its central object `H_eff = ℛ⁻¹` is constructed from a fermion propagator that does not exist here.
- That **the authors themselves** scope the theorem *"case by case"* (GS §I) and condition the vector-like conclusion on all three assumptions.
- That the categorical boundary is **independently asserted in a 3+1D primary by uninvolved authors** — Lu–Seifnashri–Shao, arXiv:2604.06307: NN-type no-goes *"are evaded by using lattice bosons rather than fermions."*
- That **the transformed N67 debt is therefore NOT blocked in principle by GS-as-proved** — stated *with its conditioning class* per RUL-049: *not blocked within the conditioning class {GS assumptions (1)–(3) as stated}*.
- That the mechanism nonetheless survives as a **design constraint**, and that N67 should name the four escape routes E1–E4 as things TWT must **exhibit**, with E2 (massless bosons) explicitly conceded by GS themselves and E1 (non-local winding operator) the most structurally natural but **currently unargued**.

### 4.2 What N67's wording MAY NOT say

- ❌ **"Nielsen–Ninomiya and its generalizations do not apply to TWT."** Blanket form, no conditioning class — a §4/RUL-049 violation and false at the mechanism level.
- ❌ **"Golterman–Shamir is refuted / wrong / does not hold."** Nothing here touches their proof. The finding is about *instantiation*, not validity. Confusing the two would be the mirror of the error being prosecuted.
- ❌ **"Wen / the SMG literature shows chiral fermions come from bosonic lattices, so TWT is fine."** Unregistered load-bearing import + §1 disguise. Wen's is a specific construction TWT has not exhibited.
- ❌ **Any wording implying the debt is discharged, reduced, or made easier.** N67's magnitude is **untouched** by this verdict. Not-blocked ≠ delivered. The debt remains: *exhibit the chiral spectrum on the solitonic route.*
- ❌ **"Our fermions are composite, so GS can't see them."** GS explicitly admit composite interpolating fields (§1.3 Reading A). This defence is dead; do not write it.
- ❌ **"Our colour is discrete, not a continuous gauge group, so GS doesn't apply."** GS need only *"discrete-valued conserved charges"*. Dead defence; do not write it.
- ⚠️ Any verbatim quote from GS reproduced in N67 must carry the §0 provenance caveat, or be re-read from the PDF by hand first.

### 4.3 Layered credences

| # | Layer | Credence |
|---|---|---|
| L1 | GS assumption (1), as stated, quantifies over lattice Hamiltonians built from fermion fields; a Grassmann-free substrate does not instantiate it | **0.96** |
| L2 | No reading of GS's hypotheses binds a bosonic-substrate/solitonic theory **as proved** ⇒ DOES-NOT-APPLY-AS-PROVED is the correct verdict | **0.90** |
| L3 | The mechanism's topological core would bind **any** emergent sector admitting a smooth one-particle Bloch `H_eff` with charge grading on TWT's BZ ⇒ a real surviving design constraint | **0.85** |
| L4 | GS does not directly engage the bosonic/qubit-substrate SMG *positive* claims (Wen-type) | **0.85** *(capped: bibliography fetch truncated)* |
| L5 | GS and the bosonic-substrate literature do **not** formally contradict (disjoint domains), while remaining in genuine unresolved physics tension | **0.80** |
| L6 | GS themselves concede massless bosons invalidate the continuous-first-derivative requirement (escape E2 is granted by the opposing primary) | **0.80** *(single-fetch extraction)* |
| L7 | E2 (massless bosons) or E1 (non-local winding operator) is TWT's **actual operative** escape rather than merely an available one | **0.50** |
| L8 | Every quoted string above is verbatim to the letter | **0.85** *(0.93 for assumption (1) and the `H_eff = ℛ⁻¹` definition — each double-fetched)* |

---

## 5. FORECAST RECONCILIATION

The commission's forecast was: *DOES-NOT-APPLY-AS-PROVED (hypotheses quantify over fermion-field lattice theories), surviving heuristic worry, no direct engagement with the SMG-from-bosonic-substrate positive literature.*

**All three confirmed.** This referee flags that the forecast was accurate, which is itself a mild anti-signal: a review that merely returns its own forecast carries reduced information. Three findings **not** in the forecast, offered as the independent content:

1. **The composite-field defence is dead.** GS explicitly permit composite interpolating fields and conjecture bound-state formation. The naive "our fermions are composite" rebuttal fails; the category failure had to be relocated to the *fundamental variables* and to `ℛ`'s constructibility. Anyone drafting N67 from the forecast alone would likely have written the dead defence.
2. **The discrete-colour defence is dead.** GS need only discrete conserved charges; ℤ₃ colour is inside their bookkeeping, not outside it.
3. **GS concede escape E2 themselves** (massless bosons break the continuous-first-derivative requirement) — the opposing primary supplies TWT's cheapest escape, and it is a *priced* escape, not a free one.

**Standing recommendation to the adjudicator:** the honest headline is not *"the theorem doesn't apply."* It is *"the theorem's hypotheses have no referent in our substrate, and the theorem's mechanism tells us what our construction must look like if it is to work."* The second clause is the load-bearing one for N67.

---
*Referee B, applicability. This file is the complete deliverable; nothing else in the repository was modified.*
