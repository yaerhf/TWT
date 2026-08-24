# READ_NN — Primary-read dossier: Nielsen–Ninomiya / symmetric mass generation

**Date:** 2026-08-24
**Worker:** primary-read duty, round-4 external-review cycle.
**Feeds:** quarantined import row **I-NN2**; rows **I-SMG-1 … I-SMG-6** of
`knowledge/reviews/r4_commission_2026-08-24/03_IMPORT_SMG_dossier.md` (§4 table).
**Diet:** this brief + the commission dossier only. No TWT derivation was opened.
**Fence:** every number and statement below was read in the artifact named. Secondary
sources appear only as locators or, where explicitly tagged, as characterizations of the
literature by named specialists. UNREACHABLE is recorded where it is the truth.

---

## 0. Sources fetched, with read-depth

| # | source | route | depth |
|---|---|---|---|
| S1 | Nielsen & Ninomiya, *Absence of Neutrinos on a Lattice. 1. Proof by Homotopy Theory*, Nucl. Phys. B185 (1981) 20 (erratum B195 (1982) 541) | INSPIRE-HEP record `inspirehep.net/api/literature` — publisher (Elsevier) abstract | **[ABS]** (publisher abstract of the primary) |
| S2 | Nielsen & Ninomiya, *Absence of Neutrinos on a Lattice. 2. Intuitive Topological Proof*, Nucl. Phys. B193 (1981) 173 | same route | **[ABS]** |
| S3 | Nielsen & Ninomiya, *No Go Theorem for Regularizing Chiral Fermions*, Phys. Lett. B105 (1981) 219 | same route | **[ABS]** (abstract is one sentence; carries no hypothesis list) |
| S4 | **D. Friedan, *A Proof of the Nielsen–Ninomiya Theorem*, Commun. Math. Phys. 85 (1982) 481–490** | https://www.physics.rutgers.edu/~friedan/papers/Commun_Math_Phys_85_481-490_1982.pdf | **[PRIMARY-FULL]** (10 pp., author-hosted CMP scan, text-extracted) |
| S5 | X.-G. Wen, arXiv:1305.1045, Chin. Phys. Lett. 30 (2013) 111101 | arXiv abs + arXiv PDF, text-extracted (7 pp.) | **[PRIMARY-FULL]** |
| S6 | J. Wang & X.-G. Wen, arXiv:1809.11171, PRR 2 (2020) 023356 | arXiv abs + arXiv PDF, text-extracted (24 pp.) | **[PRIMARY-FULL]** |
| S7 | You, BenTov & Xu, arXiv:1402.4151 | arXiv abs page | **[ABS]** |
| S8 | García-Etxebarria & Montero, arXiv:1808.00009, JHEP 08 (2019) 003 | arXiv PDF, text-extracted (83 pp.) | **[PRIMARY-FULL]** |
| S9 | Golterman & Shamir, arXiv:2311.12790, PRL 132 (2024) 081903 | arXiv abs + arXiv PDF, text-extracted (6 pp.) | **[PRIMARY-FULL]** |
| S10 | Golterman & Shamir, arXiv:2505.20436, *Constraints on the SMG paradigm…* | arXiv abs + arXiv PDF, text-extracted (41 pp.) | **[PRIMARY-FULL]** |
| S11 | Kikukawa, arXiv:1710.11101, PTEP 2019 073B02 | arXiv abs page | **[ABS]** |
| S12 | Kikukawa, arXiv:1710.11618, PTEP 2019 113B03 | arXiv abs page | **[ABS]** |

**UNREACHABLE:** the *typeset text* of S1/S2/S3 (Nucl. Phys. B / Phys. Lett. B are behind
Elsevier paywall — ScienceDirect returned HTTP 403; NASA/ADS returned HTTP 405; CERN CDS is
behind a bot-detection challenge, which I did not attempt to defeat; INSPIRE lists a
Rutherford-Lab preprint number RL-80-090 but hosts no scan). **The gap is filled at
primary strength by S4**, Friedan's independent CMP proof, which opens by stating the
Nielsen–Ninomiya hypotheses as a numbered list — the exact object claim 1 needs.

---

## 1. Claim 1 — Nielsen–Ninomiya hypotheses and conclusion

### 1a. The conclusion — **VERIFIED-AT-PRIMARY [ABS, S1]**

> "an equal number of species (types) of left- and right-handed Weyl particles (neutrinos)
> necessarily appears in the continuum limit"

— Nielsen & Ninomiya, Nucl. Phys. B185 (1981) 20, publisher abstract (via INSPIRE).
Doubling conclusion confirmed. The abstract also states the setting is "a general class of
fermion theories on a Kogut-Susskind lattice."

S2's abstract adds the discriminating dependency, verbatim: the theorem
"hangs on the existence of the charge (e.g. fermion number), and thus on the complex-field
formulation and on locality" — and that relaxing the charge assumption permits "a model
that has only one two-component field." That is the authors' own statement of a hypothesis
whose failure breaks the theorem, and it is a second escape route independent of the free-field one.

### 1b. The hypothesis list — **VERIFIED-AT-PRIMARY [PRIMARY-FULL, S4]**

Friedan, CMP 85 (1982) 481, §1 Introduction, states the theorem's conditions on the
Hamiltonian as an explicit numbered list. The four conditions, quoted in fragments:

- (1) **"it is quadratic in the fields"** — §1, p. 481
- (2) **"invariant under change of the phase of the fields"** — §1, p. 481 (the U(1) charge condition)
- (3) **"invariant under translations of the (cubic) lattice"** — §1, p. 481
- (4) **"local, specifically in the sense that it is continuous in momentum space"** — §1, p. 481

Friedan's abstract states the theorem as **"the impossibility of constructing lattice models
of non-selfinteracting chiral fermions"** (S4, abstract).

**Reconciliation with the dossier's I-SMG-1 premise cell** ("locality, translation
invariance, Hermiticity"):
- locality — **verified** (Friedan (4));
- translation invariance — **verified** (Friedan (3));
- **FREE / quadratic / bilinear action — verified, and it is the primary's condition (1)**, i.e.
  the load-bearing hypothesis is *listed first* in the only free-full-text primary proof;
- **Hermiticity — NOT-IN-PRIMARY as a listed condition.** Friedan does not enumerate it; it is
  carried implicitly in "the Hamiltonian." Golterman & Shamir's restatement (S10 §I) also
  omits it, listing instead: a **free** lattice Hamiltonian, a compact global symmetry,
  lattice translation invariance, a relativistic low-energy spectrum, and a momentum-space
  Hamiltonian with a continuous first derivative. **Recommendation: drop "Hermiticity" from
  the I-SMG-1 premise cell or demote it to "(implicit in self-adjointness of H)", and put
  FREE/QUADRATIC in the cell**, since that is the hypothesis TWT's escape actually turns on
  and it is currently missing from the row.

### 1c. The TWT-load-bearing point — **INFERENCE, not a primary statement**

The brief's load-bearing point is: *the hypotheses require a lattice fermion field with a
quadratic action, so a theory with no Grassmann fields is outside them.* The first half is
**VERIFIED-AT-PRIMARY** (Friedan (1), plus the abstract's "non-selfinteracting"). The second
half is **NOT-IN-PRIMARY**: no source read here says "a theory without fermion fields is
outside the hypotheses." It follows trivially from the hypothesis list (a condition on a
Hamiltonian quadratic in fermion fields cannot be evaluated where there are none), but the
step is an inference the corpus is making, not a quotation, and should be tiered as such.

### 1d. ⚠ ADVERSE FINDING — the free-field escape is under live attack, by name

Golterman & Shamir, arXiv:2505.20436 (S10), grant the escape and then attack it:

> "The original Nielsen-Ninomiya theorem does not apply in an SMG phase, because it is
> a theorem about free lattice theories." (§VI)

but they then prove a **generalized no-go theorem** valid "in the presence of (non-gauge)
interactions of arbitrary strength" (abstract), whose conclusion is:

> "If these conditions are satisfied, the massless fermion spectrum must be vector-like."
> (abstract)

Their mechanism: from the reduced model's two-point functions build a one-particle lattice
Hamiltonian `H_eff`, which then satisfies NN's conditions. Their stated setting is "a
lattice hamiltonian defined on a spatial lattice, which depends on fermion fields only, and
has a finite range" (§VI) — so it does **not** instantiate on a substrate with no fermion
fields either; but they explicitly claim wider reach: "objects with essentially the same
properties as this paper's `H_eff` can be constructed in a much more general setting" (§VI),
including Euclidean path-integral formulations, "if the underlying theory is local" (§VI).

**Consequence for the corpus:** "our matter is solitonic, so NN's free-field hypothesis is
not instantiated" is correct against the 1981 theorem and is *not sufficient* against the
2025 generalization. The generalization's own hypotheses (a complete set of fermion
interpolating fields; a free-massless-fermion continuum limit; a constructible local
`H_eff`) are the new thing the corpus owes an answer to. This is a real sharpening of the
NN debt, not a discharge of it. **I flag it for the adjudicator; I did not open the corpus
to assess it.**

---

## 2. Claim 2 — Wen, arXiv:1305.1045

### 2a. The general statement — **VERIFIED-AT-PRIMARY [PRIMARY-FULL, S5]**

Abstract, verbatim fragment:

> "any truly anomaly-free chiral gauge theory can be non-perturbatively defined by putting
> it on a lattice in the same dimension"

— Wen, arXiv:1305.1045, abstract. Restated near-identically in the Summary:
"as long as the chiral gauge theory is free of all anomalies" (Summary section).

### 2b. Conjecture status — **VERIFIED-AT-PRIMARY, with a precision the dossier should adopt**

The paper's *labelled* Conjecture is **not** the sentence above. The primary sets in
display, under the heading `Conjecture:`, a *different* proposition (Introduction):

> "A chiral fermion theory in d-dimensional space-time with a gauge group G is
> free of all gauge and gravitational anomalies if (1) there exist (possibly symmetry
> breaking) mass terms that make all the fermions massive, and (2) π_n(G/G_grnd) = 0 for
> n ≤ d+1" — Wen, arXiv:1305.1045, Introduction.

The paper then says "Such a conjecture allows us to show that…" (Introduction). So the
architecture is: a **labelled conjecture** supplies a *checkable criterion for anomaly-
freedom*, and the lattice-definability statement is presented as *shown* on the back of it
plus the anomaly↔SPT correspondence. The verbs across the paper are "propose"/"argue"/"show"
— never "prove."

**Verdict on the dossier's characterization:** the phrase "cite as a conjecture" is
**correct in force** but **imprecise in referent** — the primary's conjecture label sits on
the anomaly-freedom criterion, not on the definability claim, and the definability claim is
worded as a demonstration. A pedantic reviewer can catch this. Recommended I-SMG-4 wording:
*proposal resting on an explicitly labelled conjecture, not a theorem.*

### 2c. The 48 = 3 × 16 count — **VERIFIED-AT-PRIMARY, arithmetically; phrasing is the corpus's own**

Verbatim (abstract, and repeated in the Introduction):

> "a modified standard model (with 48 two-component Weyl fermions)"

and, Introduction:

> "the modified standard model contains a total of 48 two-component Weyl fermions
> (one extra neutrino for each family)."

The Summary confirms the representation: the construction is for Weyl fermions "in the
16-dimensional spinor representation of SO(10)" (Summary). So 48 = 3 families × (15 + 1)
= 3 × 16 is **exact and forced by the primary's own two statements**, but the primary never
writes the factorization "3 × 16." Quote the two facts, not the product, or mark the
arithmetic as the corpus's.

---

## 3. Claim 3 — Wang & Wen, arXiv:1809.11171 / PRR 2 (2020) 023356

### 3a. Spin(10) with Weyl in the 16 on a 3+1D lattice — **VERIFIED-AT-PRIMARY [PRIMARY-FULL, S6]**

Abstract, verbatim fragment:

> "we propose that Spin(10) chiral fermion theories with Weyl fermions in 16-dimensional
> spinor representations can be defined on a 3+1D lattice"

Status is **proposal**, stated as such in the primary's own verb, and the primary is candid
about its logical debts: "we do not require the complete versions of all these Propositions"
(§II), and it names a "logic gap here to establish Proposition 3" (§II). Good faith on the
authors' part; conjecture strength for the import.

**"Without doubling" — NOT-IN-PRIMARY as a phrase.** The abstract does not contain it. The
paper discusses prior approaches that "suffered from fermion doublings" (§I) and claims a
chiral low-energy spectrum, from which absence of doubling follows. Substantively fine;
the phrase is a paraphrase and should not be quoted as the primary's.

### 3b. ⚠ The 15n row — **CONTRADICTED as worded; the primary says something sharper and MORE favourable to a bosonic substrate**

The dossier's I-SMG-4 cell reads "the 15n (no-ν_R) Standard Models require extra structure."
The primary's abstract says instead:

> "Standard Models from the 15n-chiral fermion SU(5) Grand Unification can also be realized
> by a 3+1D local lattice model of fermions."

and the body draws the distinction the dossier misses (§IV, "Conclusion"-adjacent discussion):

> "The lattice model that realizes the dynamical SU(5) chiral gauge theory is also a local
> fermionic model (which is not a local lattice model of qubits)."

with the 16-fermion case explicitly the bosonic one: the Spin(10) theory and "the induced
16-fermion Standard Model, can be realized as the low energy effective theory of a local
lattice model of qubits" (§IV). And the primary adds "It does not require extra gauge
groups" — *of the SU(5)/15n case*, i.e. the exact opposite of "requires extra structure."

**The correct statement is a substrate-parity statement, not a difficulty statement:**
15n is realizable but only from a **fermionic** lattice; 16n is what a **bosonic / qubit**
lattice can produce. Since TWT's substrate is bosonic, this is *stronger* support for the
corpus's §3(C) than the dossier claimed — and the dossier's current wording is wrong in a
way that would be caught. **I-SMG-4's used-at cell should be re-worded.**

### 3c. ⚠ NEW CONSTRAINT NOT IN THE DOSSIER — a falsifiable condition on bosonic-substrate models

Immediately after the qubit claim, the primary states a consequence that no row in the
dossier carries (§IV):

> "all fermions and their fermionic bound states must carry non-trivial gauge charge"

described by the authors as "a falsifiable experimental prediction," and made concrete:

> "the 'Standard Model' from a lattice qubit model cannot just have a U(1)×SU(2)×SU(3)/Z_q
> gauge group" — §IV

because such a model "has fermionic bound states that carry no gauge charge"; therefore
"the 'standard model' from a lattice qubit model must have a larger gauge group, e.g.
adding a new Z2 gauge sector" (§IV), with an attendant cosmic-string signature.

**This is a live structural test on any bosonic-substrate candidate**, of exactly the class
the dossier's §3 was assembling, and it is *not* one of (A)–(D). It is adjacent to — and
possibly interacts with — the discrete-ℤ₃-colour question of OI-2, since a discrete gauge
sector is precisely what it demands. **Proposed as a further open item for the adjudicator**
(call it OI-3): does the corpus's matter content admit a gauge-neutral fermionic bound
state? I did not look; the diet forbade it.

---

## 4. Claim 4 — You, BenTov & Xu, arXiv:1402.4151

**VERIFIED-AT-PRIMARY [ABS, S7].** Abstract, verbatim fragments:

> "the Standard Model of particle physics (plus a right-handed neutrino) has precisely 16
> Weyl fermions per generation"

and the regularizability condition:

> "can be regularized on a 3 dimensional spatial lattice when and only when the number of
> flavors is an integral multiple of 16"

Both halves of the dossier's I-SMG-5 attribution to YBX are exact. The abstract also gives
the mechanism the dossier cites second-hand — interactions reducing a (4+1)D topological-
superconductor classification from ℤ to ℤ₈, with the boundary gappable "when and only when
the number of boundary chiral fermions is an integral multiple of 16." Read depth is
abstract-only; the body was not opened, so the *derivation* stays unverified — the *claim*
does not.

---

## 5. Claim 5 — García-Etxebarria & Montero, arXiv:1808.00009

Read at **[PRIMARY-FULL]** (83 pp. extracted). All four sub-claims verified.

### 5a. ℤ₁₆-valued anomaly — **VERIFIED-AT-PRIMARY**

Introduction:

> "a more careful analysis on arbitrary manifolds requires this number to be a multiple of 16"

(of the topological superconductor's fermion count), and §5 footnote 34 gives the group
explicitly: **"Ω^{Pin+}_4 (pt) = Z16"**, "generated by RP4." The relevant relation to the
five-dimensional Spin-ℤ₄ bordism is stated as Eq. (4.14), §4.3: **Ω^{Pin+}_4 ≈ Ω^{Spin^{Z4}}_5**.
Also §4.7-adjacent: "for the 3d topological superconductor one obtains a Z16 anomaly by
demanding exp(πiη) = 1 for arbitrary 4-manifolds" — with the note that restricting to
mapping tori sees only a ℤ₈. That last is a useful precision: the ℤ₁₆ is a genuinely
Dai–Freed (arbitrary-manifold) statement, not a conventional global anomaly.

### 5b. Per-Weyl contribution — **VERIFIED-AT-PRIMARY**

§4.3, p. 42, verbatim:

> "For each 4d Weyl fermion with charge 1 modulo 4, we get one 3d Pin+ Majorana fermion."

Combined with §4.3, p. 43:

> "the anomaly for the topological superconductor vanishes only when the number of Majorana
> fermions is a multiple of sixteen"

So "each unit-ℤ₄-charge Weyl contributes 1 mod 16" is **exactly right**, via the
one-Weyl → one-Pin⁺-Majorana map. The ℤ₄ is the reduction mod 4 of `X ≡ −2Y + 5(B−L)`
(Eq. 4.13, §4.3), under which "the charges of all SM fermions … are of the form q_i = 4k_i + 1."

### 5c. 15 vs 16 — **VERIFIED-AT-PRIMARY, with one scope correction the corpus must make**

§4.3, p. 43, verbatim:

> "the number of fermions in the standard model must be a multiple of sixteen for the Z4
> symmetry to be anomaly-free"

immediately followed by: "This is precisely the number of fermions in a generation of the
standard model, once we include the right-handed neutrino."

**⚠ Scope correction.** The primary's constraint is on the **total** fermion count, not
per generation. The dossier's §3 preamble demands (A)–(D) hold "generation by generation";
for (C) that is *stronger than the source*. Per-generation-16 is sufficient for the total to
be 0 mod 16 (48 ≡ 0), and three 15-Weyl generations fail (45 ≡ 13 mod 16), so the corpus's
conclusion survives — but the phrase "generation by generation" over-states the imported
theorem and should be softened to "on the total count, satisfied here generation-wise."

Likewise, the dossier's "a 15-Weyl generation carries a residual −1 mod 16" is the corpus's
own arithmetic (15 ≡ −1 mod 16); the primary states the multiple-of-16 condition, not the
residue. Harmless, but it is a restatement, not a quote.

### 5d. ⚠ The exactness caveat — **the primary states TWT's own condition as its own escape hatch**

§4.3, p. 43, closing paragraph, verbatim:

> "at low energies there is a mass term for νR that breaks B−L … the Z4 is broken
> explicitly, and there are only 15 massless fermions"

**This is the strongest single sentence in the read for the corpus's §3(C).** The primary
itself identifies the Majorana ν_R mass as the thing that *destroys* the ℤ₄ and voids the
constraint. A framework in which Majorana masses are structurally forbidden and B−L is exact
is therefore precisely the case in which the constraint applies at full force and the
16-count is not optional. The dossier asserted this consonance; the primary supplies the
matching caveat sentence that makes it non-trivial. **Recommend quoting this sentence in the
I-SMG-5 row** — it converts the consonance from "our number matches theirs" into "their
theorem has a stated loophole that our structure closes."

*(Register note, not a physics claim: I did not verify against the corpus whether R-089's
Majorana-forbidding is itself unconditional. That is the adjudicator's cell, not mine.)*

### 5e. Dai–Freed machinery covers DISCRETE symmetries — **VERIFIED-AT-PRIMARY, and better than "covers"**

This underwrites OI-2 (N68). §4 of the primary is titled **"Discrete symmetries and model
building constraints"**, with §4.1 **"Spin − Z_n"**, §4.2 "Baryon triality", §4.4
**"Spin^c − Z_n"**, and Appendix C **"Bordism groups for Z_k"**.

The machinery is not merely available — the ℤ₃ case is **computed and printed**. §4.1→§4.2,
verbatim fragment:

> "the net number of Z3 fermions (counted +1 if they have charge 1 mod 3, and −1 if they
> have 2 mod 3) has to vanish modulo 9"

i.e. Eq. (4.10): Σ_fermions s_i ≡ 0 mod 9. §4.1 supplies the η-invariant formula on lens
spaces `L_k(n)` for Ω^{Spin}_5(BZ_n), n odd (ℤ₃ qualifies), and §4.4 supplies the **Spin^c−Z_n**
case — Spin ⊗ U(1) ⊗ ℤ_n, Eq. (4.20) and the charge-q generalization — which is *exactly*
the mixed structure OI-2 needs (Spin × ℤ₃ × U(1)_Y).

Two precisions worth carrying into OI-2:
1. The primary flags an incompleteness: after the Chinese-remainder split, "there might be
   mixed anomalies between the different factors" (§4.1) — so a factorized computation is
   not automatically complete.
2. The primary also notes the escape: if the ℤ_n embeds in a U(1) whose local anomalies
   cancel, all its Dai–Freed anomalies vanish, since Ω^{Spin}_5(BU(1)) = 0 (§4.1). **If the
   corpus's ℤ₃ colour is a subgroup of a U(1) with cancelling local anomalies, OI-2 is
   discharged for free.** That is a cheap first move on OI-2 and should be tried before the
   bordism computation is commissioned.

**Verdict: OI-2 is correctly framed, well-posed, and the template is not just "a template" —
the ℤ₃ constraint and the Spin^c−ℤ_n η-invariant are both explicit in the primary.**

---

## 6. Claim 6 — the dispute rows

### 6a. Golterman & Shamir — **VERIFIED-AT-PRIMARY; the dispute is live, and larger than the dossier records**

**PRL 132 (2024) 081903 = arXiv:2311.12790** [PRIMARY-FULL]. Bibliographic identity
confirmed (the dossier gives the PRL cite without the arXiv number; it is 2311.12790).
Abstract, verbatim fragments:

> "propagator zeros … act as coupled ghost states"

> "gauge invariance will always be maintained in an SMG phase … but unitarity of the gauge
> theory is lost."

Note the objection's *shape*, which the dossier's row understates: it is not merely "whether
the composite states do what the proposal needs." It is that anomaly-matching is satisfied
**vacuously** — the abstract says gauge invariance holds "even if the target chiral gauge
theory is anomalous" — which, if right, removes the diagnostic value of the anomaly ledger
in the SMG phase, and costs unitarity. Body, §IV: the propagator zero "ruins the unitarity
of the gauge theory in the SMG [phase]."

**arXiv:2505.20436** [PRIMARY-FULL], the follow-up: submitted 2025-05-26, **revised
2026-01-12**. ⚠ **The dossier calls this "a 2026 PRD follow-up." No journal reference is
carried on the arXiv record I read** — only the 2026 revision date. **Correct the row to
"arXiv:2505.20436 (v-latest 2026), journal status unverified"** or verify the PRD publication
independently; as written the row asserts a publication I could not confirm. This is a
provenance-pinning matter, not a physics one.

Its content is summarized at §1d above and is the sharpest item in this read: a *generalized*
no-go theorem claimed to apply "everywhere in the phase diagram of any reduced model,
including in an SMG phase" (§VI), concluding the massless spectrum "must be vector-like."
The paper closes by compiling "a list of open questions which must be addressed in any SMG
model" (abstract) — i.e. the authors themselves frame the matter as unresolved.

### 6b. ⚠ Kikukawa — **CONTRADICTED. Both Kikukawa rows are mis-assigned to the opposition.**

The dossier places Kikukawa on the negative/dispute side twice. Both are wrong at the
abstract level of the primaries.

**arXiv:1710.11101 (PTEP 2019 073B02)** — dossier: "arguing the mirror sector of the tested
2d abelian models does not decouple." The primary's abstract opens by attributing that view
to *others* — "it has been argued that the mirror fermions do not decouple" — and then
**re-examines and pushes back**. Its own result, verbatim:

> "we show a numerical evidence that the two-point vertex function of the gauge field in the
> mirror sector shows a regular local behavior"

(in a modified four-flavor axial model), concluding with a proposed chiral gauge model whose
induced measure term "satisfies the required locality property and provides a solution to
the reconstruction theorem." **Kikukawa is arguing that the mission is possible**, diagnosing
*why* the earlier attempt failed (insufficiently strong 't Hooft-type couplings; a singular
Majorana mass term).

Independent corroboration from the opposing camp: Golterman & Shamir (arXiv:2505.20436)
cite this very paper, in footnote 11, as **"an attempt to explain the failure of Ref. [40]"**
— Ref. [40] being Chen–Giedt–Poppitz, JHEP 04 (2013) 131 (arXiv:1211.6947). So the actual
negative result on the 3-4-5-0 mirror sector is **Chen–Giedt–Poppitz**, which the dossier
also cites and which is correctly placed; Kikukawa is the rebuttal to it.

**arXiv:1710.11618 (PTEP 2019 113B03)** — dossier: "raises the gauge-invariant measure
problem for overlap Weyl fermions in the 16 of SO(10)." The primary is a **construction**,
not a problem-raising:

> "We define a manifestly gauge-invariant path-integral measure for the left-handed Weyl field"

with the measure applying "to all possible topological sectors," CP-invariant induced action,
correct anomaly structure. One residual is named — "There remains the issue of locality in the
gauge-field dependence of the Weyl fermion measure" — and the abstract immediately adds that
this "can be addressed in the weak gauge-coupling expansion … without encountering the sign
problem." A named open residual inside a positive construction is not the same as raising an
objection to the paradigm.

**Required repair to I-SMG-3.** The row's parenthetical currently reads
"(CGP 2013; Kikukawa 2019 ×2; Golterman–Shamir 2024/2026)". It should read, with sides marked:
- **negative/obstruction side:** Chen–Giedt–Poppitz 2013 (numerical non-decoupling in the
  3-4-5-0 mirror sector); Golterman–Shamir 2311.12790 (ghosts / unitarity loss) and
  2505.20436 (generalized no-go);
- **constructive/rebuttal side:** Kikukawa 1710.11101 (diagnosis of the CGP failure +
  positive numerical evidence in a modified model) and 1710.11618 (gauge-invariant overlap
  measure in the 16 of SO(10), locality residual open).

The dossier's *governing instruction* — "cite the conjecture as a conjecture with named
opposition" — is **VERIFIED and correct**; the dispute is unambiguously live in 2024–2026,
with the most recent word (2505.20436, revised 2026-01) on the sceptical side. Only the
**attribution of who is on which side** is wrong, and it is wrong in the direction that
overstates the opposition's numbers (2 of the 4 cited opponents are in fact proponents).

---

## 7. Disposition — which cells are now primary-verified, which stay quarantined

### I-NN2 (the quarantined NN row)

| cell | disposition |
|---|---|
| the doubling **conclusion** | **PRIMARY-VERIFIED** [ABS, S1] — publisher abstract of Nucl. Phys. B185 (1981) 20 |
| **locality** hypothesis | **PRIMARY-VERIFIED** [S4 §1, condition (4)] |
| **translation invariance** hypothesis | **PRIMARY-VERIFIED** [S4 §1, condition (3)] |
| **free / quadratic-in-the-fields** hypothesis | **PRIMARY-VERIFIED** [S4 §1, condition (1); S4 abstract "non-selfinteracting"] — *the load-bearing cell, and it is currently absent from the row* |
| **U(1) phase / charge** hypothesis | **PRIMARY-VERIFIED** [S4 §1, condition (2); S2 abstract "hangs on the existence of the charge"] — *a second, independent escape route the row does not carry* |
| **Hermiticity** hypothesis | **NOT-IN-PRIMARY as a listed condition** — absent from Friedan's list and from Golterman–Shamir's restatement; demote or drop |
| typeset text of the 1981 papers | **UNREACHABLE** (Elsevier paywall; ADS 405; CDS bot-gated). Gap closed at primary strength by Friedan, CMP 85 (1982) 481 |
| "a fieldless substrate is outside the hypotheses" | **STAYS QUARANTINED** — corpus inference from the verified hypothesis list; no primary states it |
| **the generalized-NN exposure (2505.20436)** | **NEW, unquarantined-but-unassessed** — a claimed no-go at arbitrary interaction strength. Not a refutation of the corpus's escape, but the escape no longer terminates the debt |

### I-SMG-1 … I-SMG-6

| row | disposition |
|---|---|
| **I-SMG-1** | statement + conclusion **PRIMARY-VERIFIED**; premise cell needs the repair in §1b (add FREE/quadratic and the U(1)-charge condition; drop or demote Hermiticity). Tag may drop from [KNOWN] to **[PRIMARY-FULL via S4]** |
| **I-SMG-2** | **NOT READ THIS PASS.** Eichten–Preskill (1986) and Golterman–Petcher–Rivas (1993) were not in my claim list and I did not fetch them. **Stays quarantined at [SNIP].** Corroborating context only: S10 §VI describes the Eichten–Preskill phase as one that "fails to support a chiral massless spectrum," consistent with the dossier's characterization but read in a third party |
| **I-SMG-3** | dispute **VERIFIED-AS-LIVE** at primary; Golterman–Shamir both papers **PRIMARY-FULL**. **Kikukawa ×2 CONTRADICTED** — both are constructive, not opposition (§6b). Journal-ref for 2505.20436 **unverified**; the "2026 PRD" claim should be struck or sourced. Row **stays open pending the side-reassignment repair** |
| **I-SMG-4** | Wen statement **PRIMARY-VERIFIED**; conjecture-label referent corrected (§2b). Wang–Wen Spin(10) proposal **PRIMARY-VERIFIED**. **15n cell CONTRADICTED as worded** — the primary's distinction is fermionic-lattice vs bosonic/qubit-lattice, not "requires extra structure" (§3b). Row **stays open pending re-wording**, and the re-wording is *favourable* to the corpus |
| **I-SMG-5** | **FULLY PRIMARY-VERIFIED, the strongest row in the read.** YBX 16-per-generation and the mod-16 regularizability condition verified [ABS]. GEM ℤ₁₆ / per-Weyl-1 / 16-cancels verified [PRIMARY-FULL, §4.3]. Two amendments: (i) the constraint is on the **total** count, so soften "generation by generation"; (ii) **add the primary's ν_R-Majorana-mass caveat sentence** — it is what makes the corpus's exact-B−L structure load-bearing rather than coincidental |
| **I-SMG-6** | **NOT READ THIS PASS** — the constructive-evidence sources (Zeng et al. 2022, Ayyar–Chandrasekharan, Butt–Catterall et al., Razamat–Tong) were not in my claim list. **Stays quarantined at [SNIP].** Note that S10 (Golterman–Shamir 2505.20436) argues at length that "the lessons that can be drawn from two-dimensional models" are limited (abstract) — which bears directly on how much I-SMG-6's 1+1D existence proof is worth for the 3+1D case |
| **§3(D) / OI-2 (N68)** | **the Dai–Freed-covers-discrete-symmetries premise is PRIMARY-VERIFIED and then some** (§5e): the ℤ₃ constraint (Σ s_i ≡ 0 mod 9) and the Spin^c−ℤ_n η-invariant are explicit in GEM §4.1/§4.2/§4.4 + App. C. Two riders: mixed anomalies between Chinese-remainder factors are not automatically covered; and a ℤ₃ embedding in an anomaly-free U(1) discharges the item for free (Ω^{Spin}_5(BU(1)) = 0) — **try that first** |
| **proposed OI-3 (new)** | Wang–Wen's falsifiable bosonic-substrate condition — no gauge-neutral fermionic bound states; the SM gauge group alone is insufficient for a qubit model (§3c). Not carried by any existing row. **Escalated to the adjudicator** |

---

## 8. Summary for the adjudicator

**Forecast met and exceeded.** Claims 2–5 verified at primary (three at PRIMARY-FULL, one at
ABS). Claim 1 verified at **PRIMARY-FULL** — not via a 1981 scan, which is genuinely
unreachable, but via Friedan's independent CMP proof, which states the hypotheses as a
numbered list and is freely hosted by the author. Claim 6 verified well past abstract level.

**Three repairs the dossier owes**, in descending severity:
1. **I-SMG-3 — Kikukawa is on the wrong side, twice.** Both cited Kikukawa papers are
   constructive attempts, and one is explicitly cited by Golterman–Shamir as an attempt to
   explain away the negative result. The dispute is real; the roster is wrong.
2. **I-SMG-4 — the 15n cell is contradicted as worded**, and the true statement
   (fermionic-lattice vs bosonic/qubit-lattice) is *better* for a bosonic substrate.
3. **I-SMG-1 — the premise cell omits the hypothesis the whole escape turns on** (free /
   quadratic), and lists one (Hermiticity) that the primaries do not.

**One strengthening:** GEM's own caveat — that a Majorana ν_R mass breaks the ℤ₄ and leaves
15 massless fermions — is the sentence that makes I-SMG-5 a non-trivial consonance rather
than a numerical coincidence.

**One new exposure and one new open item:** Golterman–Shamir's generalized no-go (2505.20436,
revised 2026-01) means "solitonic matter, so NN's free-field hypothesis is not instantiated"
no longer closes the debt; and Wang–Wen's no-gauge-neutral-fermionic-bound-state condition is
a falsifiable structural test on bosonic-substrate models that no row currently carries.

**Nothing banked. No file edited but this one.**
