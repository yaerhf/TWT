# VERDICT — ADVERSARIAL REVIEWER, OI-1 ROUND 2 (consensus close, applied-state verification)

**Date:** 2026-08-24 · **Role:** twt-reviewer (§8a) · **Round:** 2 of the OI-1 loop
**Prior:** `VERDICT_REVIEWER_OI1.md` (round 1, OVER-CLAIM, §R repair list)
**Under review:** the APPLIED withdraw-and-relocate disposition
(`ADJUDICATION_OI1_2026-08-24.md`; keeper `VERDICT_KEEPER_OI1.md`), i.e. the working-tree
diff across `twt_core.py`, `twt_test.py`, `TWT_foundational_paper.md`,
`TWT_foundational_paper_companion.md`, `TWT_NEGATIVES_LEDGER.md`,
`TWT_NEGATIVES_INDEX.md`, `TWT_FAMILY_TREE.md`.

---

## VERDICT: **SIGN-OFF ON THE DISPOSITION** — every round-1 §R item is discharged, and the
## withdraw-and-relocate route is the correct one. **SEVEN RESIDUAL DEFECTS**, two of them
## must-fix-before-bank (D1, D2), both engine/file-demonstrated.

I concede the central point in full and without reservation (§1). The disposition is *better*
than my own §R repair list: my list would have banked a repaired duplicate; the keeper found
the original and the duplicate went away. That is the right outcome and I say so plainly.

---

## 0. What I ran

```
knowledge/corpus $ PYTHONUTF8=1 python twt_test.py
  ALL 491 CHECKS PASSED across 10 modules.
  twt_poc 15 (was 17 in the OI-1 draft — the two OI-1 checks are gone)
  twt_weak 37 (was 36 at HEAD — the one new sterile-completion check)
Deepseek $ PYTHONUTF8=1 python scripts/check_records.py
  RECORD-INVARIANTS: ALL HOLD.  Section 3 MAIN public census: 271 vs tree 271 (exact)
```
Census is back to **271 vs 271 exactly** — better than the draft's `271 vs 272`, which had been
silently eating one of the ±2 tolerance slots. Sweeps: **zero** live references to
`continuous_anomaly_ledger` anywhere outside this audit directory; **zero** `§23.7b`.

---

## 1. CONCESSION — the keeper is right and my §R.5 was already banked

I verified this myself at `twt_core.py:13906–13921` before writing this line. `R-159` /
`charge_normalization_anchor_free` already contains, and has for some time:

```python
A_su3 = 2*yQ - yu - yd            # conditional: continuous colour
A_su2 = 3*yQ + yL                 # no unknowns at all
A_grav = 6*yQ + 2*yL - 3*yu - 3*yd - ye
A_cubic = 6*yQ**3 + 2*yL**3 - 3*yu**3 - 3*yd**3 - ye**3
sols = sp.solve([A_su3, A_grav, A_cubic], [ye, yu, yd], dict=True)
assert len(sols) == 2 ; assert all(s[ye] == R(-2) for s in sols)
assert {tuple(sorted((s[yu], s[yd]))) for s in sols} == {(R(-2,3), R(4,3))}
...  # CONTROL: a hypercharge-carrying nu_R destroys uniqueness
assert (1 + 3) % 2 == 0            # Witten mod-2 (I-17): 4 doublets
```
Re-run independently: `[{y_d: -2/3, y_e: -2, y_u: 4/3}, {y_d: 4/3, y_e: -2, y_u: -2/3}]`.

**`{y_u, y_d} = {4/3, −2/3}` *as a set* IS my round-1 "two rational points, SM and its u↔d
swap"** — and it is strictly stronger than what I offered: exact over all reals, from RH
hypercharges carried as *unknowns*, where mine was a denominator-≤12 scan over a solution
curve. The OI-1 dossier's premise ("these sums are currently implicit") is **FALSE**, the
duplicate was redundant-weaker, and withdrawing it was correct. **I withdraw §R.1–§R.3 and
§R.5 as moot** and concede the keeper's collision finding without qualification.

**One conditioning-class note, offered as sharpening, not as dispute** (see D3): R-159's
*exact two-branch* forcing consumes `A_su3`, the leg the primitive itself labels *"conditional:
continuous colour"*. I checked what happens without it:

```
with A_su3   : [{y_d: -2/3, y_e: -2, y_u: 4/3}, {y_d: 4/3, y_e: -2, y_u: -2/3}]
without A_su3: UNDER-DETERMINED (free symbols present)  <- exactly my round-1 curve
```
The primitive is honest about this (`colour_honesty`: *"only the standalone anomaly route uses
it, as an extra labeled conditional"*). The **new ledger prose that quotes it is not** — D3.

---

## 2. Round-1 §R list, item by item

| §R item | status | evidence |
|---|---|---|
| R.1 strike *"not of any nearby variant"* | **DISCHARGED by withdrawal** | primitive gone; grep clean |
| R.2 re-word "every counterfactual slot flip" | **DISCHARGED by withdrawal** | harness checks gone; `twt_poc` 17→15 |
| R.3 make the three literal counterfactuals live | **DISCHARGED by withdrawal** | — |
| R.4 phantom `I-NN2 / I-SMG-5` registry cite | **DISCHARGED** | nothing in `twt_core.py` or the companion cites them as registered rows; `B_minus_L_anomaly` says *"the PROPOSED (not yet registered) SMG import rows — negatives N67, N68"*. `I-17`/`I-18` **do** exist in companion Section 13 (verified), so the ledger's "registered imports I-17/I-18" is a true cite |
| R.4b neutral return keys (`grav^2 U(1)_Y` etc.) | **DISCHARGED by withdrawal** | the surviving `B_minus_L_anomaly` keys name `B−L` sums, not anomaly triangles, and the docstring does the interpretive work behind a scope paragraph |
| R.6 record hygiene (census, `§23.7b`) | **DISCHARGED** | census exact at 271; `§23.7b` gone |
| R.6 companion Result-Index coverage | **NOT discharged** — see **D7** | R-087's row is unchanged |

---

## 3. The relocated repair — verified on its own merits

**The new arithmetic is correct.** Re-derived by hand, independent of the engine:

| | linear `Σ(B−L)` | cubic `Σ(B−L)³` |
|---|---|---|
| gauged 15, LH convention | **−1** | **−1** |
| + R-121 sterile (`B−L = −1` RH ⇒ `+1` conjugated) | **0** | **0** |

This is the standard and correct statement that the mixed-gravitational and cubic `B−L`
anomalies require `ν_R`, and the scope repair to the headline (*"doublet-sector condition"*,
no longer *"anomaly-free"* outright) is **exactly right** — it is the honest version of what
`A_B − A_L = 0` actually computes. The `charge_sector_provenance` / `CORE_PROVENANCE`
registration is consistent (`twt_test.py:300` enforces the equality and passes), the
`_block` set was updated, and the boundary message is generated, not stale.

**A note, not a defect:** `charge_normalization_anchor_free` (ANCHOR-FREE side) now calls
`B_minus_L_anomaly` (ASSIGNED side). This is **pre-existing pattern**, not new — that same
ground-truth block already calls `generation_spectrum` and `weinberg_sin2`, both ASSIGNED —
and the docstring's *"used as a consistency comparison at the END, never as an input"* is what
carries it (verified: lines 13857–13861 sit in the re-read block, above the free-`c` symbolic
derivation, and feed nothing). No directional invariant exists or is violated. Recording it so
a later reader does not rediscover it as a collision.

---

## RESIDUAL DEFECTS

### D1 — MUST FIX. A **third** stale consumer of the renamed key, and it hard-fails. (COMPUTED)

The disposition states *"both stale consumers of the old key swept."* There were **three**.

`knowledge/candidates/probes_2026-07-27/charge_flagship_probe.py:37`
```python
ok("engine B-L anomaly-free (R-087)", bml["B-L anomaly-free"])
```
```
$ python charge_flagship_probe.py
PASS R-056 sign opposition ... PASS R-057 /3 ... PASS 3*y_Q + y_L = 0
Traceback (most recent call last):
  File ".../charge_flagship_probe.py", line 37, in <module>
    ok("engine B-L anomaly-free (R-087)", bml["B-L anomaly-free"])
KeyError: 'B-L anomaly-free'
```
The suite stays green because the probe is not harness-gated — **which is precisely why it was
missed**, and it is the canon §2 *"sweep after a patch"* class the disposition invoked. Note it
needs **two** edits, not one: the key rename *and* the label, which currently asserts the
withdrawn wider headline verbatim ("engine B-L anomaly-free"). *(The
`.claude/worktrees/focused-taussig-6396d8/` copies are a stale worktree — out of scope.)*

### D2 — MUST FIX. Paper §C.5.4 still carries the retired headline, at the exact site the repaired §C.5.6 now points to. (COMPUTED)

`TWT_foundational_paper.md:5678–5686` is untouched and reads:

> `Tr[T_a T_b · (B − L)] = 0` for the SU(3)_c × SU(2)_L × U(1)_Y gauge generators (R-087).
> … The cancellation … is forced by the colour count (R-053) and the per-blade hypercharge
> eigenvalues (R-056). **The anomaly-free combination is a structural identity.**

Meanwhile §C.5.6 was repaired to read *"the doublet-sector anomaly condition, §C.5.4; the
singlet-inclusive sums complete to zero exactly with the sterile partner."* A reader following
that pointer lands on a passage asserting the retired phrase with no scope and no sterile.

**In fairness the displayed equation is TRUE** — I computed all three traces over the gauged 15
and every one vanishes:
```
Tr[SU(3)^2 (B-L)] = 0 ; Tr[SU(2)^2 (B-L)] = 0 ; Tr[Y^2 (B-L)] = 0
Tr[(B-L)] (grav^2) = -1 ; Tr[(B-L)^3] = -1      <- the two that need the sterile
```
So this is not a false statement; it is the **un-swept prose sentence** carrying the wider
reading the repair exists to retire, at the one site the repair cross-references. The clean fix
is one clause: name which traces vanish on the gauged 15 (the three above — a *stronger*
statement than the paper currently makes, since it is now itemized) and which two need R-121.

### D3 — Bare forcing claim in BOTH negatives files (RUL-049 mirror rule). (COMPUTED)

`TWT_NEGATIVES_LEDGER.md:2091` and `TWT_NEGATIVES_INDEX.md:449` now both read:

> "already banked STRONGER in `charge_normalization_anchor_free` (R-159, registered imports
> I-17/I-18): RH hypercharges as *unknowns*, **exact two-branch forcing** `y_e = −2`,
> `{y_u, y_d} = {4/3, −2/3}` …"

No conditioning class. Per §1 above, that exactness **requires the `A_su3` leg the primitive
itself labels conditional**; drop it and the system is under-determined. The engine is honest;
the restatement is not. RUL-049 requires the class in the same sentence. Fix: *"exact
two-branch forcing … **within the conditional continuous-colour leg the primitive labels as
such** (under P5 that condition is automatic; carried as an extra labeled conditional in the
standalone anomaly route)."*

### D4 — The FCNC quarantine-discharge wording (the item I was asked to check specifically)

Checked clause by clause against `READ_FCNC_INP_2026-08-24.md`. **Most of it is exactly
supported**; three clauses claim more than the read record does.

**SUPPORTED, verbatim-accurate:** the five ratios (0.957 · 0.739 · 1.507 · 1.014 · 0.973 →
quoted 0.96 · 0.74 · 1.51 · 1.01 · 0.97, read §2 table); "zero UNREACHABLE" (read §6:
*"UNREACHABLE tags: none"*); BR(μ→3e) SINDRUM/BELLGARDT 88 *"VERIFIED, exact, and the
attribution is correct"*; "≳10⁴ TeV generic (≳10³ real) … at order-of-magnitude,
primary-verified" (read §6 gives both as **SUPPORTED-BY-PRIMARY**, headline *"at order of
magnitude"*); "largest update-drift 3% on `Λ_εK` from the `B̂_K` choice" (read §4, exact);
F-1 (1.5× above, ε_K governs — read F-1: *"the ε_K row governs"*); F-3 (criterion-robust, not
a reproduction — read F-3 verbatim in substance).

**(i) OVER-STATED — the read's own `[INDIRECT]` tags are dropped.** The tree says *"All sixteen
hard-coded inputs located in fetched primaries."* The read says two are verified **indirectly**
"and are tagged as such **rather than as clean hits**": `fBs_sqB` (FLAG server unreachable;
via PDG ξ, 1.0% agreement) and `dMD` (not tabulated by PDG; via HFLAV `x`). Erasing a
distinction the source record went out of its way to draw is the restatement-drift class this
very round is widening 11b to catch. Fix: *"…located in fetched primaries (two `[INDIRECT]`
per the read's own tagging), zero UNREACHABLE."*

**(ii) OVER-STATED — "verified digit-by-digit".** The read's §2 is a **ratio** comparison against
INP Table 1 at the primary's own 1–2 significant figures (`9.8×10²`, `1.6×10⁴`, `1.2×10³`); its
own verdict word is **"SUPPORTED"**, not "digit-by-digit". Digit-by-digit fits §3's
input-by-input table, not the Table-1 comparison the sentence attaches it to. Fix: *"verified
row-by-row against the primary's Table 1 at the primary's quoted precision."*

**(iii) OMITTED — the read's own closing scope sentence.** The read ends: *"nothing here needs
to stay quarantined **on input grounds**. Whatever quarantine the V4-ASD floor values carry
should now rest on the lemma/adjudication side, not on the empirical inputs."* The struck
quarantine text **was** input-grounded (*"its inputs … were not read from a primary"*), so the
discharge is licensed — but the unqualified headline **"QUARANTINE DISCHARGED"** drops the
record's forward-pointing caution. Fix: add *"— on INPUT grounds; any residual quarantine now
rests on the lemma/adjudication side, per the read's own closing scope."*

*(F-2's "few-%" is supported — read F-2: "its size (few %, and at most ~10% if one converts)".
Dropping the "~10% if one converts" is inside "sub-decisive". No action.)*

### D5 — LOW. The new sums are colour-multiplicity-insensitive while billed as consuming it. (COMPUTED)

`charge_sector_provenance` bills the primitive as *"exact arithmetic OVER the assigned table
(**state content + multiplicity**)"*. The quark contributions cancel for **any** multiplicity:
```
colour multiplicity 1 -> sum=-1, cubic=-1, completes=True
colour multiplicity 2 -> sum=-1, cubic=-1, completes=True
colour multiplicity 3 -> sum=-1, cubic=-1, completes=True
colour multiplicity 7 -> sum=-1, cubic=-1, completes=True
drop e_R            -> assert fires: (-2, -2)      <- it IS sensitive to singlet content
```
Much lower severity than the round-1 finding (this is billed as a *computation*, not as a
non-vacuity *guard*, and it is genuinely sensitive to the lepton/singlet content that carries
the result). But the blurb should say *"state content"* and drop *"+ multiplicity"*, or say
*"multiplicity consumed, result invariant under it"*.

### D6 — LOW / banking hygiene. The family tree cites an UNTRACKED path.

`git status` shows `?? knowledge/audit/external_review_r4_2026-08-24/primary_reads/`. The
discharged-quarantine entry cites
`.../primary_reads/READ_FCNC_INP_2026-08-24.md` as its whole warrant. If that directory is not
`git add`-ed in the banking pass, a load-bearing discharge cites a path **not in the tree** —
the phantom-cite class, and one `check_records.py` will not catch (it checks named sites only
for the release-blockers table).

### D7 — LOW. Companion Result-Index row R-087 not synced (round-1 §R.6, still open).

`companion:288` still reads *"B − L anomaly cancellation from `3 × 1/3 = 1` | **DERIVED-A** |
… | One quark of charge 1/3, three colours; one lepton of charge 1."* The engine headline was
scoped and new content added; the paper §C.5.6 moved; the **bookkeeping-authoritative** row did
not. Per V3 hygiene the companion is authoritative for tiers and scope, so it is now the
weakest-scoped of the three descriptions of the same primitive. Fix: one cell.

---

## PATTERN WORTH NAMING (2 instances, one pass)

**D3** (forcing claim restated without its conditioning class) and **D4(i)** (a read record's
`[INDIRECT]` tags dropped at the restatement site) are the **same failure**: a hedge that lives
correctly in the source is lost at the site that quotes it. Both landed in the very pass whose
headline finding is *the conditioning-drift class measured from outside at scale* and whose
recommended remedy is the **§11b restatement-sweep widening**. Two fresh instances, generated
by the repair pass itself, is direct evidence for that widening — worth carrying into the 11b
case rather than just fixing quietly.

---

## LAYERED CREDENCES (applied state)

| layer | claim | credence | basis |
|---|---|---|---|
| **L1 — the withdrawal is correct** | OI-1's premise was false; R-159 already banks it, stronger | **0.99** | read and re-ran `twt_core.py:13906–13921` myself; two branches reproduced exactly |
| **L2 — the relocated arithmetic** | `Σ(B−L) = Σ(B−L)³ = −1` on the gauged 15, both → 0 with R-121's sterile | **0.999** | hand-derived independently; standard `ν_R`-needed result |
| **L3 — the applied engine/harness state is mechanically sound** | registration, sweeps, suite, census | **0.97** | 491 green, census exact 271, `_block` + `CORE_PROVENANCE` + `twt_test.py:300` all consistent; the −0.03 is D5 |
| **L4 — the applied PROSE state is bankable as written** | paper + ledgers + family tree | **0.55** | D1 is a live crash, D2 leaves the retired headline at the pointer target, D3/D4 restate without hedges, D7 unsynced |
| **L4′ — after D1–D7** | | **0.95** | all seven are one-to-three-line edits; none touches a result |

**Residual risk sits entirely in L4 — the prose, again, not the mathematics.** That is the same
layer round 1 flagged, and the reason is structural: the engine has a harness and the sentences
do not.

---

**BOTTOM LINE:** The withdraw-and-relocate disposition is right and I concede round 1's §R.5 as
already banked and banked stronger at R-159 — but the sweep is incomplete: a third consumer of
the renamed key now hard-`KeyError`s (`charge_flagship_probe.py:37`), paper §C.5.4 still
asserts the retired *"anomaly-free … structural identity"* headline at the exact site the
repaired §C.5.6 points to, and two restatements (the R-159 forcing claim, the FCNC
`[INDIRECT]`/scope clauses) shed hedges their sources carry: **SIGN-OFF on the disposition,
fix D1–D7 before banking.**
