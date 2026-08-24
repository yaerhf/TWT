# META-OBSERVER VERDICT — applied round-4 batch (starved pass)
**Role:** twt-meta-observer · **Date:** 2026-08-24 · **Model class:** Fable (dispatcher to note cross-class rule for arbitration weighting)
**Diet:** read ONLY the eight named passages in `TWT_core_paper.md` / `TWT_foundational_paper.md` as a fresh reader; no batch report, no merge record, no adjudications, no diff. Independent checks: sympy arithmetic, engine/ledger greps, Crossref REST ×6, arXiv ×2, one full primary-text read (Volovik cond-mat/9902171 pp. 1–10).

**Diet incidents, reported for the record.** (i) A grep for the §1.2 S2 figures incidentally returned two one-line summaries from `ADJUDICATION_R4_OPUS_2026-08-24.md` (forbidden); the file was not opened, and the claim was verified instead against the pre-round governing record `axiom_arc_2026-08-23/PROBE_S2_2026-08-23.md`. (ii) A grep for "double-billed" returned one hit inside `BATCH_APPLY_REPORT_2026-08-24.md` with the line content omitted by the tool; not opened. (iii) The environment auto-injects git commit summaries; every verdict below rests on my own reading and my own computations/primaries, not on those summaries.

---

## (a) Core §3.1 — the separator and its graded table

**REFERENT:** a three-clause criterion for distinguishing structural facts a theory *obtained* from facts it *relabelled*, applied to the family's own list of ten, with pass counts on both the premise (input) and result (output) sides.
**WHAT THE WORLD IS LIKE HERE:** excess content (novel-domain consequence) is the classical Lakatos/Popper demand; a criterion that cannot fail against its own list is worthless, so the grading must be checkable entry by entry.

- **Arithmetic (checked):** 2+4+2+1+1 = 10; 10 − 1 collapsed − 1 struck = 8 distinct — consistent. Third clause: 0/10 empirical, 3 structural sharing one root → 2 independent — internally consistent.
- **Ledger cross-check (computed):** `TWT_COMPARATIVE_LEDGER.md:1994` — "`CONVOLUTED` = 0, both demotion slots empty" — the §3.1 zero-convoluted claim is backed verbatim. The DOUBLE-BILLED / UNDER-BILLED categories are real instrument verdicts with multiple recorded instances (ledger lines 93, 446, 486, 515, 702, 708, 746, 865, 877). The exact campaign count "five... and one" is plausible but not itemized by me — UNVERIFIED-detail, not a finding.
- **F2 FINDING (wording layer):** §3.1 line 873–874 states **"the hydrogen-neutrality bound is the datum the construction calibrates on."** §2.1 line 312–313 states the identity **"turns the `10⁻²¹` neutrality measurement from the datum that calibrates the theory into a test of it."** One measurement, two sections, verbatim-opposite roles. The engine draws the boundary itself: the entered datum is the **nucleon anchor `(Q_p, Q_n) = (1, 0)`** (a parameter of `charge_assignment_from_anchor`), not the hydrogen-neutrality bound, and `Q_p + Q_e = 0` then holds identically in `c`. §3.1's **score** (zero empirical passes) survives on the correct ground — the consequence lands in the same domain whose data fixed the anchor and P4–P7, so it cannot count as clause-(iii) excess content — but its stated ground misnames the calibrating datum. **Repair:** replace the sentence with the same-domain ground; do not touch the score.
- F4 both directions: the harsher half is reported first, the tail is stated as a tail, and the "coherent position stated honestly" sentence claims no more than the counted pairs. No inflation found; no under-claim found.

**Verdict (a): REFERENT-DRIFT — wording layer only; content layer CLEAR.** The finding is textual (two verbatim sentences); the referent identification is engine-grounded, so graded COMPUTED-adjacent rather than ARGUED.

## (b) Core §2.4 — the weak-arc fences, including the fourth fence

**REFERENT:** a computed classification of the 3-dim Lie subalgebras of `so(4)` closing the weak-host menu, with fences stating what the result is a result *about* — labels and selection rules of a state-carried label, not a gauge boson and not a chiral spectrum.
**WHAT THE WORLD IS LIKE HERE:** Goursat over two simple `su(2)` factors does return exactly {factor, factor, graph-of-isomorphism} at dimension three; and any lattice field theorist will reach first for Nielsen–Ninomiya.

- Citations verified at Crossref: Nielsen & Ninomiya, *PLB* **105**, 219–223 (1981), "A no-go theorem for regularizing chiral fermions"; Friedan, *CMP* **85**, 481–490 (1982), "A proof of the Nielsen-Ninomiya theorem". Exact.
- The fourth fence's logic is the honest form: not "we evade the theorem" but "the hypotheses have no referent, **and** no chiral spectrum has been exhibited either, so the debt transforms rather than discharges" — a two-sided statement, with the field-reclamation debt named.
- **F3 note (not a finding):** Golterman & Shamir, arXiv:2505.20436, generalize the no-go to **interacting** lattice theories of arbitrary strength (verified at arXiv) — so "free quadratic fermion action" characterizes the cited 1981 theorem correctly but not the current theorem family. The fence's conclusion is **robust to this**: the generalization still quantifies over fundamental lattice fermion fields, which this substrate does not define. The closing sentence "owes one of its known evasions" would be sharpened by noting those evasions (SMG) are themselves newly constrained.
- F1: the ASD-mirror claim is witnessed on three inequivalent reflection vectors including a non-basis one — the genericity of the witness is addressed in the text itself. The right-handed-singlet datum carries its reversal clause in the same sentence.

**Verdict (b): CLEAR (both layers), with the F3 currency note above.**

## (c) Core §2.5 / §3.3 — one-medium universality

**REFERENT:** why defects of one medium share one light cone (killing dimension-four relative-boost violation), what a D4-lattice arrangement adds (anisotropy pushed to dimension eight), and what neither reaches (the isotropic dimension-six residual).
**WHAT THE WORLD IS LIKE HERE:** the Collins et al. fine-tuning obstacle is real and cited correctly (*PRL* **93**, 191301 (2004) — verified); and the D4/F4 rotational improvement is established lattice field theory, not this programme's result.

- Mathematics checked: `|W(F4)| = 1152`, invariant degrees `{2,6,8,12}` — hence degree-4 invariants span `(k²)²` alone and the degree-6 space is two-dimensional; the simple-cubic counterexample (`Σk_i⁴` at degree 4) is correct.
- **F3 discharged in the text itself and verified by me:** Neuberger, *PLB* **199**, 536–540 (1987), "Spinless fields on F4 lattices" — exact at Crossref. Katz & Nográdi, arXiv:2512.10604, "QCD on the 16-cell honeycomb" — verified live (Dec 2025); note for the record that the 16-cell honeycomb's vertex set **is** the D4 lattice, so the cite is apt even though the paper's title does not say D4/F4. The residual novelty claim is hedged ("appears not to have carried the observation") — acceptable.
- The universality premise is stated **against interest** — the family's own multi-axis defect picture argues against a universal coefficient, and the nearest worked substrate programme (Volovik) is cited as reaching the opposite conclusion, which my primary read confirms in kind (noncovariant contamination, species-dependent behaviour: cond-mat/9902171 §III.F).
- §3.3 line 4 restates §2.5's conditioning exactly (theorem vs conditional defusal, neither reaching the dimension-six residual, 3–9 orders). No cross-section drift found here — the pair is the model of what §3.1's pair fails at.
- Wording-layer note only: §2.5 ¶1 asserts "structurally zero" two paragraphs before its universality condition; same-section fence, acceptable.

**Verdict (c): CLEAR (both layers).**

## (d) Core §2.6 — proton stability and B−L

**REFERENT:** one conservation law (`B − L` from two independent `π₃` windings plus the anomaly arithmetic) yielding three prohibitions, with sources and conditions itemized.
**WHAT THE WORLD IS LIKE HERE:** `π₃(SO(4)) = ℤ ⊕ ℤ` is correct; a double cover is an isomorphism on `π₃` (so the `ℤ₂`-clause blindness is right); and `ΔB = ΔL = 3` at three generations is indeed the incumbent's own sphaleron selection rule.

- **F2 (checked in the engine):** the "own lattice flows have recorded unwinding events" and "deficit falling as the inverse square" sentences are backed: `twt_candidate_v3.py:10344/10626` (two recorded unwinding events, under-resolved core, reproducible-on-demand, harness-checked at `twt_test.py:3237-3239`) and `twt_candidate_v3.py:9798/10288` (`deficit ~ 1/ρ²` at ρ = 2/3/4, extrapolating to 1). The paper's self-report of its own adverse data is accurate.
- **F4 attacked and not sustained:** the bullet "**The proton is absolutely stable in the smooth sector**, at any lifetime" is the passage's sharpest sentence, and the grainy-member paragraph two paragraphs later conditions it ("exact in a continuum member and carries a resolution condition in every grainy one... does not compute the unwinding rate of the member it endorses"). No verbatim sentence + contradicting number exists — the fence is in-passage and the "smooth sector" qualifier is in the same sentence. **Wording-layer note:** a reader quoting the bullet alone will over-read the *endorsed grainy* member; the "distinctive forward bet against grand unification" is crisp only in the continuum member. Worth one clause at the bullet ("— exact in a continuum member; see below"), not a finding.
- The non-canonical-splitting residue and the monopole re-attack handle are stated as such — the negatives discipline observed inside the paper body.

**Verdict (d): CLEAR (both layers), with the quotability note.**

## (e) Core §3.4 — kinship paragraphs

**REFERENT:** three lineage claims — SHP two-time tradition, Volovik's vacuum-as-medium programme, and the small Euclidean-SR literature — each with corrections binding both directions.
**WHAT THE WORLD IS LIKE HERE:** these literatures exist and say specific things; the risk is a kinship sentence that claims more of the primary than the primary contains.

- **Volovik sentence VERIFIED AT PRIMARY** (cond-mat/9902171, same author/content as the cited book, read in full pp. 1–10):
  - "doubly degenerate through the ordinary nuclear spin" → §III.H: *"the Fermi point... is doubly degenerate owing to the ordinary spin σ of the ³He atom"*. ✓
  - "local and dynamical SU(2) gauge field... Yang–Mills... atomic spin in the role of weak isospin" → Eq. (25) and *"acts on the chiral quasiparticles as SU(2) gauge field... the ordinary spin of the ³He atoms plays the part of the weak isospin... also dynamical and in the leading logarithmic order obeys the Maxwell (actually Yang-Mills) equations"*. ✓
  - "coupling equal to the emergent electromagnetic one" → Eq. (25) carries the **same** `e` on `A_μ` and `σ_α W_μ^α`; supported at the primary at the induced-action level. ✓
  - Limit 1, degeneracy-not-chirality → §II.C.3: *"the conventional spin of the ³He atom is responsible for the degeneracy, but not for chirality, and thus plays the part of the isospin"* — the paper's limit sentence tracks the primary clause-for-clause. ✓
  - Limit 2, not-perfect → §III.F: *"³He-A, with its given physical parameters, is not a perfect model for quantum vacuum"*; zero-charge (screening) effect §III.E; massive analogue modes §III.D. ✓
  - "SM node marginal, halves cancelling" → consistent with the primary's `N₃ = ±1` by chirality and the SM's Fermi points at one origin; the word "marginal" is the book's — consistent-in-kind, not verified verbatim here. The inner-observer scoping sentence likewise: consistent in kind with the 1999 paper, verbatim source is the book (UNVERIFIED-detail, not a finding).
- SHP corrections: the mass-*squared* frequency caveat is correct for the `K = p^μp_μ/2M` generator; the twenty-eight-year biennial series is arithmetically right for IARD (1998→2026). The corrections run **against** the kinship — the direction honesty demands.
- Third kinship: the circularity remark **computed** (sympy): `tan(θ₁+θ₂) = (v₁+v₂)/(1 − v₁v₂)` — wrong-sign denominator, unbounded, periodic; and §2.2's vector-generator hyperbolic route is the correct contrast. The passage explicitly declines to attribute the circular reading to any particular paper — no straw-man F3.
- The self-directed correction ("measured that route closed on its own substrate") is engine-backed: the spectral-node probe in `twt_candidate_v3.py` (~4738 ff.) runs the real-symmetry-class test **with a mandated synthetic-Weyl failure mode** — the instrument is calibrated, not just pointed.

**Verdict (e): CLEAR (both layers).** This is the batch's strongest passage: every checkable clause of the kinship sentences survived contact with the primary.

## (f) Core §2.1 — the charge-pattern prior-art clause

**REFERENT:** crediting Pati–Salam 1974 as the closest group-based cousin of the 3+1 arithmetic, and narrowing this family's claim from uniqueness-of-possession to distinctiveness-of-price.
**WHAT THE WORLD IS LIKE HERE:** *Phys. Rev. D* **10**, 275–289 (1974) is literally titled "Lepton number as the fourth 'color'" (verified at Crossref, with the 1975 erratum).

- The clause attributes to the 1974 paper exactly its title content (lepton number as the fourth colour value; the four-colour group), correctly defers the **name** `B − L` to "later usage," and bills the scheme's costs as the enlarged group, breaking sector, and experimentally constrained quark-lepton (leptoquark) vertices. It does **not** attribute a no-proton-decay property to the 1974 paper — the right restraint, since the primary's decay structure is branch-dependent. F3 CLEAR.
- Soft observation, not a finding: "the only member of that class that furnishes it without buying a group" is a uniqueness claim over an informally bounded class; it is fenced by "of that class" and I know no counterexample, but it is the kind of sentence a future survey could falsify. Acceptable as worded.

**Verdict (f): CLEAR (both layers).**

## (g) Core §1.2 — the "On S2" note

**REFERENT:** that S2's negative-square clause places the substrate's one global phase (a central complex unit), not the observer's Lorentzian signature, and that its consumption is measured, not argued.
**WHAT THE WORLD IS LIKE HERE:** `Cl(4,0) ≅ M₂(ℍ)` is central simple over ℝ (centre = scalars — no central `−1`-square exists); `Cl(4,1) ≅ M₄(ℂ)` has centre ℂ; and for `E = e₁₂₃₄₅`, `E² = e₅²` (reorder sign `(−1)^{10} = +1`, spatial squares `+1`) — **computed**, checks.

- The "eighteen primitives and four of the suite's ten modules" experiment is a real measured pre-round record: `PROBE_S2_2026-08-23.md` §2.2 — 16 main + 2 companion movers = 18, four named modules red (`twt_algebra`, `twt_observer_qm`, `twt_matter`, `twt_cosmo`), and the charge/weak/EM/hadron/spectra modules untouched — which is exactly the note's "nothing in §2 does." F2 CLEAR.
- F4 two-sided: the note simultaneously *denies* S2 the signature role (narrowing) and *asserts* its earned cost outside §2 (widening, with the measurement to back it) — both sides stated, both backed.

**Verdict (g): CLEAR (both layers).**

## (h) Dossier §C.1.6 — the moving-case paragraph (de Broglie / unrolling)

**REFERENT:** what a uniformly moving electron-defect *is* — the rest-frame meta-time clock tilted into space by a boost, read inside-frame as the de Broglie phase wave, with the winding boost-invariant.
**WHAT THE WORLD IS LIKE HERE:** virtually nothing in the universe is stationary and the best available case is uniform linear motion — this paragraph is precisely the generic-witness case this program's history demanded; and the phase-wave with `v_phase·v_group = c²` is de Broglie's own 1924 picture.

- **Arithmetic COMPUTED (sympy):** `(E,p) = m(cosh ζ, sinh ζ)` gives `E² − c²p² = m²c⁴` exactly; `ω = E/ℏ, k = p/ℏ` gives `ω² − c²k² − ω₀² = 0` identically; and `v_p·v_g = (ω/k)(c²k/ω) = c²` identically from that dispersion. The claim "follows identically" is exact.
- The paragraph's own referent-fence is the correct one: "a **reading** of the mass shell in the register of a defect's own phase, **not a second derivation** of the dispersion relation" — it refuses the double-count a less careful writer would have banked. F4 CLEAR in both directions.
- Topology survival: a boost is continuously connected to the identity and preserves the boundary condition, so it cannot change the `π₃` class — sound, and the "the electron becomes a wave is the wrong picture" sentence is the correct ontology statement given S4.
- F5 CLEAR: phase-unrolling vs envelope-spreading (`λ̄_C` core vs `a₀` orbital) are explicitly separated as two axes — the exact layer-slip this mode exists to catch is pre-empted in the text.
- F3: the object is named the de Broglie wave; no novelty is claimed for the relation. CLEAR.

**Verdict (h): CLEAR (both layers).**

---

## AXES ATTACKED AND ABANDONED (with reasons)

- **F1 on (h):** hunted a non-generic witness; abandoned — the paragraph *is* the generic uniform-motion case, treated at all rapidities by exact boost.
- **F1 on (b):** attacked the accessible-energy quantifier of the RH-singlet datum; abandoned — the reversal clause is in the same sentence.
- **F4 on (d):** attacked "at any lifetime"; abandoned as a formal finding (no verbatim sentence + contradicting number; in-passage fence), retained as a quotability note.
- **F3 on (h):** considered demanding an explicit de Broglie 1924 citation; abandoned — the attribution is in the object's name and no priority is claimed.
- **F2 on (a)'s counts:** attacked the ten-item bookkeeping; abandoned — 2+4+2+1+1 = 10 and 10−1−1 = 8 are consistent, and CONVOLUTED = 0 verified at the ledger.
- **F3 on (e)'s SHP block:** considered auditing the "two proposals by two authors" mass-stability sentence against the SHP literature; abandoned for effort-bounding after the Volovik primary read consumed the F3 budget — flagged UNVERIFIED, not dropped.

## VERDICT: **REFERENT-DRIFT** (one wording-layer finding, §3.1's calibration-datum sentence vs §2.1's test sentence); all other seven sections **CLEAR** at both layers.

**NARROWEST DEFENSIBLE STATEMENT OF THE CLAIM (the batch as a whole):** eight passages each carry in-passage conditioning that matches their computed or primary-verified content; one §3.1 sentence misnames the charge construction's calibrating datum (the entered nucleon anchor `(Q_p,Q_n) = (1,0)`) as the hydrogen-neutrality bound, in verbatim opposition to §2.1, while the zero-empirical score it grounds survives on the correct same-domain ground.

**WIDEST DEFENSIBLE STATEMENT:** the batch's attribution hygiene exceeds what it advertises — all nine externally checkable attributions tested (six Crossref-verified prints, two arXiv items, one full primary-text Volovik read) verified exactly, the Volovik-limits sentence tracking its primary nearly clause-for-clause; and §2.4's Nielsen–Ninomiya fence is robust even against the 2025 interacting-theory generalization it does not cite — a mild UNDER-CLAIM in the fence's favour, recorded here as the sentence the developer may quote: *the no-referent escape survives the strongest currently published form of the no-go, because that form too quantifies only over fundamental lattice fermion fields.*
