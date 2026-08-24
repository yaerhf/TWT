# PRIMARY READ — Volovik, *The Universe in a Helium Droplet* (O5.2 quarantined claims)

**Date:** 2026-08-24
**Worker:** primary-read duty, round-4 external review (`external_review_r4_2026-08-24`)
**Scope:** the two quarantined claims from Opus finding **O5.2** — (a) the inner-observer parallel; (b) the weak-isospin parallel. Import row **I-25** promotion trigger.
**Diet declaration:** deliberately starved of the TWT derivations and of the round-4 adjudication. Everything below is what the primary says. No TWT mapping is asserted anywhere in this dossier.

---

## 1. Sources fetched

| # | Source | URL | Status |
|---|---|---|---|
| S1 | **Volovik, G. E., *The Universe in a Helium Droplet*, author's own full-book PDF** (PDF internal metadata: `title = Book5.Tex`, `author = Grigori Volovik`, `creationDate = 2002-11-27`, Acrobat Distiller; 526 PDF pages) | `http://home.ustc.edu.cn/~gengb/201216/Volovik_The_universe_in_a_helium_droplet.pdf` (2,835,099 bytes, `Content-Type: application/pdf`) | **FETCHED, full text extracted** |
| S2 | Internet Archive scan of the printed OUP edition (`universeinhelium0000volo`; Oxford: Clarendon, 2003; xx + 509 pp.; ISBN 0198507828) | `https://archive.org/details/universeinhelium0000volo` | metadata only — item is `access-restricted-item: true` (lending); search-inside API endpoints returned nothing. **Used for bibliographic confirmation only.** |
| S3 | Internet Archive item `Grigori_Volovik__The_Universe_in_a_Helium_Droplet` | `https://archive.org/details/Grigori_Volovik__The_Universe_in_a_Helium_Droplet` | **DEAD** — the hosted `book.pdf` is a 17,937-byte HTML error stub, not the book. Its two cited upstream links (`http://ltl.tkk.fi/personnel/THEORY/volovik/book.pdf`, freescience.info) are both dead; `ltl.aalto.fi` 301-redirects to the Aalto front page. |

### Pagination convention used

S1 carries the **book's own running heads and printed page numbers**. Verified offset: **printed page = PDF page − 19** (e.g. PDF p. 58 head reads `NORMAL COMPONENT – 'MATTER' 39`; PDF p. 134 head reads `EFFECTIVE SU(N) GAUGE FIELDS 115`). Cross-checked against S1's own back-of-book Index, which independently lists e.g. *"clocks and rods … of inner observer, 40"*, *"Michelson–Morley, 40, 327"*, *"Fermi point … discrete symmetry, 5, 115"* — consistent with the running heads. **All page numbers below are printed-book pages.**

*Caveat on edition:* S1 is the author's pre-publication file (Nov 2002) for the 2003 Clarendon edition. Chapter/section numbers and §-titles are quoted directly and are the primary locator; page numbers should be treated as accurate-to-the-author's-file and near-certain but not independently re-verified against a physical OUP copy.

### Read-depth tags

- **FULL-SECTION-READ** — the complete section text was read verbatim from S1.
- **KEYWORD-SWEEP** — regex sweep over the full extracted book text (1,274,963 chars, all 526 pages) for `weak isospin`, `inner observer`, `ether drift|Michelson`, `SU(2)`, `resembl`, `chiral.*SU(2)`.
- Both claims below rest on **FULL-SECTION-READ** of the named sections, plus a whole-book KEYWORD-SWEEP to confirm there is no contradicting or superseding passage elsewhere.

### Quotation policy

Quotations are held to the minimum needed to verify the contested wording — each under 15 words, each attributed with chapter/section/page. Everything else is close paraphrase with a locator.

---

## 2. CLAIM (a) — THE INNER-OBSERVER PARALLEL

**Verdict: VERIFIED-AT-PRIMARY.**

### Primary locus

**§4.3.2 "External and inner observers", pp. 39–40** (Ch. 4, *Effective theory of superfluidity*, Part I) and its immediate sequel **§4.3.3 "Is the speed of light a fundamental constant?", p. 40**. Both FULL-SECTION-READ. The Index confirms these as the canonical loci (`clocks and rods … of inner observer, 40`; `speed of light … for inner observer, 40, 305`; `fundamental constants … for inner observer, 40`).

### What Volovik actually claims

Volovik erects an explicit **two-observer** scheme. The *external* observer is made of the atoms of the liquid, lives in the "trans-Planckian" **Galilean** world, and uses rigid rods and clocks. The *inner* observer is constituted of the low-energy quasiparticles and lives in the emergent "relativistic" world (§4.3.2, p. 39). Volovik's words: the inner observer is

> "made of low-energy quasiparticles"  — §4.3.2, p. 39

and, decisively for the claim,

> "uses clocks and rods also made of the 'relativistic' low-energy quasiparticles"  — §4.3.2, p. 39

Those instruments are described as **"flexible"** — set by the local acoustic metric — as against the external observer's **"rigid"** ones (§4.3.2, p. 39).

**What exactly the inner observer cannot see.** Volovik names three distinct things, all on p. 40 (§4.3.3):

1. **The motion of the substrate.** The Lorentz–FitzGerald contraction of a quasiparticle rod and the time dilation of a quasiparticle clock are *physical* effects that, in his phrasing, conspire to produce effective special relativity; they therefore

   > "do not allow the inner observer to measure the 'ether drift'"  — §4.3.3, p. 40

   which he glosses in the same sentence as the motion of the superfluid vacuum, and states that a Michelson–Morley-type measurement of massless-quasiparticle speed in a moving "ether" would return a **negative result**.

2. **The anisotropy of the substrate.** The low-energy rods and clocks follow the vacuum's anisotropy and therefore **cannot record it** (§4.3.3, p. 40) — with the concrete number: in ³He-A the external observer finds the "speed of light" running from ~3 cm s⁻¹ to ~100 m s⁻¹ with direction, while every inner observer agrees the speed of light is a fundamental constant.

3. **The substrate itself, as a substance.** Earlier in §4.3.2 (p. 39): for the inner observer the liquid in its ground state is *empty space*; the smooth inhomogeneity of the underlying liquid is read as **effective spacetime**, which "does not reflect the real absolute space and absolute time of the world of atoms" (§4.3.2, p. 39).

**Under what conditions — the scoping, which the primary states explicitly and repeatedly.** The claim is *not* unconditional:

- **Low-energy corner only.** Effective special relativity "emerg[es] in the low-energy corner" (§4.3.3, p. 40); the inner observers are unable to believe the broader picture precisely because they live there.
- **Local measurement only.** "the invariance of the speed holds only if the measurement is purely local" (§4.3.3, p. 40) — extend the measurement over gradients of *c* and *v_s* and the measured speed departs from the local value (this is GR's "coordinate speed of light").
- **The blindness is observer-relative, not absolute.** In §9.2.6 (p. 114) Volovik makes the converse explicit: homogeneous states with different ˆl-direction, hence different vector potentials, are "equivalent for an inner observer, but can be easily resolved by an external observer". He draws the moral for gravity in the same paragraph: if GR is an effective theory, general covariance must be violated at high energy, so metrics equivalent for us become physically distinguishable at high energy.
- **Velocity-limited.** When the flow velocity exceeds *c*, the inner observer cannot remain at rest in the laboratory frame and is dragged by the vacuum flow (§4.3.2, p. 40).

**Corroborating loci found in the KEYWORD-SWEEP** (the doctrine recurs throughout, always in the same form):

- §5.4.1, p. 48 — the effective (Tolman) temperature is what a *local inner observer* measures; the external observer measures the true thermodynamic *T*.
- §7.3.3–§7.3.4, pp. 73–74 — the inner observer "knows only the low-energy excitations" and believes the vacuum energy comes from the Dirac sea and zero-point bosons; the external observer knows there are larger contributions from higher Planck scales, and knows the equilibrium vacuum energy is exactly zero.
- §9.1.5, p. 108 — the inner observer believes spin follows from a fundamental rotation/Lorentz group; the external observer finds spin is *not fundamental* but emergent at the Fermi point.
- §10.3.2, p. 123 — quasiparticle number conservation is "a true conservation law" *for an inner observer*, though anomalous at the quantum level.
- §31.4 region, p. 390 — the particle number *N* (the count of bare ³He atoms) is "the quantity which is missing by an inner observer, but is instrumental for the Planckian physics".
- Ch. 30–32, pp. 400, 428, 430 — two inner observers in split domains "are not aware of existence of their partner"; the inner observer uses rods and clocks made of the same quasiparticles; at *T* = 0 and zero gradients the co-moving inner observer "does not know … whether the liquid is moving or not".

**No contradicting passage was found anywhere in the 526-page sweep.**

### Honest two-sentence summary of what the primary licenses

Volovik states, as a worked and repeatedly-applied feature of his effective-theory programme, that an observer built out of the low-energy quasiparticles measures with rods and clocks made of the same quasiparticles, and therefore cannot detect the substrate's own state of motion ("ether drift"), its anisotropy, or its existence as a substance — reading its ground state as empty space and its smooth inhomogeneity as spacetime. The claim is explicitly **scoped to the low-energy corner and to purely local measurement**, and is explicitly **observer-relative rather than absolute**: an external (high-energy) observer resolves exactly what the inner observer cannot.

---

## 3. CLAIM (b) — THE WEAK-ISOSPIN PARALLEL

**Verdict: VERIFIED-AT-PRIMARY, and stronger than the forecast on the "dynamical" question — with its own scoping, which is about *exactness*, not about dynamism.**

### Primary locus

**§9.3 "Effective SU(N) gauge fields", §9.3.1 "Local SU(2) from double degeneracy", pp. 114–115**, in **Ch. 9, "Effective quantum electrodynamics in ³He-A"** (p. 105 ff.). Set up by **§9.1.5 "Spin from isospin, isospin from spin", pp. 108–109**. Continued in **§9.3.2 "Role of discrete symmetries", pp. 115–116** and **§9.3.3 "W-boson mass, flat directions, supersymmetry", p. 116**. All FULL-SECTION-READ. (The reviewer's guess of "around Ch. 8–9" is correct; the exact home is §9.3.)

### From which degree of freedom does it arise?

**The ordinary (nuclear) spin of the ³He atom — not the orbital, and not the Bogoliubov–Nambu, degree of freedom.** Volovik is careful to separate the three, and to invert the naive assignment:

- The **Bogoliubov–Nambu** "spin" τ̌ is what plays the role of *relativistic spin* for the inner observer, and is what carries **chirality** (§9.1.5, p. 108; §9.1.1, p. 105).
- The **conventional spin** *S_z* = ±1/2 of the ³He atom is what doubly degenerates the Fermi point and therefore "plays the role of isotopic spin in the world of quasiparticles" (§9.1.5, p. 108). The global SO(3)_S spin-rotation group — "actually this is the SU(2) group" — is seen by quasiparticles as an **isotopic** group.
- The **orbital** ˆl degree of freedom is separately the source of the effective *electromagnetic* U(1) field, **A** = p_F ˆl (§9.2, pp. 109–113). Note that a *different* orbital/GUT-style analogy appears at §17.x, p. 184, where ˆl corresponds to the weak-isospin **quantization axis** — that is an r-space defect-topology analogy, a distinct construction, and should not be conflated with §9.3.

Volovik flags the inversion himself back at §7.4.4 (p. 94): Bogoliubov–Nambu isospin plays for quasiparticles the role conventional spin plays for matter, and "later we shall see the inverse relation" — the conventional ³He spin playing the role of the weak isospin.

### Is it a genuine *local* gauge field, and is it dynamical?

**Yes on both counts, per the primary — and this exceeds the "background, not dynamical" forecast.**

The mechanism (§9.3.1, pp. 114–115): each Fermi point in ³He-A is doubly degenerate through the atomic spin (total topological charge *N*₃ = −2); the degeneracy holds only in equilibrium; a perturbation breaks the ℤ₂ symmetry *P* and splits it into two elementary Fermi points with *N*₃ = −1 each, which can then move **separately** (the perturbed A-phase becomes effectively the axiplanar phase). The collective degrees of freedom governing that separate motion are, in Volovik's words,

> "viewed by an inner observer as the local SU(2) gauge field"  — §9.3.1, p. 115

Concretely: perturbing the 4×4 propagator gives `G⁻¹ = τ̌ᵇ e_bᵘ (p_µ − qA_µ − qσᵃW_µᵃ)` (eqn 9.26), where σᵃ is the Pauli matrix for **conventional** spin and W_µᵃ the collective variable coupling to it. Volovik then states, in consecutive sentences (§9.3.1, p. 115):

> "it is the analog of the weak field in the Standard Model"

> "The ordinary spin of the ³He atoms"  …  "viewed by an inner observer as the weak isospin"

and, decisively for the dynamical question:

> "This weak field … is dynamical, since it represents some collective motion"

— of the fermionic vacuum. He then **integrates out the fermions** and obtains a leading-log **Yang–Mills action** (eqn 9.27), and reports that the computed Yang–Mills coupling γ_W "coincides with the coupling constant γ for the Abelian field" of eqn (9.22) — i.e. the "weak" charge is logarithmically screened by the fermionic vacuum. He notes the sign of the running is **opposite** to the SM's: ³He-A shows a **zero-charge (screening)** effect rather than asymptotic freedom, because the emergent SU(2) bosons are not fundamental and their antiscreening contribution is subdominant to the fermionic one.

**Symmetry chain (§9.3.2, p. 116):** `SU(2)_global → ℤ₂ → SU(2)_local` (eqn 9.28), with the pointed generalisation that the first stage is not even necessary — a bare ℤ₂ vacuum symmetry suffices to produce a local SU(2) in the effective theory, and higher discrete groups (ℤ₄, ℤ₂×ℤ₂) would give SU(4) etc. Already at §9.1.5 (p. 109) he previews this: the global spin SU(2) "corresponds to the weak isospin in the Standard Model", and

> "the global SU(2) group gradually becomes a local one"

in the low-energy corner.

### Exact, partial, or suggestive? — the primary's own limits

Volovik states the identification **flatly** in the text (no hedging verb at the point of assertion), but frames the whole construction as an **emergent, approximate, low-energy** one and lists concrete disanalogies. Load-bearing caveats, all from the primary:

1. **The gauge invariance is approximate.** §9.3.3, p. 116 opens: "In the effective theory the gauge invariance is approximate." It is violated by non-renormalisable terms from beyond the log approximation — and as a direct consequence **the W-boson acquires a mass in ³He-A** (from physics beyond the BCS model; within BCS it is a Goldstone boson of a flat direction and massless).
2. **The bosons are not fundamental.** §9.3.1, p. 115: "the SU(2) gauge bosons are not fundamental: they appear in the low-energy limit only."
3. **The effective SU(2) is not the carrier of chirality.** §9.1.5, p. 109, of the spin-rotation group seen as isotopic: "It is responsible for the SU(2) degeneracy of quasiparticles, but not for their chirality." **NOT-FOUND:** the book contains **no claim anywhere in the sweep** that ³He-A's effective SU(2) acts on one chirality only, i.e. no claim that it reproduces the SM's *left-handedness*. Volovik states the SM's chiral asymmetry as SM fact at §12.1, p. 146 ("The group SU(2)_L thus transforms only left fermions"), but does not assert that the ³He-A analogue shares it. **Treat "SU(2)_L specifically" as unverified.**
4. **The host system is explicitly imperfect.** §9.2.4, p. 113: "³He-A is not a perfect system for a complete simulation of RQFT". §10.5.6, p. 134: "³He-A is not a good example of emergent RQFT" — because its Planck-scale hierarchy is the wrong way round (Lorentz violation sets in *below* the natural cut-off), so the bosonic effective action is contaminated by non-covariant terms. Conclusion, p. 462: "liquid ³He-A cannot serve as a perfect model for the quantum vacuum" — it is in the right universality class and "reproduces many fragments" of the SM vacuum, but "the full pattern is missing".
5. **Book-level framing.** Conclusion, p. 461: ³He-A's collective modes are "very similar to gravitational, electromagnetic and SU(2) gauge fields", whose quanta are analogues of gravitons, photons and weak bosons; the stated *reason* for the similarity is **common momentum-space topology** (Fermi points, co-dimension 3), not a shared microscopic mechanism. Introduction §1, p. 5: the SM vacuum "might" belong to the same universality class as ³He-A — and he immediately qualifies that reproducing all SM bosons and fermions needs *several* Fermi points related by discrete symmetries, putting the SM closer to the **planar phase** than to the A-phase.

### Honest two-sentence summary of what the primary licenses

Volovik does claim, in the book's own text and without hedging at the point of assertion, that the ordinary atomic spin of ³He is seen by the inner observer as **weak isospin**, and that the collective mode moving the two split Fermi points independently is a genuine **local, dynamical SU(2) gauge field** — he derives a Yang–Mills action for it by integrating out the fermions and computes its coupling. What the primary does **not** license is any claim that this reproduces the SM's SU(2)_L specifically (chirality is carried by a different, Bogoliubov–Nambu, degree of freedom, and the left-handedness of the analogue is never asserted), nor that the correspondence is exact: the gauge invariance is approximate, the W acquires a mass beyond BCS, the charge screens rather than antiscreens, and Volovik states three separate times that ³He-A is not a perfect or even a good model of the SM vacuum.

---

## 4. Verdict table

| Claim | Verdict | Primary locus |
|---|---|---|
| (a) inner observer cannot detect the substrate's own geometry/velocity because its rulers and clocks are quasiparticles | **VERIFIED-AT-PRIMARY** (scoped: low-energy corner; purely local measurement; observer-relative, external observer *can* resolve it) | §4.3.2–§4.3.3, pp. 39–40; corroborated §5.4.1 p. 48, §7.3.3 p. 73, §9.1.5 p. 108, §9.2.6 p. 114, §10.3.2 p. 123, pp. 390, 400, 428, 430 |
| (b) the substrate's own spin appears to the inner observer as a local SU(2) gauge field "resembling weak isospin" | **VERIFIED-AT-PRIMARY**, and the field is **local and dynamical** (Yang–Mills action derived, coupling computed) — arising from the **ordinary atomic spin**, via ℤ₂-protected Fermi-point double degeneracy | §9.3.1, pp. 114–115 (eqns 9.26–9.27); set up §9.1.5 pp. 108–109; chain §9.3.2 p. 116 (eqn 9.28); mass §9.3.3 p. 116; framing Conclusion p. 461 |
| (b′) the analogue SU(2) is **chiral** / is SU(2)_**L** | **NOT-FOUND** — never asserted; chirality is explicitly carried by a *different* (Bogoliubov–Nambu) degree of freedom | §9.1.5, p. 109 |
| (b″) the correspondence is exact | **CONTRADICTED** — Volovik states the opposite three times | §9.2.4 p. 113; §10.5.6 p. 134; Conclusion p. 462 |

---

## 5. Draft language for §3.4 (conservative)

*Offered as drafting material only. Each sentence is a statement about what Volovik claims, not about any correspondence to our own construction; the mapping is for the §3.4 author to make or decline.*

**For claim (a) — clear to enter, if scoped.**

> Volovik's ³He programme contains a directly comparable observer construction. In *The Universe in a Helium Droplet* (§4.3.2–§4.3.3, pp. 39–40) he distinguishes an "external" observer, made of the liquid's atoms, from an "inner" observer made of its low-energy quasiparticles, whose rods and clocks are themselves built from those quasiparticles and are therefore set by the local effective metric; such an observer cannot measure the "ether drift" — the motion of the superfluid vacuum — nor register its anisotropy, and reads the liquid's ground state as empty space. Volovik scopes the claim explicitly to the low-energy corner and to purely local measurement, and makes it observer-relative rather than absolute: configurations indistinguishable to the inner observer are resolved without difficulty by the external one (§9.2.6, p. 114).

**For claim (b) — clear to enter, if the chirality caveat rides with it.**

> A second parallel appears in Volovik's treatment of effective gauge fields in ³He-A (§9.3.1, pp. 114–115). There the Fermi point is doubly degenerate through the *ordinary* nuclear spin of the ³He atom; perturbing the ℤ₂ symmetry splits it into two elementary Fermi points whose independent motion is carried by a collective variable that couples to that spin as a **local SU(2) gauge field**, with the atomic spin playing the role of weak isospin and the field itself dynamical — Volovik obtains its Yang–Mills action by integrating out the fermions, and finds its coupling equal to the emergent electromagnetic one. Two limits must travel with the citation: the emergent SU(2) governs the Fermi-point degeneracy but **not** the quasiparticles' chirality (which is carried by the Bogoliubov–Nambu index), so Volovik nowhere claims it reproduces the Standard Model's *left-handed* SU(2)_L; and he states plainly that ³He-A "is not a perfect system for a complete simulation of RQFT" (§9.2.4, p. 113), its gauge invariance being approximate, its W-boson massive beyond BCS, and its charge screening rather than antiscreening.

**What must NOT be written into §3.4 on this evidence:**
- that Volovik derives, or claims, the Standard Model's **chiral** SU(2)_L from a substrate spin;
- that he treats the correspondence as exact rather than as a shared **universality class fixed by momentum-space topology**;
- that the inner observer's blindness is absolute rather than an artefact of the low-energy, purely-local regime.

---

## 6. Residual / reproducibility notes

- The extracted full text and the search harness used for the KEYWORD-SWEEP are session-scratch artefacts and were not banked; S1 is re-fetchable at the URL above and the offset rule (printed = PDF − 19) reproduces every locator in this dossier.
- The most-cited "official" free link for this book (`ltl.tkk.fi/personnel/THEORY/volovik/book.pdf`) is **dead**, as is the Internet Archive mirror that points at it. Anyone re-running this read should expect to use S1 or an equivalent mirror.
- Volovik's own arXiv reviews (e.g. *Superfluid analogies of cosmological phenomena*, Phys. Rep. **351** (2001) 195, `gr-qc/0005091`) are the book's precursors and would supply an independent, permanently-hosted second primary for both passages. **Not read in this pass** — flagged as the cheapest available corroboration if a second witness is wanted before promotion.
