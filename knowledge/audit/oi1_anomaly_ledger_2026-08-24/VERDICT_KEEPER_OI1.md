# COHERENCE-KEEPER VERDICT — OI-1 `continuous_anomaly_ledger()` (§23.7b)

**Date:** 2026-08-24 · **Role:** coherence keeper (domain-wide consistency search)
**Target:** new CORE primitive `continuous_anomaly_ledger()` in `knowledge/corpus/twt_core.py`,
its `charge_sector_provenance()` / `CORE_PROVENANCE` registrations, and its two `twt_test.py` checks.
**State at check:** working tree dirty (`twt_core.py`, `twt_test.py` modified); `twt_test.py` → **ALL 492 CHECKS PASSED**; `scripts/check_records.py` → **RECORD-INVARIANTS: ALL HOLD**.
**Model class:** Opus. **RUL-045 note:** if the primitive was authored by an Opus-class instance this verdict does **not** satisfy the cross-class requirement and must be re-run on a different class; I cannot determine authorship from the dispatch and flag it rather than assume it.

---

## VERDICT: **COLLISION** — with a **LATENT-COLLISION** rider and an **UNDER-CLAIM** rider.

**Do not bank as drafted.** Everything the primitive banks is *already banked, anchor-free, and
strictly stronger, ~6800 lines below it in the same file.* The repair is cheap and leaves the corpus
better than either the pre- or post-change state, because it also surfaces one old banked docstring
that has been quietly over-claiming (`B_minus_L_anomaly`) and one genuine under-claim (the classical
work the sterile neutrino is doing).

All four collisions are **COMPUTED**, not ARGUED (C-16 CHECK-block extension).

---

## NEIGHBOURHOOD LOADED (14 results; all four axes)

**(a) Shared engine primitive.** `generation_spectrum`, `charge_assignment_from_anchor`, `T3`,
`doublet_hypercharge`, `hypercharge`, `gmn_coefficient`, `weinberg_sin2`, `charge_sector_provenance`,
`CORE_PROVENANCE`, `anomaly`, `B_minus_L_anomaly`, **`charge_normalization_anchor_free`** (the one
that matters — found by the `grep -i anomal` sweep, axis (a), not by the dispatch brief).

**(b) Dependency cone.** Upward: R-056, R-057, R-058, R-062, R-063, R-079, R-087, R-159, P4–P7,
A-P2′, the RH-singlet datum. Downward: nothing — the primitive has **no** dependents, **no** Result-Index
row, **no** View-A row, **no** paper section (see ORPHANS).

**(c) Same physical object.** The three hypercharge sum rules and the SU(2) doublet parity, under
their other names: `A_su2`, `A_grav`, `A_cubic`, and the Witten mod-2 assert — all inside
`charge_normalization_anchor_free()`; paper §C.2.7 (the two anomaly conditions), §C.4.6(i) (the
Witten count), §C.5.4 (the B−L traces); import-registry rows **I-17** (Witten) and **I-18**
(gauge-anomaly cancellation package), both **JUSTIFIED**, both load-bearing.

**(d) Same jurisdiction.** N67 (Nielsen–Ninomiya; solitonic matter, no fermion action), N68 (OI-2
discrete-ℤ₃ cobordism), the SMG dossier §3(A)–(E), R-121/R-122 (the sterile), R-089 (exact B−L).

---

## COLLISIONS FOUND: 4

### COLLISION 1 — the ledger is a weaker restatement of a banked anchor-free theorem [COMPUTED]

**THE TWO CLAIMS.**

*OLD* — `twt_core.py:13960-13975`, inside `charge_normalization_anchor_free()` (R-159, **ANCHOR-FREE**
side of `charge_sector_provenance`, paper §C.2.7/§C.2.8, harness-checked, imports I-17/I-18 registered):

```
A_su3  = 2*yQ - yu - yd          # conditional: continuous colour
A_su2  = 3*yQ + yL               # no unknowns at all
A_grav = 6*yQ + 2*yL - 3*yu - 3*yd - ye
A_cubic= 6*yQ**3 + 2*yL**3 - 3*yu**3 - 3*yd**3 - ye**3
...
assert (1 + 3) % 2 == 0          # Witten mod-2 (I-17): 4 doublets
```

with the docstring: *"the system {[SU(3)]²-U(1), grav²-U(1), [U(1)_Y]³} is 0-dimensional with EXACTLY
TWO branches: y_e = −2 with {y_u, y_d} = {4/3, −2/3}... [SU(2)]²-U(1)_Y vanishes with NO unknowns at
all — a parameter-free pass of the derived LH values (the same arithmetic as R-087)"* — and the
anti-circularity clause: *"c is carried as a free symbol throughout; GMN's c = 1/2 is never assumed."*

*NEW* — `twt_core.py:6967`, `continuous_anomaly_ledger()`, **ASSIGNED** side:
*"the three standard hypercharge sum rules + the SU(2) doublet parity, EVALUATED EXACTLY over the
assigned one-generation table... converting 'the table reproduces the SM charges' into 'the table
satisfies the ledger' as a CHECKED FACT."*

**WHY THEY CANNOT BOTH HOLD (as an addition to the corpus).** They are the same four expressions.
`A1 ≡ A_su2`, `A3 ≡ A_grav`, `A2 ≡ A_cubic`, `doublet_count == 4` ≡ the Witten assert. The old
primitive carries `c` free and uses them as **equations that force** the RH hypercharges and `c = 1/2`;
the new one substitutes `c = 1/2` in, **enters the solution**, and verifies the equations hold there.

Engine counter-computation (re-running the banked system standalone):

```
BANKED solution set:  {y_e: -2, y_u:  4/3, y_d: -2/3}
                      {y_e: -2, y_u: -2/3, y_d:  4/3}
NEW ledger's entered RH column:  y_e = -2, y_u = 4/3, y_d = -2/3
is the NEW column a member of the BANKED solution set?  -> True
=> A_grav there = 0 ;  A_cubic there = 0
```

So **A2 = A3 = 0 is entailed by the banked theorem plus the entered column — it cannot fail.** The
new checks are non-vacuous only for A1 (three counterfactuals genuinely break it) and for the
doublet parity. The one counterfactual touching A2/A3 (`u_R unconjugated`) flips a **conjugation sign
on one row**: it tests the primitive's own bookkeeping convention, not the spectrum. The harness
message nevertheless reads *"the three hypercharge sum rules evaluate to EXACTLY zero"* as though all
three were properties of the spectrum being tested. That is canon §8a's own tell (*a tight tolerance
on a vacuous check is not rigour, it is a tell*) wearing five counterfactuals as cover.

Worse, the substitution **destroys information**: at free `c` the grav and cubic conditions have
`c = 1/2` as their unique / triple root — that is R-159's whole point, and it is what makes I-18 a
*fixing* of the normalization. At `c = 1/2` they are `0 = 0` and say nothing about `c`.

**IF THE NEW STANDS → old must change:** nothing in the old *can* change to accommodate it; the old
is the general case and the new its specialization. The corpus would carry the same four objects
twice, on **opposite sides of its own provenance boundary** (anchor-free at 13773, assigned at 6967),
with the weaker copy shelved above the stronger one and no cross-reference in either direction.
*Blast radius:* R-159, §C.2.7, §C.2.8, I-17, I-18, `charge_sector_provenance`, plus every future
reader who meets §23.7b first and concludes the anomaly sums ride the assigned table.

**IF THE OLD STANDS → new must change:** the ledger becomes either (i) a fold-in — move the
presentation and the genuinely-new counterfactuals into `charge_normalization_anchor_free`'s return
dict, where they attach to the free-`c` form and gain force; or (ii) a thin, explicitly-derivative
reader's primitive that **cites** `charge_normalization_anchor_free` in its first line, states that
A2/A3 are the `c = 1/2` evaluation of an already-banked system and carry no independent weight, and
keeps only what is actually new: the A1 slot-flip counterfactuals and the 15+1 count.
*Blast radius:* the new primitive's docstring, its harness message, its two provenance rows. Nothing else.

**RECOMMENDATION + EVIDENCE: the OLD stands; the NEW must change (option (ii), or fold in).**
Evidence is the entailment above, computed. This is not a recency judgment — the old result would win
on the same evidence if the order were reversed, because it is the one that carries the free parameter.

---

### COLLISION 2 — import posture: I-18/I-17 asserted in one place, quarantined in the other [COMPUTED-BY-RECORD]

**THE TWO CLAIMS.**

*OLD (admitted).* Companion Section 13, **I-18**: *"Gauge-anomaly cancellation package (mixed-gravitational
`Tr Y = 0` and cubic `[U(1)_Y]³`...) | R-159, §C.2.7 — the corroborating fixings of `c = 1/2` and the
right-handed hypercharges | ... | **JUSTIFIED as inside-frame theorem** (registered 2026-07-27)"*.
**I-17** (Witten): *"**JUSTIFIED as inside-frame theorem**"*, used at *"§C.4.6 step (i) — gaugeability
of weak SU(2)₊"*. Paper §C.2.7: *"two anomaly-cancellation conditions... each force `c = 1/2` alone,
and the same system forces the right-handed hypercharges."* Paper §C.4.6(i): *"TWT has 4 left-handed
doublets per generation... = even, so the global anomaly cancels per generation. **Gaugeable.**"*

*NEW.* `continuous_anomaly_ledger` docstring: *"SIGNIFICANCE FENCE: reading (A1)-(A3) as triangle/'t
Hooft anomaly cancellation and (B) as the absence of the SU(2) global anomaly consumes standard QFT
theorems... **This primitive banks the SUMS, the PARITY and the COUNTS; it asserts no imported
significance.**"*

**WHY THEY CANNOT BOTH HOLD.** Assert-then-retract on the same object. The corpus already asserts the
anomaly reading of these exact sums at **registered-import strength**, load-bearing, in the paper body,
and uses it to force three hypercharges and a normalization. An adjacent CORE primitive then declines
to assert it. A reader cannot tell whether TWT claims to satisfy the continuous anomaly ledger or not.

**Compounding record error (admitted row resting on a false premise).** N68's adjacent-bank cell says
OI-1 *"should land first, converting 'we reproduce SM charges' into 'we satisfy the anomaly ledger' as
a checked fact"*, and the SMG dossier §3(A) says the sum rules *"are currently **implicit**."* Both are
false, and were false when written: `charge_normalization_anchor_free` has computed them symbolically,
with sympy, under registered imports, since 2026-07-27. This is precisely the conditioning-drift class
the round-4 Opus adjudication already named as the session's structural headline — *four of the
reviewers' sharpest charges name things the corpus already holds.* This is a fifth.

**IF THE NEW STANDS → old must change:** I-18 and I-17 would have to be demoted from JUSTIFIED to
quarantined; R-159's `c = 1/2` fixings (ii)/(iii) fall; §C.2.7's "the same system forces the
right-handed hypercharges" is withdrawn; §C.4.6(i)'s **Gaugeable** verdict is withdrawn. *Blast radius:
large and unwarranted* — I-18's own revert clause exists and this is not a reason to fire it.

**IF THE OLD STANDS → new must change:** split the fence where the literature actually splits.
ABJ/'t Hooft triangle cancellation and Witten's mod-2 obstruction are **theorems with registered rows
(I-18, I-17)**, not the SMG conjecture; only the **mod-16 / Spin×_{ℤ₂}ℤ₄ reading** rides the
quarantined I-NN2/I-SMG-5 and N67/N68. The fence should quarantine the second and cite the first.

**RECOMMENDATION + EVIDENCE: the OLD stands; the NEW's fence must be split.** Evidence: the registry
rows exist, are marked JUSTIFIED, and are cited from the paper body — a state of the record the new
docstring does not know about. **Additionally: correct N68's cell and the dossier §3(A) sentence** —
an admitted negatives row must not rest on a false statement about the corpus's own contents.

---

### COLLISION 3 — R-062's non-circularity parenthetical vs. the ledger's `Y := 2(Q − T3)` [COMPUTED]

**THE TWO CLAIMS.**

*OLD.* Companion Result Index, **R-062** note cell: *"The combination — including the exact 1/2 — is
derived, and the non-circularity is genuine (**`Y` never defined as `2(Q − T_3)`**)."*

*NEW.* `continuous_anomaly_ledger` docstring: *"`Y = 2*(Q - T3)` per the engine's `Q = T3 + Y/2`
normalization, cross-checked against `doublet_hypercharge`"*; code: `Y = 2 * (_rat(q) - _rat(t3))`.

**WHY THEY CANNOT BOTH HOLD.** R-062's parenthetical is a claim about corpus practice, and it is the
stated ground of the non-circularity. A CORE primitive now does exactly the named forbidden thing, for
the whole 15-state table, and banks three sums over the result.

Engine counter-computation — the ledger's `Y` column against the engine's own `hypercharge()`:

| state | ledger `Y = 2(Q−T3)` | engine `hypercharge()` blade value |
|---|---|---|
| nu_L, e_L | −1 | −1 ✓ |
| u_L, d_L | 1/3 | 1/3 ✓ |
| **e_R** | **−2** | **−1 ✗** |
| **u_R** | **+4/3** | **+1/3 ✗** |
| **d_R** | **−2/3** | **+1/3 ✗** |

The cross-check to `doublet_hypercharge` covers **6 of 15 states**, and the **9 states it omits are
exactly the 9 where the two objects disagree.** The docstring's compressed "cross-checked against
`doublet_hypercharge`" reads as covering the table; the code (correctly) asserts only inside
`if label.endswith("_L")`. Two different objects are both called `Y`.

This is not an error of arithmetic — the RH values are the right SM values, and they are *entailed*
by P4+P5+P7 (universal `c`, chirality-independent `Q`, the slot table), so "inherits its premises" is
technically accurate. It is a **referent collision**: the substrate's hypercharge map is per-blade and
chirality-blind, and therefore *does not supply* state-level RH hypercharge at all. The corpus already
knows this for the doublet split — `charge_assignment_from_anchor` says *"the `e_4`-bilinear... is a
PER-BLADE map — `nu_L` and `e_L` share the single lepton blade `e123`"* — but **no passage states the
chirality-blindness**, which is the case that matters here.

**IF THE NEW STANDS → old must change:** R-062's parenthetical narrows to *"`Y` is never defined as
`2(Q − T3)` **in the doublet sector, where the `e_4`-bilinear supplies it independently**"*, and the
corpus acquires an explicit statement that the RH-singlet hypercharges are GMN-reconstructed, not
substrate-computed. *Blast radius:* R-062's note cell, R-063 (which cites the non-circularity), §C.2
prose. Small — and this reading is **correct**, because it is what the engine actually does.

**IF THE OLD STANDS → new must change:** the ledger reads `Y` from the substrate wherever the substrate
supplies it and names the extra premise where it does not — which is what
`charge_normalization_anchor_free` already does, by carrying `y_e, y_u, y_d` as **unknowns** and
solving for them. *This is the same conclusion as Collision 1.*

**RECOMMENDATION + EVIDENCE: BOTH give, in different registers.** The new primitive should stop
manufacturing `Y` (Collision 1's fold-in does this for free); **and** R-062's parenthetical should be
narrowed regardless, because it is over-broad *independently of this change* — the RH hypercharges have
never been anything but GMN-reconstructed, and the corpus has been asserting a non-circularity slightly
wider than it holds. That is a finding about an old banked row, and it is the kind this role exists for.

---

### COLLISION 4 — `B_minus_L_anomaly()` says "anomaly-free" on one of three conditions [COMPUTED] — **the old result is the one that gives**

**THE TWO CLAIMS.**

*OLD (banked, R-087, DERIVED-A).* `twt_core.py:6956`: *"A_B = 3·(1/3) = 1, A_L = 1, so **A_{B-L}=0
(anomaly-free, exactly conserved)**"*; returned key `"B-L anomaly-free": True`. Paper §C.5.6: *"`B − L`
is exactly conserved (**anomaly-free**, §C.5.4)"*.

*NEW (the standard the ledger installs).* The anomaly ledger for a U(1) charge `X` is **three** sums:
`[SU(2)]²X`, `X³`, `grav²·X` — the new primitive's A1, A2, A3.

**WHY THEY CANNOT BOTH HOLD.** `B_minus_L_anomaly` computes **only** the first (`anomaly()` sums over
LH doublets: `3·X_quark + 1·X_lepton`) and returns the unqualified verdict. Engine counter-computation,
in the new primitive's own LH-Weyl convention, over the same 15-state table:

```
WITHOUT nu_R (generation_spectrum's minimal content):
  grav^2*(B-L) = Sum(B-L)   = -1        <-- NONZERO
  [(B-L)]^3    = Sum(B-L)^3 = -1        <-- NONZERO
WITH the R-121 sterile partner (16 states):
  grav^2*(B-L) = 0
  [(B-L)]^3    = 0
```

By the ledger's own standard, B−L on the 15-state table **fails two of three conditions**. The paper's
§C.5.4 is correctly scoped — *"`Tr[T_a T_b · (B − L)] = 0` for the SU(3)_c × SU(2)_L × U(1)_Y gauge
generators"*, two gauge generators, and I verified all three of those do vanish. The **engine docstring,
the returned key, and §C.5.6 are not scoped**, and they are what a reader and a downstream primitive
meet. This is a bare necessity/universality claim without its conditioning class — **RUL-049**, whose
motivating measured case (the Sakharov "guarantee", honest in its fine print and false as a headline)
is the identical shape.

**IF THE NEW STANDS → old must change:** `B_minus_L_anomaly`'s docstring and returned key gain their
conditioning class — *anomaly-free **against the gauge-generator backgrounds**, which is what makes the
conservation sphaleron-exact; the gravitational and cubic conditions are nonzero on the 15-state content
and vanish only with the R-121 sterile.* §C.5.6's parenthetical gains the same scope.
**Blast radius: prose only.** The *value* `A_{B−L} = 0` is untouched, `A_{B+L} = 2` is untouched, R-087
keeps its DERIVED-A tier for what it computes, **R-089 survives and is strengthened** (see UNDER-CLAIM),
the §E.3 falsifier rows 4/5 are unaffected, and the assert at `charge_normalization_anchor_free:13912`
still passes. No revert clause fires.

**IF THE OLD STANDS → new must change:** the ledger would have to drop A2/A3 as ledger conditions —
which would gut it and contradict I-18, which uses precisely those two.

**RECOMMENDATION + EVIDENCE: the OLD gives.** Evidence: the two computed nonzero values, and the paper's
own §C.5.4, which already states the scoped version correctly — the engine and §C.5.6 have simply drifted
wider than the paper they back. Docstring-contradicting-the-text-it-backs is the recurring class the
brief says to check every time; here it cost nothing to find and it is the finding with the most physics in it.

---

## LATENT COLLISION — jurisdiction, against N67 (gap: the solitonic chiral spectrum)

**N67** (admitted 2026-08-24) disposes of Nielsen–Ninomiya thus: *"NN does not bind the banked substrate
at all, because the corpus contains **no lattice fermion action** (zero Grassmann and zero Fock
occurrences across all six engine files; every `fermion` hit is Finkelstein–Rubinstein **soliton**
quantization). That is not an evasion."*

The 't Hooft anomaly ledger lives in the **same jurisdiction** — a gauged chiral fermion QFT with a
fermion measure (exactly what I-17 and I-18's premise cells say: *"4D chiral fermion path integral"*,
*"a gauged U(1)_Y at the effective level"*). If "our matter is solitonic and there is no fermion action"
is what makes NN inapplicable, the identical argument makes the anomaly theorems inapplicable, and the
ledger's zeros clear no obstruction. **You cannot use one argument in two directions.**

The new primitive's fence currently protects it — it asserts no significance, so nothing fires today.
**The gap that triggers this:** N67's transformed debt — *"the candidate must exhibit the observed chiral
spectrum as the low-energy sector of its own FR-quantized solitons."* The moment that closes, the ledger
becomes load-bearing **and** the jurisdictional symmetry must be stated in the same pass, or the corpus
will be visibly arguing both ways. Note this cuts against Collision 2's recommendation *in the SMG
direction only*: I-17/I-18 are applied at the **inside-frame effective** level (their registry rows say
so), which is a different and legitimate jurisdiction from the substrate level at which N67 operates.
**That distinction must be written down** — it is currently nowhere, and it is the whole reason the two
postures are compatible.

---

## ORPHANS

1. **The primitive has no paper or companion home.** Zero hits for `continuous_anomaly_ledger`, `23.7b`
   or `OI-1` in `TWT_foundational_paper.md`, `TWT_foundational_paper_companion.md`, `TWT_core_paper.md`.
   No Result-Index row, no View-A row, no dependency-graph edge, no Engine↔Paper Map row. This is
   canon §10's named failure mode verbatim (the gluon-octet result that drifted out of §20.2 for a full
   session). `check_records` passed only because the MAIN public census drift (271 → **272**) sits inside
   the ±2 tolerance — **the tolerance is why the missing row is invisible**, not evidence that it is fine.
2. **The four anomaly objects now sit on BOTH sides of `charge_sector_provenance`'s own boundary** —
   anchor-free inside `charge_normalization_anchor_free`, assigned inside the new primitive. The
   boundary's guard is `assert not overlap` over **names**, not content, so a content-level straddle of
   the corpus's most carefully-built provenance line is structurally invisible to it.
3. **`Y(S_−) = 0` carries two strengths in one file.** `twt_core.py:13846-13850`: *"the inference
   'wave-decoupled ⇒ gauge-decoupled ⇒ Y(S_-) = 0' is **FRAMING-supported, NOT a closed identity** — it
   is named separately here with its own would-change-if."* `twt_core.py:6976-6978` (new): *"The three
   sterile partners of R-121 **are** total singlets (Y = T3 = 0)."* Same proposition, flat assertion,
   no would-change-if. The new site must inherit the old site's conditioning.
4. **Nothing relates R-089/R-121 to the gravitational and cubic B−L conditions** — see UNDER-CLAIM.
5. `generation_spectrum`'s *"No nu_R in minimal content."* now has a CORE consumer returning **16** from
   the same table. The relating sentence exists, but on the consumer, not the producer. One clause on
   `generation_spectrum` ("no ν_R among the **gauged** states; the sterile `S₋` partner (R-121) is a
   total singlet and is not tabulated here") closes it.

---

## UNDER-CLAIM — the 16 is doing classical work that the fence hides

The `−1` I computed for `grav²·(B−L)` and `(B−L)³` on the 15-state table is **the same `−1`** the SMG
dossier reports as *"a 15-Weyl generation carries a residual −1 mod 16."* But the classical half of that
statement needs **no SMG import at all** — it is I-18-class, already registered, already JUSTIFIED.

So: **R-121's sterile is the condition under which the corpus's own banked exact-B−L survives its own
gravitational and cubic anomaly conditions.** That is a wholly classical, non-conjectural, in-corpus
consonance between two independently-derived results (R-089's exact B−L ⇒ Dirac ⇒ ν_R exists, and the
16 that completes the ledger), and R-089 is a **live falsifier** (§E.3 rows 4, 5). The new primitive
quarantines the *entire* significance of `n_states_with_sterile = 16` onto I-NN2/I-SMG-5/N67/N68 —
conjecture-strength rows with named opposition (I-SMG-3). That is **too much quarantine**: it hides a
result the corpus has earned behind a conjecture it has not.

The honest split: the **classical** completion (B−L's grav² and cubic conditions close at 16) is
assertable now under I-18; the **mod-16 / Dai–Freed** reading stays quarantined. N67's *"a favourable
coincidence of content, **never** an argument"* is correct **for the mod-16 reading** and should be
scoped to it — the classical statement is not a coincidence, it is an entailment.

---

## RUL-097 / record-invariants (dispatch item 5)

Ran `PYTHONUTF8=1 python scripts/check_records.py`: **RECORD-INVARIANTS: ALL HOLD.** The entered-datum
restatement sweep is non-vacuous (21 live matches), reports **no** unscoped restatement in any governing
file, and flags only the pre-existing **non-fatal** `CLAUDE.md:147` WARN, which is unrelated to this change
and is by design the coordinator's. **No new string introduced by this change trips the sweep.**

Two things the sweep **cannot** see, reported because it cannot:

- **The doublet-parity claim (B) rides the reversible RH-singlet datum and carries no scope marker.**
  `doublet_count == 4` is true *because* the RH fermions are weak-isospin singlets — the entered,
  explicitly **REVERSIBLE** datum (*"an observed right-handed charged current reverses it"*). The sweep
  is phrase-keyed on restatement families; the new primitive states the datum's *consequence* without
  restating the datum, so it passes silently. Candidate item for the 11b widening already on the docket.
- **`continuous_anomaly_ledger` is not registered in `CORE_PROVENANCE["rh_singlet_datum"]["consumers"]`,**
  though it consumes the datum exactly as `charge_normalization_anchor_free` (which **is** registered)
  does. That row is `marker`-checked, so a *missing* consumer fires nothing. Unregistered-premise class;
  cheap to fix, invisible to the suite until fixed.

## Dispatch item 4 — `charge_sector_provenance` boundary prose and `not_in_class`

- `not_in_class` (*"pi3_S3_integer_completion, hypercharge, doublet_hypercharge,
  charge_normalization_anchor_free — the ANCHOR-FREE side; they consume no anchor"*): **still accurate.**
- The ONE-SCREEN prose is **stale**: *"Everything computed downstream of them (**gmn_coefficient,
  weinberg_sin2**) inherits their premises"* — the dict immediately below now has **three** such
  consumers. Record-drift class, one-line fix. (Also note the tension this parenthetical now creates
  with Collision 1: the corpus's flagship anomaly computation is on the *other* side of this boundary.)

## Dispatch item 2 — sterile count consistency

**Consistent everywhere, no collision.** R-121 row: *"Three sterile right-handed neutrinos... DERIVED"*
(3 total). `weinberg_sin2`: *"the three sterile RH neutrinos of R-121 are total gauge singlets,
db1 = db2 = 0"*. N67: *"15 gauged Weyl + 1 sterile RH neutrino = **16**"* (per generation). New primitive:
15 + 1 = 16 per generation, three sterile total. 3 total = 1 per generation × 3 generations — coherent.
The residue is Orphan 5 (wording on `generation_spectrum`) and Orphan 3 (the missing `Y(S_−) = 0`
conditioning), not the count.

## Dispatch item 3 — does the primitive deliver what OI-1 proposed?

**Delivers (A) and (B), plus the counterfactuals, and slightly more than asked on presentation** (it
separates the 15 gauged from the 1 sterile rather than summing over 16 — equivalent, since the sterile
is a total singlet, and cleaner). **Its quarantine language does not conflict with N67** (*"never an
argument"* ↔ *"asserts no imported significance"* agree). **It does conflict with N68's own cell**, which
describes OI-1's deliverable as *converting this into "we satisfy the anomaly ledger" as a checked fact*
— see Collision 2, including N68's false premise that the sums are currently absent. Minor: N68 says
"over the 16-Weyl spectrum"; delivered is "over the 15 + sterile-as-singlet". Non-blocking.

---

## COHERENCE DELTA — what the corpus asserts after this change, as drafted

**It asserts two incompatible things about the same four sums.** Via R-159/I-17/I-18/§C.2.7/§C.4.6(i)
it asserts, load-bearing and at registered-theorem strength, that the mixed-gravitational and cubic
hypercharge conditions **force** `Y_{e_R} = −2, {Y_{u_R}, Y_{d_R}} = {4/3, −2/3}` and **force** `c = 1/2`,
and that the Witten count makes SU(2)₊ **gaugeable**. Via §23.7b it asserts that the same sums are
arithmetic over an assigned table whose anomaly significance the corpus **does not claim**.

It also asserts, via R-062, that `Y` is *never* defined as `2(Q − T3)`, while a CORE primitive so defines
it for all 15 states — disagreeing with the engine's own `hypercharge()` on 9 of them.

**Newly redundant:** all four banked objects (A1, A2, A3, doublet parity) — each already computed and
asserted in `charge_normalization_anchor_free`, in the stronger free-`c` form.
**Newly unreferenced:** the primitive itself — no Result-Index row, no paper section, no dependents.
**Two sections now saying the same thing in different words:** §23.7b and §23.7/§C.2.7/§C.4.6(i).

**After the recommended repairs the corpus would assert one thing, and something better than before:**
the anomaly conditions are an anchor-free system that forces the RH hypercharges and the normalization
(unchanged, R-159); B−L is anomaly-free **against the gauge-generator backgrounds**, with the
gravitational and cubic conditions closing exactly when R-121's sterile is included (new, correct,
strengthens R-089); the mod-16 reading remains quarantined pending N67's transformed debt and N68's
cobordism computation; and the ledger primitive becomes an honest reader's view onto the system rather
than a second, weaker copy of it.

---

## REQUIRED BEFORE BANKING (ordered by cost)

1. Cite `charge_normalization_anchor_free` in the new docstring; drop "CHECKED FACT" for A2/A3 and state
   that they are the `c = 1/2` evaluation of an already-banked free-`c` system (Collision 1).
2. Split the significance fence: assert the (A)/(B) reading under **I-17/I-18** (registered, JUSTIFIED);
   quarantine only the mod-16 reading (Collision 2).
3. Scope `B_minus_L_anomaly`'s docstring + returned key, and §C.5.6's parenthetical, to the gauge-generator
   backgrounds; add the computed `−1`/`−1` and the sterile's completion (Collision 4, UNDER-CLAIM).
4. Narrow R-062's non-circularity parenthetical to the doublet sector; state the chirality-blindness of the
   `e_4`-bilinear once, somewhere (Collision 3).
5. Correct N68's adjacent-bank cell and the dossier §3(A) "currently implicit" sentence (Collision 2).
6. Register the primitive in `CORE_PROVENANCE["rh_singlet_datum"]["consumers"]` with its marker; refresh
   the stale `(gmn_coefficient, weinberg_sin2)` parenthetical (item 4/5).
7. Add the Result-Index row, View-A row, dependency edges, and the paper-body sync (Orphan 1).
8. Add the `Y(S_−) = 0` conditioning to the new docstring; add the "gauged states" clause to
   `generation_spectrum` (Orphans 3, 5).

---

*Persisted by the coherence keeper per RUL-079(ii). Suite 492 + 87 green and record-invariants ALL HOLD
at the time of check — neither fact bears on this verdict, which is about what the sentences assert.*
