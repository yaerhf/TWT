# VERDICT — REFEREE A (PROSECUTORIAL): THE GOLTERMAN–SHAMIR GENERALIZED NO-GO, FROM THE INSIDE

**Date:** 2026-08-24 · **Joint:** the theorem as proved — statement, hypotheses, load-bearing steps,
the authors' own scope limits, and the citing literature. **Diet:** saturated on the two primaries;
starved of the TWT corpus and of the applicability referee. Nothing below is an opinion about TWT.

## 0. The primaries, as fetched

| Ref | Identity | Status |
|---|---|---|
| **PRD** (main target) | M. Golterman, Y. Shamir, *Constraints on the symmetric mass generation paradigm for lattice chiral gauge theories*, arXiv:**2505.20436** [hep-lat] (v1 26 May 2025; **v3** 12 Jan 2026, "Clarifications (in particular Sec. 6) added, no changes in conclusions. Matches published version") | Published **Phys. Rev. D 113 (2026) 014503**, DOI 10.1103/qd1t-wzy1. RevTeX, 41 pp. **License CC BY 4.0** (verbatim quotation below is licensed, with attribution). Read in full: Secs. I–VII, App. A.1–A.4, App. B.1–B.4. |
| **PRL** (predecessor) | M. Golterman, Y. Shamir, *Propagator zeros and lattice chiral gauge theories*, **Phys. Rev. Lett. 132 (2024) 081903**, arXiv:2311.12790 | Read in full (6 pp., v2). |
| (context, same authors) | *Symmetric mass generation and the Nielsen-Ninomiya theorem*, arXiv:2603.15985 (16 Mar 2026) | Lattice-proceedings **overview of the PRD by the same authors** — not an independent check. Read. |

Two upstream results the PRD leans on but does not re-derive: **Shamir, PRL 71 (1993) 2691** and its long
companion (cited `NNYSPRL`/`NNYSlong`) — the *original* generalization, in which, in the PRD's own words,
"analyticity properties were essentially postulated" (Sec. I). The PRD's genuinely new content is (i) a
**proof** of that analyticity under stated assumptions (App. B.2/B.3), and (ii) the **bound-state /
kinematical-zero** conjecture that is supposed to secure hypothesis (3).

---

## 1. THE THEOREM AS STATED (verbatim, Sec. III; CC BY 4.0, © Golterman & Shamir)

> "Consider a reduced model defined on a regular spatial lattice, with a compact global symmetry $G$ that
> is not broken spontaneously. The $G$ generators are thus discrete-valued conserved charges. Assume also:
> (1) The hamiltonian has a finite range, and depends on fermion fields only; (2) The continuum limit is a
> theory of relativistic free massless fermions and with no massless bosons; (3) In any charge sector which
> supports at least one massless fermion, one can find a complete set of interpolating fields (as defined in
> the introduction) so that the corresponding ${\cal R}(\vec p)$ is free of zeros. Then $H_{\rm eff}(\vec p)$
> satisfies all the assumptions of the Nielsen-Ninomiya theorem, and as a result, the massless fermion
> spectrum in this charge sector is vector-like."

### 1a. What the objects are (answering "massless spectrum of WHAT, probed by WHICH correlators")

- **Of what.** The **reduced model** — the target lattice chiral gauge theory *with the gauge field turned
  off*, so that the gauge group $G$ is an exact **global** symmetry. The theorem never touches the gauged
  theory. The claim is about the **massless fermion asymptotic states** of that reduced model, **charge
  sector by charge sector** under $G$. "Vector-like" = equal numbers of RH and LH massless states in each
  sector (in $d=1$ spatial dimension, right-movers vs left-movers).
- **Probed by.** The **zero-frequency limit of the retarded (equivalently advanced) anticommutator**
  two-point function of a chosen set of interpolating fields $\Psi_a$:
  $R_{ab}(\vec x,t)=i\theta(t)\langle 0|\{\Psi_a(\vec x,t),\Psi_b^\dagger(0,0)\}|0\rangle$ (Eq. 18),
  Fourier-transformed (Eqs. 19–20), then ${\cal R}(\vec p)=\lim_{\epsilon\to0}\tilde R(\vec p,i\epsilon)$
  (Eq. 21), and finally $H_{\rm eff}(\vec p)={\cal R}^{-1}(\vec p)$ (Eq. 1).
  Retarded/advanced, **not** time-ordered — that choice is load-bearing (footnote 35: "This is where the use
  of the retarded (or advanced) two-point function is crucial"), because it is what makes the $t$-integral
  converge for ${\rm Im}\,\omega>0$ and hence gives analyticity in $\omega$.
- **Objects that must exist.** A **spatial lattice** with continuous time and a **second-quantized
  hamiltonian** acting on a **fermionic Fock space**; a **unique translation-invariant vacuum** $|0\rangle$
  and a momentum-resolved spectrum $|\vec p,n\rangle$ (used in App. B.1, Eqs. 49–50); **asymptotic
  single-particle states** with an interpolating-field (LSZ-like) dictionary; **elementary fermion fields
  obeying canonical anticommutation relations**; and a set of **local composite operators** built from them.
  No transfer matrix, no gauge field, no path integral is required — the whole apparatus is canonical
  hamiltonian.
- **Definitions carried in from Sec. I** (they are part of the hypothesis, not decoration):
  a **degeneracy point** = a $\vec p_c$ receiving a contribution from intermediate states with $E\to0$;
  a **primary singularity** = a degeneracy point where ${\cal R}\to\infty$ (⇒ $H_{\rm eff}$ has a zero
  eigenvalue); a **complete set of interpolating fields** = a set for which (1) the massless fermion
  asymptotic states are in **one-to-one correspondence** with the primary singularities and (2) ${\cal R}$
  is **free of zeros**.

### 1b. The proof skeleton (five links)

1. **Equality** ${\cal R}={\cal A}$ away from degeneracy points (Sec. III, property 1) — spectral
   decomposition, energy denominators $1/(\omega\pm E)$.
2. **Hermiticity** of ${\cal R}$, hence of $H_{\rm eff}$ (App. B.1) — $v_a v_b^*$ manifestly hermitian; the
   time integral gives a *real* factor as ${\rm Im}\,\omega\to0$.
3. **Smoothness / analyticity** of ${\cal R}(\vec p)$ away from degeneracy points (App. B.2, B.3) — a
   Lieb–Robinson-type argument: the multi-commutator Taylor series (Eq. 55), the finite range $R_0$ of the
   hamiltonian density, and the **operator-norm bound** deliver
   $\|\{\psi(\vec x,t),\psi^\dagger(0,0)\}\|\sim(2eR_0{\cal N}t/\|\vec x\|)^{\|\vec x\|/R_0}$ (Eq. 56), which
   falls faster than exponentially; $C^\infty$ in $\vec p$ follows, and (B.3) analyticity via the
   **edge-of-the-wedge theorem** on wedges $W^\pm={\cal E}\pm i{\cal U}$ with the cone condition
   $\|{\rm Im}\,\vec p\|\,s_0^{\max}<{\rm Im}\,\omega$ (Eq. 66).
4. **Behaviour at the degeneracy points** (Sec. III, Eqs. 23–24; App. B.4 for secondary ones) — relativistic
   leading behaviour is *assumed* (Eq. 23), and the leading non-analytic correction is *estimated* from a
   one-loop EFT self-energy with two least-irrelevant vertices, giving
   $E=\pm q\,[1+c_1G^2(aq)^{2(n-d-1)}\log q^2]$ with $n-d-1\ge1$ (Eq. 24) ⇒ **continuous second derivative**.
5. **Invoke Nielsen–Ninomiya** on $H_{\rm eff}$: hermitian matrix family over a periodic Brillouin zone,
   commuting with discrete-valued charges, $C^1$, relativistic zeros ⇒ RH and LH zeros balance in each charge
   sector. Hypothesis (3)'s one-to-one correspondence transports that count from $H_{\rm eff}$'s zeros to the
   physical massless spectrum.

### 1c. Where "interaction-strength independence" actually comes from

**Not** from propagator zeros — zeros are the *obstruction to be removed*, never the source of the result.
It comes from exactly two places, and both are worth naming precisely:

- **Link 3 is uniform in the coupling**: the bound needs only $R_0<\infty$ and ${\cal N}=\|{\cal H}(\vec x)\|<\infty$.
  Strength enters solely through ${\cal N}$, i.e. through the slope of the effective light-cone
  ($s_0 = 2R_0{\cal N}e^{R_0\|{\rm Im}\vec p\|+1}$, Eq. 63). Prosecutorially: the analyticity **domain
  shrinks** as the coupling grows (Eq. 66 tightens like $1/{\cal N}$) but never closes for finite coupling.
  So "arbitrary strength" is honest for any finite coupling and **fails at strictly infinite coupling**,
  where ${\cal N}\to\infty$ — which is exactly the limit Sec. IV takes (see §4, crack C4).
- **Link 4 is strength-independent only because hypothesis (2) makes it so**: near the continuum limit the
  surviving interactions among the massless states must be irrelevant *whatever* the lattice-scale coupling
  was. The theorem's advertised power over strongly-coupled SMG phases is therefore **entirely borrowed from
  hypothesis (2)**, not earned by the dynamics. That is the single most important structural fact about this
  theorem and the authors say so plainly (Sec. VII: "basically because the continuum limit of the reduced
  model has to be a free theory").

---

## 2. HYPOTHESIS TABLE

**A. Stated in the theorem box**

| # | Hypothesis | Where stated | Role in the proof | What breaks without it |
|---|---|---|---|---|
| H1 | Regular spatial lattice, lattice translation invariance | Thm, Sec. III; §1b link 3 | Gives a **periodic Brillouin zone**; makes $\hat R(\vec p,t)$ a Fourier sum | NN's topological counting has no compact momentum torus — the theorem is void, not merely weakened |
| H2 | Compact global symmetry $G$, **not spontaneously broken**; generators = discrete-valued conserved charges | Thm; Sec. III p. after Eq. 21 | Block-diagonalizes ${\cal R}$/$H_{\rm eff}$ into **charge sectors**; NN counts within a sector | No sector labels ⇒ no per-sector RH/LH balance; SSB also destroys the unique-vacuum spectral decomposition of App. B.1 |
| H3 | Hamiltonian of **finite range** $R_0$ | Thm (1); App. B.2 cond. (2) | Sets $n(\vec x)\ge\|\vec x\|/R_0$ in Eq. 56 ⇒ faster-than-exponential clustering | Analyticity/smoothness of ${\cal R}$ fails; $H_{\rm eff}$ may be non-$C^1$; NN inapplicable (this is the SLAC-fermion escape) |
| H4 | Hamiltonian **depends on fermion fields only** | Thm (1); App. B.2 cond. (1); Sec. III property 3 | **Two distinct jobs.** (a) CAR ⇒ $\|\psi_a(\vec x)\|=1$ ⇒ ${\cal N}=\|{\cal H}(\vec x)\|<\infty$ — the *entire* norm apparatus of B.2/B.3; (b) makes the anticommutator $\{\Psi_a,\Psi_b^\dagger\}$ the natural object and the Fock/charge structure available | (a) With **unbounded** local operators (canonical bosons/scalars) the norm bound and hence the whole analyticity proof collapses; (b) the correlator's very definition loses its motivation. *See crack C1: (a) is over-stated as "fermionic" — what the proof actually needs is uniformly bounded local operators* |
| H5 | Continuum limit = **relativistic free massless fermions**, **no massless bosons** | Thm (2); Sec. III Eqs. 23–24 | Fixes the dispersion form near $p_c$ (Eq. 23), forces residual interactions irrelevant ($n\ge d+2$), gives Eq. 24's $C^2$ | Marginal/relevant residual interactions ⇒ $n-d-1=0$ ⇒ $\partial E/\partial p$ discontinuous ⇒ NN inapplicable. The authors demonstrate this failure in 2d (Sec. V) and in their own gauge-fixing programme (Sec. III) |
| H6 | Existence of a **complete set of interpolating fields** with **zero-free** ${\cal R}$ in every charge sector supporting a massless fermion | Thm (3); definition in Sec. I | Zeros of ${\cal R}$ ⇒ poles of $H_{\rm eff}$ ⇒ non-$C^1$ ⇒ NN inapplicable. Also *imports by definition* the one-to-one correspondence between primary singularities and massless states | The theorem's conclusion cannot be transported to physics: either $H_{\rm eff}$ is not $C^1$, or its zero-count is not the physical massless count. **This is the contested hypothesis and it is supported only by a conjecture** |

**B. Used but NOT in the theorem box** (prosecutorial extraction — each is load-bearing somewhere)

| # | Unstated hypothesis | Where used | What breaks without it |
|---|---|---|---|
| U1 | Hamiltonian (not Euclidean/path-integral) formalism; **continuous time** | Eqs. 18–21, 48, 52 | Sec. III concedes Euclidean formulations are "in a strict technical sense" outside the theorem; the transfer to Euclidean is asserted, not proved |
| U2 | **Unique** translation-invariant ground state $\lvert0\rangle$, infinite volume, momentum-resolved spectrum | App. B.1 Eqs. 49–50; B.3's $E_{\min}(\vec p)$ | A phase with **topological ground-state degeneracy** (a live possibility for SMG/"symmetric gapped" phases in the condensed-matter literature this paper is arguing with) is not excluded by H2 or H5, yet breaks the spectral decomposition as written. **Not discussed anywhere in the paper.** |
| U3 | Degeneracy points are **isolated** (finitely many), so primary singularities can be counted | Whole of Sec. III; NN's counting | A gapless surface (Fermi surface, gapless line) makes "one-to-one correspondence with massless states" ill-posed. Excluded *de facto* by H5, but never stated |
| U4 | The interpolating-field index $a$ runs over a **finite** set (finite matrix ${\cal R}$) | Eq. 1's inversion; NN on a finite-rank bundle | If a "complete set" required infinitely many composites, "inverse", "free of zeros" and the topological counting all need re-doing. Never addressed; the paper's finiteness assumptions concern each *operator's* locality, not the *number* of operators |
| U5 | Operator scaling dimensions in the low-energy EFT are **canonical integers** | Sec. III, before Eq. 24: dimension "is just its canonical mass dimension, which is integer" | An interacting IR fixed point gives anomalous dimensions and possibly $n-d-1<1$ arbitrarily small ⇒ Eq. 24's $C^2$ conclusion degrades. Excluded by H5's *free* continuum limit — another debt H5 pays |
| U6 | The near-zero eigenvectors can be **assembled into $2\times2$ Weyl blocks** in $d=3$ (Eq. 23b) | Link 4 | Multiple/degenerate massless states at one $p_c$ need not organize this way a priori; the paper asserts "it must be possible to choose a basis" |
| U7 | Majorana fermions excluded | footnote 3, Sec. I | Real representations only; irrelevant to chiral gauge theories, honestly flagged |
| U8 | In the free-hamiltonian sanity check: the interpolating set **must include every field in $H$** | Sec. III, after the theorem | Omitting fields yields $H_{\rm eff}\ne{\cal H}$ and **spurious** zeros/poles. Shows how strongly the conclusion depends on the operator-set choice — i.e. how much work H6 does |

---

## 3. THE SINGLE MOST FRAGILE STEP

I separate *step* from *hypothesis* because the honest answer differs.

**Most fragile PROOF STEP: Eq. (24) — the leading-log EFT estimate of $H_{\rm eff}$'s smoothness *at* the
primary singularities (Sec. III; App. B.4 for secondary ones).**

Everything else in the chain is either rigorous (B.1 hermiticity, B.2 norm bounds, B.3 edge-of-the-wedge) or
an explicit hypothesis. Eq. (24) is neither: it is a **one-loop, leading-logarithm, perturbative-in-$G$
self-energy estimate** ("The leading logarithmic correction ... will arise from a self-energy diagram with two
vertices of the least-irrelevant interaction") inserted at the one point where the theorem must control the
function's regularity, and it is inserted into a theorem whose entire selling point is validity at
**arbitrary interaction strength**. The tension is contained (not resolved) by H5: near the continuum limit
the EFT coupling $G$ is small *by hypothesis*. But no bound is proved — higher orders are not estimated,
non-perturbative contributions at $\vec p\to\vec p_c$ are not excluded, and the claim upgrade from "the
leading correction is $\propto(aq)^{2(n-d-1)}\log q^2$" to "$H_{\rm eff}$ has a continuous second derivative"
is a *leading-order* inference. The asymmetry is stark and should be stated plainly in any use of this
result: **the analyticity of ${\cal R}$ away from the degeneracy points is proved; the smoothness of
$H_{\rm eff}$ at the degeneracy points — the property NN actually consumes — is argued.**

Two things keep me from calling it wrong. (i) The step is **sharp, not vacuous**: the same estimate correctly
detects its own failure at $n-d-1=0$ (2d marginal four-fermion operators, Sec. V) and in the higher-derivative
scalar sector of the gauge-fixing model (Sec. III) — a criterion that flags real counterexamples is doing
work. (ii) The conclusion has a fallback: in Sec. V they retreat to the Karsten–Smit continuity/crossing
argument requiring only continuity of $E(p)$, which survives a discontinuous derivative in $d=1$ — though at
the price that the crossings can no longer be identified with massless fermions without model-specific work.

**Most fragile HYPOTHESIS: H6 (the zero-free complete set).** It is the contested one; it is supported only by
a two-part **conjecture** (Sec. VI: local theory ⇒ no ghosts in the low-energy EFT; corollary ⇒ a zero-free
complete set always exists); the conjecture's supporting mechanism (bound-state formation) is proved only
where a strong-coupling expansion exists (Eichten–Preskill, via Golterman–Petcher–Rivas), and **explicitly not**
in the model the paper is arguing about — the ZZWY model has no such expansion, so the bound states are
posited, with the honest admission "we have no concrete knowledge about the actual situation" (Sec. II).

**A dependency worth prosecuting: H6's definition is partly circular in effect if not in logic.** "Complete
set" is *defined* to include the one-to-one correspondence between primary singularities and massless
asymptotic states — i.e. the very bookkeeping that makes the free-theory counting transportable. The theorem
therefore reads, uncharitably but not unfairly: *if you can find a field basis in which the interacting
reduced model presents itself with the analytic structure of a free lattice hamiltonian, then the free-theory
theorem applies to it.* That is not vacuous — links 3 and 4 supply the non-trivial content that such a basis's
${\cal R}$ really is analytic and $C^1$ — but the physical bite is concentrated in an unproved existence claim.

**A historical crack the authors do not foreground.** The PRL (2311.12790, p. 5) considered exactly the
bound-state escape and dismissed it: bound states "would remedy the theory only if they undo the effect of
the propagator zeros both for the beta function and for the anomaly", followed by "It is hard to see how this
would come about." The PRD's *central mechanism* is that same escape, now adopted — footnote 12 concedes they
"did not appreciate that bound-state formation would ... play a key role." A referee should note that the
inference direction reversed between the two papers on the same evidence, and that no new calculation forced
the reversal (the driver is the locality argument attributed to You *et al.*).

---

## 4. FOUR ADDITIONAL INTERNAL CRACKS (prosecutorial, none fatal)

- **C1 — "fermion fields only" is stronger than the proof needs, and weaker than the abstract implies.** The
  actual content of App. B.2's use of H4 is: *local terms are bounded operators with uniformly bounded norm*
  ($\|\psi_a\|=1$ from the CAR ⇒ ${\cal N}<\infty$). Any lattice model with **finite-dimensional local Hilbert
  spaces** (spin systems, hard-core/clock/rotor variables with bounded generators) satisfies that, and the
  Lieb–Robinson machinery of B.2 runs unchanged. What genuinely fails for **canonical bosons/scalars** is
  norm-boundedness (unbounded operators). So the honest statement of hypothesis (1) for the *analyticity*
  half is "bounded local terms of finite range", not "fermionic". The genuinely fermionic content sits
  elsewhere: in the anticommutator being the natural correlator, in the Fock/charge-sector structure, and in
  reading $H_{\rm eff}$'s zeros as one-particle fermion states. The paper never makes this separation, and
  its own "wider setting" remarks (§5) never mention bosonic microscopic variables.
- **C2 — the "free hamiltonian" digression concedes basis-sensitivity.** Sec. III's own worked check shows
  that omitting fields present in $H$ produces $H_{\rm eff}\ne{\cal H}$ **with spurious zeros/poles**. The
  same sensitivity in the interacting case is precisely H6. The theorem is a statement about a *chosen
  operator basis*, and the paper offers no algorithm and no uniqueness claim ("building a complete set can be
  a trial and error process", Sec. I).
- **C3 — no per-model verdict is delivered.** The theorem is applied to nothing. For the ZZWY model, (1) holds
  by construction, (3) is *expected on the conjecture*, and (2) is judged to fail ("it is practically certain
  that this condition is not satisfied", Sec. VI). So the paper's headline conclusion is not instantiated in
  the one model it was written against.
- **C4 — Sec. IV's strong-coupling decoupling theorem is a separate result and is derived loosely.** Eq. (27)
  rescales $\chi\to g_1^{-1/n}\chi$ — legitimate as a Grassmann-measure/path-integral change of variables, but
  written in the hamiltonian formalism where a $c$-number rescaling of a canonical fermion operator **violates
  the CAR** $\{\chi,\chi^\dagger\}=1$ and the norm normalization that the rest of the paper relies on. Also,
  at strictly infinite coupling ${\cal N}\to\infty$, so B.2/B.3's analyticity apparatus does not apply in that
  limit. The conclusion (uncoupled $\xi$ sector ⇒ NN applies to it) is plausible and is corroborated by the
  earlier waveguide-model result; the derivation as written is not tight. This does **not** contaminate the
  main theorem, which never takes $g\to\infty$.

---

## 5. THE AUTHORS' OWN SCOPE STATEMENTS (quotes ≤15 words, attributed)

**5a. Bounding the reach**

| # | Quote | Where |
|---|---|---|
| S1 | "will not be subject to the generalized no-go theorem as stated above" | PRD Sec. III (of "many attempts" at lattice chiral gauge theories) |
| S2 | "or the theory may contain massless scalar fields besides the fermion fields" | PRD Sec. III (listing ways the assumptions fail) |
| S3 | "the required properties of $H_{\rm eff}$ were established in a fairly specific setting" | PRD Sec. VII |
| S4 | "It assumes that the reduced model contains fermion fields only" | PRD Sec. III, property 3 (analyticity) |
| S5 | "$H$ depends on fermion fields only." | PRD App. B.2, condition (1) |
| S6 | "Our work can only have tentative implications for any specific SMG model" | PRD Sec. I |
| S7 | "we have not reached a final verdict concerning the ZZWY model" | PRD Sec. VI |
| S8 | "it is practically certain that this condition is not satisfied" | PRD Sec. VI (condition (2), ZZWY) |
| S9 | "we have no concrete knowledge about the actual situation" | PRD Sec. II (the bound-state scenario) |
| S10 | "this would-be $H_{\rm eff}$ does not have a continuous first derivative" | PRD Sec. III (their own gauge-fixing approach) |
| S11 | "there might exist valid dynamical scenarios in which $H_{\rm eff}$ will not have" [a continuous first derivative] | PRD Sec. III |
| S12 | "the presence of marginal ... interactions ... invalidates the requirement" | PRD Sec. V |

**S10/S11 deserve emphasis.** The authors **themselves exhibit a local model containing a bosonic field in
which their theorem fails and the spectrum is chiral** — the gauge-fixing approach, whose higher-derivative
group-valued scalar $\phi\in G$ generates a coupling-dependent critical exponent and a discontinuous first
derivative of $H_{\rm eff}$ in one handedness per charge sector. This is an author-supplied existence proof
that hypothesis H4/H5 (no bosons) is load-bearing rather than technical.

**5b. Claiming reach beyond the proved setting**

| # | Quote | Where |
|---|---|---|
| W1 | "However, one expects that the generalized theorem is still relevant" | PRD Sec. III |
| W2 | "because in many cases one can still construct from the fermion two-point functions" | PRD Sec. III (continuation) |
| W3 | "experience teaches us that objects with essentially the same properties" | PRD Sec. VII |
| W4 | "can be constructed in a much more general setting" | PRD Sec. VII (continuation) |
| W5 | "Whenever such a construction is possible, the Nielsen-Ninomiya theorem eventually applies." | PRD Sec. VII |
| W6 | "the remarkably wide scope of the Nielsen-Ninomiya theorem" | PRD Sec. VII |
| W7 | "applies in principle everywhere in the phase diagram of any reduced model" | PRD Sec. VII (of the generalization) |

**Reading.** Every reach-claim is an **expectation with an unproved antecedent** (W1 "one expects"; W3
"experience teaches"; W5 "whenever such a construction is possible"). The *named* extension is to
**Euclidean path-integral lattice models** ("lattice models formulated within the euclidean path-integral
framework", Sec. VII) — i.e. a change of *formalism*, still with fermion fields. Nowhere in either primary do
the authors claim reach over models whose microscopic degrees of freedom are **not** fermionic. The nearest
they come is W5's conditional, which is content-free until the antecedent is established, and Sec. IV's
side-theorem, which does admit scalars ("These results easily generalize to the case that the reduced model
contains also scalar fields") — but Sec. IV is the strong-coupling decoupling result, **not** the generalized
no-go theorem.

**5c. The "theorem about free lattice theories" sentences — read carefully**

| # | Quote | Where |
|---|---|---|
| F1 | "because it is a theorem about free lattice theories" | PRD Sec. VII |
| F2 | "the NN theorem—which is a theorem about free hamiltonians—is safely inapplicable" | PRD Sec. I |

Both sentences are about the **original** Nielsen–Ninomiya theorem, and in both places the very next clause
**withdraws** the concession for the generalization. Sec. VII, immediately after F1: "However, the
generalization of this theorem ... applies in principle everywhere in the phase diagram of any reduced model,
including in an SMG phase." Sec. I, after F2: "At face value" ... "However, a closer look reveals another
facet ... which comes very close to satisfying the assumptions of the NN theorem." **These are set-ups for
the paper's thesis, not concessions about it.**

---

## 6. VERDICT ON OUR RECORD'S ATTRIBUTION

Our record states: *"their stated setting is fermion-field-only, so it doesn't instantiate [a bosonic
substrate], but they claim wider reach."*

| Clause | Verdict | Ground |
|---|---|---|
| "their stated setting is fermion-field-only" | **VERIFIED — and understated.** | It is hypothesis (1) of the theorem *and* condition (1) of the analyticity proof (S4, S5). It is not a stylistic restriction: it is what delivers $\|\psi_a\|=1\Rightarrow{\cal N}<\infty$, the norm bound the entire B.2/B.3 apparatus rests on. The authors call the setting "fairly specific" themselves (S3). |
| "so it doesn't instantiate [a bosonic substrate]" | **VERIFIED as a statement about the theorem's hypotheses.** (Whether some other object *would* satisfy them is the other referee's joint, not mine.) | H4 is not satisfied by a model whose microscopic hamiltonian is not built from fermion fields; the authors additionally exclude massless bosons (H5) and exhibit their own bosonic-field escape (S10/S11). **Caveat C1 stands: the *analyticity* half of the proof would survive for any bounded-local-operator model, so "not fermionic ⇒ theorem silent" is right, but "not fermionic ⇒ the machinery cannot be built" is too strong a reading of the same fact.** |
| "but they claim wider reach" | **PART-SUPPORTED (as forecast).** | The reach-claims exist and are prominent (W1–W7, including in the conclusion), so the attribution is not fabricated. But (i) they are **expectations/conjectures**, never proved or even sketched; (ii) the **named** generalization is Euclidean-formalism, still fermionic; (iii) **no claim of reach over non-fermionic microscopic degrees of freedom appears in either primary.** So the record's clause is accurate only if it is read as "they expect the *method* to generalize", and would be an over-read if used to mean "they claim their theorem covers bosonic/solitonic substrates." |
| (brief's third item) "a concession that it is 'a theorem about free lattice theories' that SMG phases escape" | **REFUTED as applied to the generalized theorem; VERIFIED only of the original NN theorem.** | F1/F2 are set-ups, immediately reversed in the same paragraph (§5c). Any use of F1/F2 as the authors conceding that *their* theorem is escaped by SMG phases misreads the text. What they *do* concede, and what should be quoted instead, is S1/S2/S3/S6/S7/S8/S10. |

**Recommended repair to the record's wording** (one sentence, so the citation survives contact with the
text): *Golterman–Shamir prove their generalized no-go for a hamiltonian lattice model that is finite-range
and built from fermion fields only, with a free-massless-fermion continuum limit and no massless bosons; they
do not prove, but do expect, that an $H_{\rm eff}$-like object exists in more general settings — the
generalization they name is to Euclidean fermionic path-integral formulations, and neither primary claims
reach over non-fermionic microscopic degrees of freedom.*

---

## 7. THE CITING LITERATURE — IS THE THEOREM CONTESTED?

INSPIRE, queried 2026-08-24: PRD (recid 2925563) **6 citations**; PRL (recid 2724859) **18 citations**.
Complete citing list for the PRD inspected. Findings:

- **No reply, Comment, erratum, or counter-paper exists.** Nothing in either citing list is directed at
  refuting the theorem or its proof.
- **Cited neutrally as legitimate by the SMG side.** Hasenfratz & Xu, *A Guide to Symmetric Mass Generation in
  Lattice-QCD* (arXiv:2604.02424) cite it under "the Nielsen-Ninomiya no-go theorem and its generalizations to
  interacting systems" — notable because Xu is an SMG proponent and a discussant thanked in the PRD.
- **Numerical SMG work cites it as background only**: Maiti, Banerjee, Chandrasekharan, Marinkovic
  (arXiv:2512.24836, arXiv:2602.18360) — no engagement with the hypotheses.
- **One paper is materially relevant and mildly adverse:** Baig, Chen, Cherman, Neuzil, *Bosonization versus
  the Nielsen-Ninomiya theorem* (arXiv:2607.09935, 10 Jul 2026), which cites **both** primaries and describes
  the status of propagator zeros as having "been debated". They study the **2D modified Villain scalar model**
  — an **ultra-local, purely bosonic** lattice model — construct composite fermionic operators, and find the
  reconstructed lattice Dirac operator is **doubler-free but non-local**, with poles whose total
  Poincaré–Hopf index is topologically fixed (movable by contact terms, but not all removable), while the
  microscopic model is "completely non-pathological". Their framing: NN "never forbids a ultra-local lattice
  model from having chiral fermions" in its long-distance spectrum.
  **How much does this dent GS?** It is **not** a counterexample to the theorem's conclusion (their spectrum
  is a single massless Dirac fermion — vector-like) and it does not violate any stated hypothesis (H4 fails
  outright: no microscopic Grassmann fields). What it *does* dent is the **conjecture** GS lean on to secure
  H6 — that in a *local* theory the low-energy reconstructed inverse propagator cannot be non-local /
  pole-bearing without signalling ghosts. Here is a local, healthy, ghost-free model whose reconstructed
  $H_{\rm eff}$-analogue is robustly non-local. GS could answer that their conjecture is stated for
  fermionic reduced models — which is exactly the point at issue, and which is precisely where the
  fermion-field-only hypothesis stops being technical.
- **Independent verification: none found.** No third party has re-derived App. B.2/B.3 or checked Eq. (24).
  Status of the theorem in the field is therefore best described as **uncontested but also unexamined** — the
  only overview of it in the literature (arXiv:2603.15985) is by the same two authors.

---

## 8. LAYERED CREDENCES

| Layer | Claim | Credence | Note |
|---|---|---|---|
| L1 | **The theorem is correct as a physics-level result, given its hypotheses** | **0.90** | The chain is coherent, the upstream 1993 result is now properly proved rather than postulated, and the criterion correctly self-flags its known failure modes |
| L1′ | **The proof is rigorous as mathematics end-to-end** | **0.40** | B.1/B.2/B.3 are rigorous; Eq. (24) is a leading-order EFT estimate at the one point NN consumes. A mathematician would call the theorem conditional on an unproved regularity claim |
| L1″ | **The analyticity result (App. B.2/B.3) alone is correct** | **0.92** | Standard Lieb–Robinson + edge-of-the-wedge; the norm bookkeeping checks out; my only reservation is the un-flagged unique-vacuum assumption (U2) |
| L2 | **My hypothesis list (§2A+2B) is complete for load-bearing hypotheses** | **0.75** | The stated six are certain; the eight unstated ones are my extraction. U2 (unique vacuum / no topological ground-state degeneracy) and U4 (finite interpolating-field basis) are the two I would most expect a specialist referee to confirm as genuine and un-addressed |
| L3a | Our record's "stated setting is fermion-field-only" | **0.97 accurate** | Verbatim hypothesis (1) + App. B.2 condition (1) |
| L3b | Our record's "they claim wider reach" | **0.90 that PART-SUPPORTED is the right grade** | Reach is claimed as expectation, and the named extension is Euclidean-fermionic, not bosonic |
| L3c | Reading F1/F2 as a concession that SMG phases escape *their* theorem | **0.95 that this is a MISREAD** | Both sentences concern the original NN theorem and are reversed in the next clause |
| L4 | The theorem is currently **uncontested in the literature and independently unverified** | **0.90** | Full citing lists inspected; one materially relevant adjacent result (arXiv:2607.09935), no rebuttal |

---

### Files fetched (working copies, scratchpad — not banked)
`arxiv.org/html/2505.20436v3` (full text, converted); `arxiv.org/pdf/2311.12790` (PRL, 6 pp.);
`arxiv.org/html/2603.15985`; `arxiv.org/html/2607.09935`; `arxiv.org/html/2604.02424`;
`arxiv.org/html/2602.18360`; `arxiv.org/html/2512.24836`; INSPIRE API records 2925563 / 2724859 and their
citing lists.
