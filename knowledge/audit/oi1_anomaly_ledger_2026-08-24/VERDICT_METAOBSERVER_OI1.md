# VERDICT — META-OBSERVER — OI-1 anomaly ledger — 2026-08-24

Role: meta-observer (`knowledge/prompts/meta_observer.md`). Model class: **Opus** (cross-class
requirement — see the independence note at the foot).
Information diet honoured: the derivation was **not** opened. `twt_core.py`, `twt_test.py`, the
commission files and both round-4 adjudications were not read. Everything below is computed from the
claim's own stated table in my own scratch scripts, plus publisher/INSPIRE metadata.

---

## REFERENT (one sentence, for an outsider, written before any computation)

This claim is about one generation of the Standard Model's fermion content and the standard
requirement that a chiral gauge theory built on it be quantum-mechanically consistent — i.e. that the
triangle-diagram (and global) anomalies involving hypercharge cancel between the quark and lepton
columns.

## WHAT THE WORLD IS LIKE HERE

Anomaly cancellation in the Standard Model is not a list of three sums. It is a **closed set of six
conditions** on one generation: `[SU(3)]³`, `[SU(3)]²U(1)_Y`, `[SU(2)]²U(1)_Y`, `[U(1)_Y]³`,
`grav²U(1)_Y`, and the non-perturbative Witten `SU(2)` doublet-parity condition. Two facts about that
set are load-bearing here and are *facts about the world*, not about any framework:

1. **The set is not partitionable by taste.** A spectrum that satisfies some conditions and violates
   another is an inconsistent theory, full stop. "The ledger is satisfied" is a statement that only
   means anything against the complete set.
2. **Given the representation content, the set is nearly rigid.** The four abelian/mixed conditions,
   solved simultaneously for the hypercharges of `(Q, u^c, d^c, L, e^c)`, have essentially a unique
   solution — the Standard Model's — up to overall normalization and the `u↔d` relabel. This is a
   published theorem (Geng–Marshak 1989; Minahan–Ramond–Warner 1990), and I reproduce it below.
   **This is the fact that decides both findings**, because the condition the claim omits is
   precisely the one that supplies the rigidity.

---

## LAYER 1 — THE TABLE-ARITHMETIC LAYER: **CLEAR**

Independently recomputed from the claim's stated table alone, in exact rationals, in the all-left-handed
Weyl basis (`Y → −Y` on conjugation), `T(2) = 1/2` with colour multiplicity carried:

```
[SU(2)]^2 U(1)_Y  = 0        SU(2) doublets = 4  (even -> Witten OK)
[U(1)_Y]^3        = 0        counts = 15 gauged + 1 sterile = 16
grav^2 U(1)_Y     = 0
```

All three sums vanish; the parity and the counts are as stated. Conventions check out against the
literature objects: the table is the SM in the `Y = 2(Q − T₃)` normalization
(`Q(e_R) = −1 = Y/2 ⇒ Y = −2` ✓, `u_R: 2/3 ⇒ Y = 4/3` ✓, `d_R: −1/3 ⇒ Y = −2/3` ✓,
`Q_u = 1/2 + 1/6 = 2/3` ✓); the sums are homogeneous of degree 1 and 3, so the normalization choice
cannot affect vanishing. The 15 gauged states (2+6+1+3+3) match the SM's 15 per generation exactly,
with no `ν_R` among them — internally consistent with the sterile state being listed separately.
**No arithmetic finding. The tier as claimed — exact arithmetic over an entered table — is honest.**

---

## LAYER 2 — THE CLAIM-WORDING LAYER

### F1 non-generic witness : **FINDING**

The one-generation witness is *generic for the generation family* — anomalies are additive, so `N`
generations give `N × 0`. That part is fine and I do not contest it.

The non-generic witness is the **rigidity sub-claim**: *"Five counterfactual slot flips ... each break
the ledger."* Five hand-chosen points are offered as evidence of the ledger's discriminating power over
a **continuous five-dimensional** deformation space. I checked all five: every one of them is caught by
the three listed sums — so the sample is entirely inside the detected region. A generic probe is not.
Fixing `Y(Q) = 1/3` and solving the claim's three sums as a system, there is a **one-parameter
continuum** of hypercharge tables that pass all three and are nonetheless anomalous. Sampled members:

```
 s=b+c      Y(u^c)       Y(d^c)      Y(e^c)   [SU2]^2U1  grav^2U1   [U1]^3   [SU3]^2U1
 -0.667    0.666667   -1.333333     2.0000        0          0         0      0   <- the SM member
  0.250    1.111111   -0.861111    -0.7500        0          0         0     0.9167
  1.000    2.264709   -1.264709    -3.0000        0          0         0     1.6667
  5.000   11.041439   -6.041439   -15.0000        0          0         0     5.6667
```

and a clean **rational** member, so this cannot be dismissed as an irrational-branch artefact:

```
Y(Q)=1/3   Y(u_R^c)=10/9   Y(d_R^c)=-31/36   Y(L)=-1   Y(e_R^c)=-3/4
   [SU(2)]^2U(1)_Y = 0 , grav^2U(1)_Y = 0 , [U(1)_Y]^3 = 0     ALL THREE LISTED SUMS PASS
   [SU(3)]^2U(1)_Y = 11/12                                      ANOMALOUS
```

*Rule applied:* the witness must be generic for the claim's scope, or the scope narrowed to the
witness. Here the scope should be narrowed: the flips demonstrate that **those five** deformations are
caught, not that the ledger discriminates.

### F2 referent drift : **FINDING** (one sub-point; conventions themselves CLEAR)

**(a) The three sums as implemented ARE the objects the literature means. CLEAR.** LH-conjugate
convention, doublet weighting with colour multiplicity, and `grav²U(1)_Y = Σ Y` over left-handed Weyl
states all match. The claim's own counterfactual #4 ("enter `u_R` unconjugated") is direct evidence the
sign flip on conjugation is implemented rather than assumed.

**(b) "one sterile *total-singlet* partner" — the name and the object come apart the moment the
16 is quoted.** Under `SU(3)×SU(2)×U(1)_Y` the state *is* a total singlet, which is exactly why it
contributes zero to all three sums. But the `16` reported in the same sentence is only meaningful in
the mod-16 framework, and there the relevant symmetry is a `ℤ₄ ⊂ U(1)_{B−L}` — under which the state
is **not** a singlet. It is charged, and its charge is precisely what supplies the sixteenth unit.
Verified against the primary abstract (García-Etxebarria & Montero, arXiv:1808.00009, JHEP **08**
(2018) 003): *"Assuming the existence of certain anomaly-free ℤ₄ symmetry we relate the fact that there
are 16 fermions per generation of the Standard Model — including right-handed neutrinos — to anomalies
under time-reversal of boundary states in four-dimensional topological superconductors."*

So the two roles of this one state — *contributes 0 to the three sums* and *contributes 1 to the mod-16
count* — are roles under two different symmetry groups, and the word "total" pre-commits to the reading
that would **void** the very import the claim is trying to hold open. Read literally (singlet under
everything, `B−L` included), the state contributes 0 mod 16, the count is 15, and the SMG condition
fails rather than being merely unasserted. The quarantine line is drawn in the right *place*; the
descriptor undercuts it. Recommended repair: "**gauge-singlet under `SU(3)×SU(2)×U(1)_Y`**", plus one
sentence recording that any future cash-out of the 16 requires this state to carry `B−L`.

### F3 prior art : **CLEAR**

Searched Crossref and INSPIRE REST (per the operational note — WebSearch not used). The claim wears its
non-novelty correctly: it calls the sums "**the standard** hypercharge sum rules" and calls the result a
checked fact, not a discovery. There is no priority to contest. Verified antecedents, publisher metadata,
recorded here so the corpus can cite them (they bear on the findings below, not on any novelty claim):

| Antecedent | Locus | Verified |
|---|---|---|
| Bouchiat, Iliopoulos, Meyer — "An anomaly-free version of Weinberg's model" | Phys. Lett. B **38** (1972) 519 | `10.1016/0370-2693(72)90532-1` |
| Witten — "An SU(2) anomaly" (the doublet-parity condition) | Phys. Lett. B **117** (1982) 324 | `10.1016/0370-2693(82)90728-6` |
| Alvarez-Gaumé, Witten — "Gravitational anomalies" | Nucl. Phys. B **234** (1984) 269 | `10.1016/0550-3213(84)90066-x` |
| Geng, Marshak — "Uniqueness of quark and lepton representations ... from the anomalies viewpoint" | Phys. Rev. D **39** (1989) 693 | `10.1103/physrevd.39.693` |
| Minahan, Ramond, Warner — "Comment on anomaly cancellation in the standard model" | Phys. Rev. D **41** (1990) 715 | `10.1103/physrevd.41.715` |
| Foot, Joshi, Lew, Volkas — "Charge quantization in the standard model and some of its extensions" | Mod. Phys. Lett. A **05** (1990) 2721 | `10.1142/s0217732390003176` |
| García-Etxebarria, Montero — "Dai-Freed anomalies in particle physics" (the mod-16 source) | JHEP **08** (2018) 003, arXiv:1808.00009 | INSPIRE, abstract quoted above |

Nothing UNVERIFIED; every row read from publisher-deposited metadata, none invented.

### F4 scope inflation : **FINDING — and simultaneously an UNDER-CLAIM on the wide side**

*Rule applied (two-sided): restate at the narrowest and the widest scope the computation supports, and
compare both against the text.*

**Narrow side — SCOPE-INFLATION.** Verbatim: *"the three **standard** hypercharge sum rules"* and *"the
ledger is satisfied"*. Three is not the standard set. **`[SU(3)]²U(1)_Y` is a hypercharge sum rule, it
is standard, and it is missing from the list** — conspicuously, since its exact weak-sector analogue
`[SU(2)]²U(1)_Y` *is* listed. The counter-computation above is the number that contradicts the
sentence: a rational table passing all three listed sums with `[SU(3)]²U(1)_Y = 11/12 ≠ 0`. A reader
who meets the words "the ledger is satisfied" will take away "this spectrum is anomaly-free", and the
three listed sums do not support that. The omission is not cosmetic — it is **the load-bearing one**:

```
With all four conditions, solving for the hypercharges given the reps:
    {b: -4a, c:  2a, d: -3a, e: 6a}        <- the Standard Model, up to normalization a
    {b:  2a, c: -4a, d: -3a, e: 6a}        <- the same, u<->d relabel
With the SU(3) condition dropped:  a CONTINUUM of solutions (table above).
```

**Wide side — UNDER-CLAIM.** The *same* entered table, with the *same* arithmetic, satisfies the
**complete** one-generation condition set, not three of it: `[SU(3)]³` = 0 (the colour content is
vector-like — two triplets from `Q` against two antitriplets from `u^c, d^c`), `[SU(3)]²U(1)_Y` = 0
(computed), the three listed sums = 0, and Witten's parity (4 doublets, even). Six conditions.

And then the verbatim sentence *"the ledger is satisfied GIVEN the table and does not certify it"* is
**false in one specific direction, against the claim's own interest**. The complete ledger does not
certify the *representation content* or the *normalization* — that much is right, and that is where the
genuine import lies. But given the reps, it **pins the hypercharge column uniquely up to scale and the
`u↔d` relabel** (the solve above; Geng–Marshak 1989, Minahan–Ramond–Warner 1990). "Five flips break it"
is a shadow of a theorem the claim already has in hand and is declining to state.

---

## AXES ATTACKED AND ABANDONED

- **F5 layer slip — not run** (retired 2026-07-29 per the role spec, notwithstanding the brief's
  request). The one variant that pays is folded into F2, where I ran it: the conjugation convention
  *is* consistent with having no `ν_R` among the gauged 15 (2+6+1+3+3 = 15, matching the SM's 15
  exactly), and the substantive slip-shaped issue — which symmetry group the 16 is counted under —
  is reported as F2(b) rather than dressed as an F5.
- **F1 against the one-generation restriction — attacked and ABANDONED.** My first instinct was that
  one generation is a non-generic witness for a three-generation theory. It is not: anomaly
  coefficients are additive over generations, so `N × 0 = 0` with no further content. Abandoned as a
  non-finding, and the claim's per-generation framing is correct. (The `ℤ₉` baryon-triality condition
  in the same GEM paper *is* generation-number-sensitive, but neither it nor generation count is in
  the claim's scope, so it is not a finding against this claim.)
- **F3 priority — attacked and ABANDONED as a finding.** I went looking for a novelty over-claim and
  there is none to find; the claim self-labels the sums "standard" and the result "a checked fact".
  Reported CLEAR rather than stretched into a finding.
- **The quarantine itself — attacked and largely UPHELD.** I expected the 't Hooft / mod-16 quarantine
  to be the soft spot. It is drawn at the right line: the readings genuinely are not asserted. The
  defect is not the quarantine, it is (i) that the fence encloses three sums while the word "ledger"
  gestures at all of them, and (ii) the one word "total" in F2(b). Credit where due.
- **Arithmetic re-derivation — run to completion and CLEAR**, and I record that explicitly so this is a
  reportable all-clear on that layer rather than an empty page.

---

## VERDICT: **SCOPE-INFLATION** (primary, **COMPUTED**) — with a co-equal **UNDER-CLAIM** on the wide side

Both findings are at the **claim-wording layer only**; the **table-arithmetic layer is CLEAR** and the
claimed tier is honest. The refuting element carries its own counter-computation (the rational
counter-witness table and the four-condition uniqueness solve, both reproduced above from the claim's
stated table alone, in an independent script, without opening the engine) — so it is COMPUTED, not
ARGUED. Scratch scripts are ephemeral by design; every number above is reproducible in under a minute
from the table as stated.

## NARROWEST DEFENSIBLE STATEMENT OF THE CLAIM

> Over the entered one-generation table, **three** of the Standard Model's anomaly-cancellation
> conditions — `[SU(2)]²U(1)_Y`, `[U(1)_Y]³`, `grav²U(1)_Y`, right-handed states entered as conjugates
> — evaluate to exactly zero, and the `SU(2)` fundamental count is 4, even. Five specific counterfactual
> slot flips are each caught by these three sums. This is exact arithmetic over an entered table; the
> three sums are not the complete condition set, and passing them does not by itself establish
> anomaly-freedom.

## WIDEST DEFENSIBLE STATEMENT — *this exceeds the claim as submitted, and that is the UNDER-CLAIM finding*

> The entered one-generation table satisfies the **complete** set of perturbative and global
> anomaly-cancellation conditions for `SU(3)×SU(2)×U(1)_Y`: `[SU(3)]³ = 0` (vector-like colour),
> `[SU(3)]²U(1)_Y = 0`, `[SU(2)]²U(1)_Y = 0`, `[U(1)_Y]³ = 0`, `grav²U(1)_Y = 0`, and Witten's global
> `SU(2)` condition (4 doublets, even). Moreover — and this is stronger than the five counterfactual
> flips — **given the representation content, these conditions determine the hypercharge column
> uniquely**, up to overall normalization and the `u↔d` relabel (Geng–Marshak, Phys. Rev. D **39**
> (1989) 693; Minahan–Ramond–Warner, Phys. Rev. D **41** (1990) 715; reproduced independently here).
> So the honest division is sharper than "the ledger does not certify the table": the ledger does not
> certify the **representation content** or the normalization — that remains the entered import and the
> counted bit — but it **does** pin the hypercharges given the reps. The framework should say which
> half of its entered table is free and which half is forced, because the forced half is larger than
> claimed. The `15 + 1 = 16` count and its mod-16 reading remain correctly quarantined, subject to the
> F2(b) wording repair.

---

### Cross-class independence

Run on **Opus**; the work under review was not authored by this instance, and the meta-observer diet
(derivation withheld) was maintained throughout. Per RUL-045 as scope-corrected by RUL-065, internal
§8a checking is keyed on who authored the work — this is a cross-class check and the CLEAR on the
arithmetic layer therefore carries information.

### Self-persistence

Written by the meta-observer per RUL-079(ii). This is the only file written by this dispatch.
