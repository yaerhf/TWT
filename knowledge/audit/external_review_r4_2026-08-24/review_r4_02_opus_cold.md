# Referee report — *TWT-Core: A family of substrate theories, what it derives, and its first candidate*

**Reviewer note on method.** I re-derived every algebraic claim in §2 from scratch in my own Clifford-algebra code rather than trusting the paper or its engine, then separately cloned the repository and ran the advertised suite. Where I say "verified," I mean independently verified. Where I say "not checkable," I say so.

---

## 0. Summary verdict

**The mathematics is correct. The claim structure is mostly honest. The physics gap is much larger than the paper's tone conveys, and there are three specific technical problems the paper does not address at all — two of which, if they hold, kill the published candidate independently of the two wounds it already confesses.**

Concretely:

- **Every algebraic claim I checked in §2 is true.** Not approximately, not modulo convention — true. This is unusual for a paper of this type and should be said first.
- **§2.5's D4 result is genuinely correct, non-trivial, and independently valuable.** I verified it by direct computation. It is the single most publishable thing in the paper and it is buried in a subsection of a framework paper.
- **The self-auditing apparatus is real, not decorative.** The gated primitives really do raise. The tier tags really do distinguish "computed" from "assigned." I tried to catch the paper overstating its own engine and could not.
- **But**: three unaddressed no-go problems (§2 below), a prior-art omission that materially affects the novelty claim (§4), and a separator (§3.1) that does not do the job it is advertised to do (§3.3).

The paper's own closing line — "we would rather be shown wrong on a specific claim than credited on a general one" — is taken at face value below.

---

## 1. What I verified, and what passed

### 1.1 Independent algebra checks (my code, not yours)

| Claim | §  | Result |
|---|---|---|
| γ⁰=e₄, γʲ=e₄eⱼ satisfy Cl(1,3) Dirac relations, η=diag(+,−,−,−) | 2.2 | ✅ Confirmed. (γ⁰)²=+1, (γʲ)²=−1, all anticommutators vanish |
| Cl(4,0) ≅ Cl(1,3) ≅ M₂(ℍ); Cl(3,1)≅Cl(2,2)≅M₄(ℝ) | 2.2 | ✅ Correct standard classification |
| B̃·e₄·B = ±e₄; e₁₂₄,e₁₃₄,e₂₃₄ → +e₄; e₁₂₃ → −e₄ | 2.1 | ✅ Confirmed exactly |
| e₁₂₄·e₁₃₄·e₂₃₄ = e₄ | 2.1 | ✅ True — **but order-dependent**, see §5.1 |
| I₄²=+1, dim Λ²₋(ℝ⁴)=3 | 2.3 | ✅ Confirmed; eigenvalues (+1,+1,+1,−1,−1,−1) |
| [Kᵢ,Kⱼ]=−εᵢⱼₖJₖ (Thomas precession as a closure sign) | 2.2 | ✅ Confirmed for all three pairs |
| so(4) 3-dim subalgebras = exactly {SD, ASD, diagonal} | 2.4 | ✅ Correct (Goursat argument is sound; SD/ASD structure constants have opposite sign, so no handed mixture closes; {e₁₄,e₂₄,e₃₄} indeed fails to close) |
| D4: degree-4 invariant space 1-dimensional, spanned by (k²)² | 2.5 | ✅ **Verified numerically.** Σ(k·r)⁴/(k²)² over the 24 D4 roots: spread = **0.0 exactly**. Degree 6: spread = 5.76 (anisotropic). Simple cubic at degree 4: spread = 1.45 (anisotropic) |
| Q_p + Q_e = 0 identically in c | 2.1 | ✅ Both brackets vanish separately, confirmed symbolically |

**On the "dimension eight" claim in §2.5**, which reads like an error on first pass: it is not. Polynomial degree 6 in the dispersion ↔ operator dimension 8 in LV-EFT counting; polynomial degree 4 ↔ dimension 6. The statement is internally consistent and correct under the operator-dimension convention. I flag it because a referee will trip on it — **add one clause naming the convention.**

### 1.2 Repository and suite

`git clone` → `pip install -r requirements.txt` → `python twt_test.py`:

```
ALL 490 CHECKS PASSED across 10 modules.
```

Runs clean, no environment fiddling. I then tested the specific honesty claims:

- `alpha_em_value()` → raises `GatedError` ✅
- `texture_tetrad()` → raises `UnderivedError` ✅
- `qcd_collider_phenomenology()` → raises `UnderivedError` ✅
- `weak_su2_menu_exhaustion()` returns the classification *with* its conditioning premise stamped ENDORSED and its empirical leg named ✅
- `charge_normalization_anchor_free()` returns the identity *with* P4/P5/P6/P7 individually tagged INPUT vs derived, and explicitly warns "never phrase as engine-checked" on P4 ✅

**This is the strongest part of the submission and I want to be unambiguous about it.** The apparatus is not theatre. I attempted to catch the paper claiming engine support it doesn't have and failed. The `charge_sector_provenance` machine-readable compute/assign split is a genuinely good idea that more programmes should copy.

### 1.3 One unexpected point in your favour

You cite Stueckelberg–Horwitz–Piron as your reference class but not the **Euclidean-relativity tradition** (Newburgh & Phipps 1969; Montanus, *Found. Phys.* 31, 1357 (2001); Gersten, *Found. Phys.* 33 (2003); Almeida 2001), which is a much closer match to §2.2: 4D Euclidean space, proper time as the fourth axis, a lock ("all energy moves at c through 4D"), Lorentz transformations as SO(4) rotations.

That tradition's known Achilles' heel is that **relativistic velocity addition fails**. I checked whether yours inherits that failure. It does not: because you go through the Clifford route, boosts are rotors exp(w·e₁/2) with e₁²=+1, so composition gives cosh/sinh addition, rapidities add exactly, and v = tanh(w) reproduces Einstein addition identically. **Your construction fixes the standard objection to that literature.** That is a real result and you are not claiming it. Cite the tradition and claim the fix.

---

## 2. Three unaddressed problems, in severity order

These are my main substantive objections. None appears in the paper, the negatives ledger index, or the companion as far as I could find.

### 2.1 Nielsen–Ninomiya vs. pick #1 + the §2.4 headline — **most serious**

You want, simultaneously:

- **Pick #1**: the substrate arrangement is a regular D4 lattice.
- **§2.4's headline output**: V−A. Chiral weak coupling. Unpaired left-handed doublets, right-handed singlets.

The Nielsen–Ninomiya theorem says you cannot have both. A lattice fermion action that is local, hermitian, translation-invariant, and has the right continuum limit cannot carry unpaired Weyl fermions; chiralities come in cancelling pairs (doublers). This is not a technicality — it is the central obstruction that has shaped forty years of lattice gauge theory.

The known evasions all cost something you have not paid:

- **Ginsparg–Wilson / overlap / domain-wall fermions** — buy lattice chiral symmetry, but it is a *modified* symmetry (γ₅ D + D γ₅ = a D γ₅ D), not the naive one your §2.4 argument uses, and constructing the operator is nontrivial.
- **Fermi-point / momentum-space-topology evasion** — this is Volovik's route in ³He-A, and it works, but it obtains chiral fermions as low-energy excitations near nodes of a *gapped* spectrum, not as a symmetry of the lattice action. You have not adopted it.

Your §2.4 argument is conducted entirely in the continuum rotation algebra so(4), where the problem is invisible. **The moment you put that algebra on pick #1's lattice, the theorem applies.** As written, §2.4's V−A result and §5.1's pick #1 appear jointly inconsistent.

*What I'd want to see*: either an explicit statement of which evasion the candidate uses, or a demotion of "V−A follows" to "V−A follows in the continuum member; the lattice member owes a Nielsen–Ninomiya evasion." The second is cheap and honest. The current silence is the expensive option.

### 2.2 Topological charge is not exact on a lattice — hits the proton-stability bet

§2.6's absolute proton stability rests on π₃ of the local-state class being ℤ⊕ℤ, with B and L as homotopy invariants "conserved under any smooth deformation."

Homotopy invariance requires **continuous maps**. On a lattice with finite spacing a, a Skyrmion whose core shrinks below a can unwind through the discretization — the configuration leaves the space of admissible maps and the winding number simply is not defined through the transition. This is standard in lattice studies of Skyrmions and in the cosmological texture literature; it is why lattice topological charge requires an admissibility condition to be well defined at all.

So: **"the proton is absolutely stable, at any lifetime" is a continuum statement.** In the published lattice candidate it becomes "stable up to an unwinding rate set by the ratio of the soliton core size to the lattice spacing" — which is a number, which is downstream of the unbuilt kernel, which means the candidate has *no* prediction here rather than an absolute one.

This matters more than the other technical points because §4.2 identifies proton stability as **"the family's one distinctive forward bet against grand unification."** If that bet only exists in the continuum branch, then the published candidate's genuinely discriminating row count drops from four to three, and the flagship prohibition is owed to a member you haven't built.

I note the paper *is* careful that the winding argument "rides the defect class — a preferred direction." It is not careful that it also rides the *arrangement*, which is a candidate pick.

### 2.3 The one-medium Lorentz argument is load-bearing and under-conditioned

§2.5's family-level result — dimension-4 relative-boost LV is structurally zero because all species are defects of one medium — is the paper's answer to Collins et al. (2004). You flag the assumption in a rider: "one substrate assumption that is not engine-checkable — that one medium generates all the radiative corrections, so the induced coefficient really is common to every species."

That is not a rider. That is the entire claim, and §1.1 argues against it in the paper's own voice:

> "a defect has several independent axes on which it can be defective: its winding, its deficit of carrier rotation, an internal rotation perpendicular to the advance, a notch in the amplitude. Collapsing those into one scalar is the recurring error in reading this picture."

Exactly. Different defect species differ along those axes — that is what makes them different particles with different masses. Radiative corrections to a defect's dispersion depend on **how that defect couples to the medium's modes**, and species that differ in winding, amplitude notch, and internal rotation generically couple differently. One medium does not imply one correction; it implies one *source* of corrections with species-dependent vertices.

Getting a universal shift requires a further symmetry argument — something like a Ward identity forcing the leading correction to be proportional to a universal quantity independent of the defect's internal structure. **You have not exhibited one**, and I don't think one is obvious.

Until that argument exists, §2.5's dimension-4 protection should be stated as *conditional on a universality claim about substrate self-energies* rather than as following from S4. As it stands, §3.3 line 4 ("two real counterweights exist here") overstates the first counterweight, and Collins et al. is not defused — it is deferred.

---

## 3. Methodological problems

### 3.1 The separator is one clause short

§3.1 is the most intellectually serious thing in the paper and I want to engage with it properly rather than wave at it.

Your criterion: a structural fact is *obtained* rather than *relabelled* when (i) a named substrate feature's deletion breaks it, and (ii) it is independent of the framework's free parameters.

**This detects idle premises. It does not detect reverse-engineered ones**, and reverse-engineering is the failure mode you say you are guarding against.

Concretely: delete the trivector factor of three and neutrality fails. True — I verified it (the residue is nonzero for every c). But if the trivector structure was *selected* because you needed a 3, the deletion counterfactual is guaranteed to fire and tells you nothing. Any premise chosen to produce a result will break that result when removed. Criterion (i) is satisfied automatically by construction.

What separates obtained from fabricated is the classical Lakatosian condition — **excess corroborated content**: does the feature do work somewhere it was *not* selected to do work? Does it have a consequence in a domain not used to fix it, which then checks out?

You already know this, because §4.1 states the deficiency exactly:

> "this is a research programme with one inherited total kill condition, a real set of family-level prohibitions, and **no channel of its own in which agreement would count as evidence**."

That sentence *is* the admission that the separator's clause (iii) is empty. I'd recommend adding the third clause explicitly and re-grading the list against it. My guess is that the "pass cleanly" count goes from 2 to 0, and that this is worth saying — a programme with zero clean passes and a named route to a first one is a coherent, defensible position. A programme claiming two clean passes on a criterion that cannot fail is not.

### 3.2 On "developed with AI assistance under that protocol"

§6.3 discloses this and names the failure mode ("apparatus that carries the texture of rigour while load-bearing calculations remain undone"). Two things follow that the paper doesn't say.

First: if the "independent reviewer in a fresh context, briefed to argue against the submitted conclusion" is a language model, **it is not independent in the relevant sense.** A fresh context decorrelates a model from the conversation; it does not decorrelate a model from itself. Systems of this kind share priors, share failure modes, and are specifically prone to (a) finding elaborate structural frameworks coherent, (b) generating fluent justifications for arbitrary identifications, and (c) producing the exact texture-of-rigour artefact you name. The referent checker and coherence keeper have the same problem. Your protocol's blind spot sits precisely where it believes it has a guard.

Second, and more usefully: this is fixable and cheap. **The three problems in §2 above are all things a human lattice field theorist would raise in the first ten minutes.** None required deep engagement — Nielsen–Ninomiya is the first thing anyone with lattice background thinks when they see "lattice substrate" and "V−A" in the same document. That your protocol did not surface them, across a corpus of this size and 490 checks, is the measured evidence about the protocol's coverage. I'd treat it as such, in the negatives ledger.

### 3.3 Ratio of epistemic apparatus to new calculation

Said plainly, because you asked for specifics rather than credit: a large fraction of the prose is doing epistemic-status work rather than physics work. Sentences like "and that is not a defence," "stated once," "said as such," "this paper does not merge them" are load-bearing for your protocol and dead weight for a referee, who wants to know what was computed.

The practical cost is that your best material is invisible. §2.5's D4 result — which is correct, non-trivial, independently checkable, and has a legitimate novelty claim — is a subsection inside a framework paper, wrapped in three premises and a prior-art disclaimer. **No lattice theorist will ever find it there.**

---

## 4. Prior art

### 4.1 Volovik — the significant omission

You situate the family against Stueckelberg–Horwitz–Piron, Furey, and the lattice-isotropy literature. You do not cite **G. E. Volovik, *The Universe in a Helium Droplet* (OUP 2003)** or the associated body of work, and that is the closest existing programme to yours by a wide margin.

Volovik's ³He-A programme obtains, from a substrate: emergent Lorentz invariance, emergent chiral (Weyl) fermions, emergent gauge fields, emergent gravity, topological defects as matter, an "inner observer" who cannot see the substrate's own geometry, and — directly parallel to your §2.4 — **the substrate's own spin degree of freedom perceived by the inner observer as a local SU(2) resembling weak isospin.** It also engages the Lorentz-violation problem extensively and from the same side you do.

This changes several claims:

- "Whose company the family keeps" (§3.4) is materially incomplete. Your decomposition — "their two-time kinematics, plus substrate realism, plus Euclidean signature with the wavefront lock, plus matter-as-defect" — attributes substrate realism and matter-as-defect entirely to your own risk. Volovik has both, with a *worked microscopic model*.
- §2.4's move (weak isospin hosted in the substrate's own rotation algebra) has a precedent that reached a related conclusion by different means, exactly as you say of Furey in §2.3. Same treatment is owed.
- Volovik's route is also an **existence proof for the Nielsen–Ninomiya evasion** you need in §2.1 above. That is a constructive reason to cite him, not just a defensive one.

The Euclidean-relativity tradition (§1.3 above) is a second, smaller omission, and there the news is good for you.

### 4.2 Citation to verify

**Katz & Nográdi, arXiv:2512.10604** — I was unable to confirm this identifier. Please double-check it; a bad arXiv number in the one paragraph where you are conceding prior art is the worst possible place for one.

---

## 5. Specific technical corrections

### 5.1 The "factor of three is a triple product" is a non sequitur as stated (§2.1)

The identity e₁₂₄·e₁₃₄·e₂₃₄ = e₄ is true. Two problems with the use made of it.

**(a) It is order-dependent.** I computed all six orderings:

```
(124)(134)(234) = +e4      (134)(124)(234) = -e4
(124)(234)(134) = -e4      (134)(234)(124) = +e4
(234)(124)(134) = +e4      (234)(134)(124) = -e4
```

Three of six give −e₄. If the argument is meant to be about an unordered configuration of three facets, the sign is not well defined without a further orientation convention, which should be named.

**(b) The inference does not follow.** "Three blades multiply to a unit" ⇏ "each carries one third of the integer charge." Charge is *additive*; blade composition is *multiplicative*. Getting from one to the other requires a homomorphism from the multiplicative blade structure to the additive charge group — i.e. an assignment of the form Q = (1/3)·(facet count)·(winding). That assignment is the physics, and it is entered, not computed.

§2.1's own "What is not derived here" paragraph concedes exactly this ("the values are entered"), and `charge_sector_provenance` marks it machine-readably. So the ledger is right and the *rhetoric* is wrong. **"The factor of three is a triple product" is a sentence that will be quoted against you.** Recommend: "the trivector orbit structure is what makes a three-facet decomposition available; the 1/3 assignment is entered on it."

### 5.2 Stated counterfactual residue (§2.1)

You say deleting the factor of three gives "the residue is 2c ≠ 0." With standard hypercharge normalization (Y_Q = 1/3, Y_lep = −1) I get **−2c/3**, not 2c. The *point* survives untouched — nonzero for every c, both separator clauses satisfied — but the number is wrong or the normalization is unstated. A referee will run this.

### 5.3 sin²θ_W = 3/8 (§5.3)

Two corrections, cutting opposite ways.

**Harder on you than you are**: 3/8 is the tree-level SU(5)/SO(10) value. *Any* scheme in which the SU(2) and U(1) normalizations are unified returns it. Reproducing 3/8 is not evidence for the substrate; it is evidence that you have imposed a unified normalization. §4.4 calls it a place "the Weinberg ratio works because it is a ratio" — that is a statement about dimensional analysis, not about substrate structure.

**Easier on you than you are**: the "33% miss of a five-digit number" is not a well-defined comparison. sin²θ_W(M_Z) = 0.2312 is a *running* quantity at a specific scale. Comparing a scale-free normalization identity to it requires RG evolution, which requires the unbuilt kernel. The honest statement is not "we miss by 33%" but **"no comparison is currently possible; here is the number we would compare if we could run it."** The current framing gives away a number you haven't actually lost.

### 5.4 S2 (meta-time) appears to do no derivational work

§2.2 states outright that the meta-time generator "does not enter this construction at all, and none of the five primitives named below computes with it; the arc is therefore independent of S2." Scanning §2 for where S2 *is* consumed, I find only mass-as-frequency-in-meta-time (§1.1) — which is a picture, not a derivation.

There is also an unresolved algebraic question. If τ₅'s direction squares to −1, the natural home is Cl(4,1) or a similar extension. You work in Cl(4,0) throughout, where every generator squares to +1. **Where does the −1 live?** The paper does not say.

By your own charter rule — "a theory that drops any one of them is a different theory" — S2 is carrying full axiom cost. §3.2 books it as one of eight structural commitments against the incumbent's ~10. An axiom that costs and does not produce should either be shown doing work or demoted to §1.3's endorsement list, which would improve your own accounting.

### 5.5 The gauge sector — the gap the paper under-weights

What §2.4 delivers is a **global** SU(2) label with the right chirality structure. The Standard Model's electroweak sector is a **gauge** theory: W± and Z with specific masses and couplings, a Higgs mechanism, and precision electroweak fits confirmed at the per-mille level. None of that is derived, and §4.4's "field-reclamation debt" names gauge structure as possibly un-reclaimed.

More striking is §3.1's parenthetical: "colour is not a gauge group in this family at all." That is stated in passing as a reason one entry is "partial," and it is enormous. QCD is confirmed by α_s running across two decades in Q, jet production rates, DIS scaling violations, and lattice hadron spectroscopy. `qcd_collider_phenomenology()` raising is honest, but the consequence is that the theory currently says nothing about the most quantitatively verified non-QED sector of particle physics — while §5.2 books Skyrme-model hadron masses as "calibration performance."

Those numbers (936.4 MeV, 1229.8 MeV, the 293.4 MeV splitting) are the Adkins–Nappi–Witten results from 1983, obtained by fitting f_π and e to exactly those two masses. You say so. But a reader skimming §5.2's table sees four rows of impressive-looking agreement and one line of disclaimer. **The right presentation is that this sector currently inherits the Skyrme model's performance and adds nothing to it**, which is a defensible position honestly stated, rather than a table that reads as calibration success.

---

## 6. What I would do next, in priority order

1. **Extract the D4 result and publish it separately.** *"Point-group protection of Lorentz invariance fails at dimension six for hypercubic lattices and holds for D4"* is a short, correct, checkable paper for a lattice or LV-phenomenology venue. It stands entirely without the substrate framework. It is the one piece of this corpus that a working physicist will cite. Right now it is invisible.

2. **Address Nielsen–Ninomiya explicitly** (§2.1), even if the answer is "the lattice member owes this and hasn't paid." A named unpaid debt is your own method; this one is missing from the ledger.

3. **Re-condition §2.5's dimension-4 result** on the substrate-self-energy universality claim, and either exhibit the Ward-type argument or book the universality as a premise at full weight (§2.3).

4. **Add clause (iii) to the separator** — excess corroborated content — and re-grade the ten. Publish the new grade even if it is 0/10 clean, with §4.1's higher-order-interference channel named as the route to a first.

5. **Cite Volovik**, and cite the Euclidean-relativity tradition while claiming the velocity-addition fix (§1.3) that the Clifford route buys you and that tradition lacks.

6. **Fix §2.1's rhetoric** on the triple product, and the −2c/3 residue.

7. **Get a human lattice field theorist to read §2.4–§2.6 and §5.1.** One afternoon. Nothing in your protocol substitutes for it, and §2's three problems are what an afternoon buys.

---

## 7. Closing assessment

The paper asks to be judged on whether its debts are named, in-principle payable, and being worked, and grades itself PARTIALLY SUPPORTED, NOT CONFIRMED. On my reading that self-grade is close to right but slightly generous, for three reasons that are all fixable:

- **Two debts are unnamed** (Nielsen–Ninomiya; lattice topological-charge non-conservation) and both sit under the published candidate rather than the family.
- **One named debt is under-weighted** (substrate self-energy universality, which is the whole of §2.5's family-level protection rather than a rider on it).
- **The separator that licenses the "two clean passes" claim cannot fail**, so the headline economy result is unsupported by its own criterion.

Against that: the algebra is correct throughout, which I did not expect and which matters. The D4 result is real. The gating apparatus is real and I could not catch it lying. The Clifford construction genuinely repairs a known defect in the Euclidean-relativity literature, which you haven't noticed you did. And the paper's own §5.4 — "a family that has not yet said a number cannot be wrong about one" — is a sentence very few authors in this reference class would write.

The programme's central problem is unchanged and is the one you state: every magnitude waits on an object nobody has built, and until it exists there is no channel in which agreement counts as evidence. Everything above is about making the *structural* half honest enough to be worth the wait.
