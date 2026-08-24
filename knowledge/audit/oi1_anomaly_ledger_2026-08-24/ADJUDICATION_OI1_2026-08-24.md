# ADJUDICATION — OI-1 (the continuous-anomaly-ledger adjacent bank): CLOSED BY DISCOVERY

*Coordinator-session worker pass, 2026-08-24 (scheduled session following the round-4 close).
Author of the reviewed item: Fable class (this session). Checkers: reviewer + meta-observer +
keeper, all Opus class — cross-class per RUL-045/RUL-065 (keyed on authorship). Verdicts on
disk in this directory; every claim below is theirs or engine-verified this pass.*

## 1. What was attempted

Round-4 commission item 3 proposed **OI-1**: engine primitives for the three continuous
hypercharge sum rules + the Witten SU(2) doublet parity over the banked one-generation table,
"cheap, should land first; needs no primary read." The merge adjudication
(`MERGE_AND_COMMISSION_2026-08-24.md` Part B item 3) carried that recommendation. This session
authored `continuous_anomaly_ledger()` in `twt_core.py` (§23.7b), registered it on the ASSIGNED
side, added two harness checks (suite 490 → 492 green), and dispatched the full §8a round.

## 2. The verdicts (files in this directory)

- **Reviewer (`VERDICT_REVIEWER_OI1.md`): OVER-CLAIM**, two sub-points REFUTED-COMPUTED. The
  arithmetic holds (L1 credence 0.999) and the tier word is right, but the discriminating-power
  billing is false: three of six counterfactuals were typed constants; the whole non-vacuity
  guard runs green on a P5-violating table (the `u_R ↔ d_R` charge swap); A1 and the doublet
  parity are code identities given the `doublet_hypercharge` cross-check; the quarantine cites
  registry rows (I-NN2/I-SMG-5) that exist nowhere in companion Section 13 (phantom-cite class).
  Its honest replacement measurement: over rationals with denominator ≤ 12 the ledger's live
  content (two equations on the three RH charges) admits exactly **two** points — the SM table
  and its u↔d swap.
- **Meta-observer (`VERDICT_METAOBSERVER_OI1.md`): SCOPE-INFLATION + UNDER-CLAIM** at the
  claim-wording layer; table-arithmetic CLEAR (recomputed blind). "The three standard sum rules"
  omits `[SU(3)]²U(1)_Y` while "the ledger is satisfied" gestures at completeness; exhibited a
  rational counter-witness passing all three listed sums while SU(3)-anomalous; noted the full
  six-condition system pins the hypercharge column uniquely (Geng–Marshak; Minahan–Ramond–
  Warner); flagged "total-singlet" as voiding the mod-16 import if read literally.
- **Keeper (`VERDICT_KEEPER_OI1.md`): COLLISION — the decisive verdict.** All four objects the
  new primitive banks are **already banked, anchor-free and strictly stronger**, in
  `charge_normalization_anchor_free` (R-159, registered imports I-17/I-18), ~6,800 lines below
  in the same file: the anomaly system with the RH hypercharges as **unknowns**
  (`sp.solve([A_su3, A_grav, A_cubic], [ye, yu, yd])`), exactly two branches, `y_e = −2` forced
  in both, `{y_u, y_d} = {4/3, −2/3}` as a set — which *is* the reviewer's two-point degeneracy,
  exact and not scan-limited — the Witten mod-2 parity asserted, the charged-ν_R
  under-determination control, and the continuous-colour condition handled as
  conditional-then-automatic under P5. **Conditioning class (RUL-049), to travel with every
  restatement of the forcing:** the two-branch uniqueness holds *given* the `A_su3` leg the
  primitive itself labels "conditional: continuous colour" — drop it and the system is
  under-determined (the reviewer's round-1 one-parameter curve). The new primitive
  substituted the solved point back in:
  **entailed, could not fail.** Verified independently by the developer on the engine source
  before concession (`twt_core.py:13962–13975`).

## 3. Disposition (converged): WITHDRAW AND RELOCATE

The three verdicts triangulate: there was nothing new to bank. The commission dossier's §3(A)
premise — "these sums are currently **implicit**" — is **FALSE**; the corpus holds them
stronger (forcing, not checking), under registered imports, on the anchor-free side. The
deliverable was **findability**, not code.

**Withdrawn:** `continuous_anomaly_ledger()` and all four of its edit sites (git-reverted;
suite back through 490 baseline before the repairs below).

**Enacted instead (the checkers' converged repairs — each specified in at least one verdict):**

1. **`B_minus_L_anomaly` scope repair + sterile-completion sums** (keeper repair 3; the old
   result that had to give). The headline "anomaly-free, exactly conserved" was one condition of
   the standard set. Now computed LIVE over the gauged table (LH convention): `Σ(B−L) = −1` and
   `Σ(B−L)³ = −1` on the 15 alone, **both completing to exactly 0 with R-121's sterile
   partner** — the sterile does *classical* completion work for R-089's exactness, consuming no
   SMG import. Return key renamed (`"B-L anomaly-free"` → `"B-L doublet-sector condition
   vanishes"`); the two stale consumers of the old key (inside R-159's ground-truth block and a
   harness message) swept in the same pass. Registered on the ASSIGNED side +
   `CORE_PROVENANCE` consumers (it now consumes the assigned table's content/multiplicity;
   B, L entered per label). Harness: +1 check. **Suite 491 MAIN + 87 COMPANION, green.**
2. **Findability cross-link** in `B_minus_L_anomaly`'s docstring: the full free-`c` system,
   two-branch forcing, Witten parity and ν_R control are banked at R-159; OI-1 closed by
   discovery against it.
3. **`generation_spectrum` docstring**: "No nu_R in minimal content" → scoped to the *gauged*
   states, with `Y(S_−) = 0`'s FRAMING-supported status carried (keeper collision 3 — one
   proposition, two strengths, now one strength).
4. **Companion R-062 row**: the non-circularity parenthetical narrowed to the doublet sector;
   the `e₄`-bilinear's chirality-blindness stated; RH-singlet `Y`s attributed to R-159's
   system (keeper repair 4).
5. **Dossier §C.5.6**: the "(anomaly-free, §C.5.4)" parenthetical scoped to the doublet-sector
   condition + the sterile completion (keeper: §C.5.4 itself was correctly scoped; §C.5.6 had
   drifted wider).
6. **N68 row corrected** (dated strikethrough annotation): the OI-1 adjacent-bank cell rode the
   false "currently implicit" premise; OI-2 unchanged; the NN/SMG read's cheap first move
   (ℤ₃ ⊂ anomaly-free U(1) ⇒ discharge free) recorded there.
7. The commission dossier file itself (`03_IMPORT_SMG_dossier.md`) is a filed verbatim
   submission and is **not edited** — its §3(A) error is corrected here and at N68 (deliberate
   divergence from the keeper's letter, per verbatim-record discipline).

## 4. The finding worth more than the item

**A fifth "corpus-holds-it" instance for the round — this one inside the engine itself.** The
round-4 merge's organizing axis was four referee charges naming things the corpus holds and the
Core paper doesn't carry. This pass adds: a commission worker, the merge adjudicator, and this
session's author all failed to find a banked result **in the same file** as the code they were
reading, because it lives inside a large flagship primitive under a name
(`charge_normalization_anchor_free`) that does not say "anomaly." The §11b-widening case
(premise/conditioning coverage) now has an intra-engine face: **a banked result whose name does
not carry its strongest content is findable only by whoever already knows it exists.** Candidate
mechanization (for the §8a batch's PART-C items): the Result-Index row for R-159 and the
engine↔paper map should carry the anomaly-system content as a named searchable term — cheap,
prose-level, and it would have prevented this whole detour.

Also recorded: canon §3 failure-mode 3 ("scoping a search too narrowly") — the author's
pre-write search was `grep "def .*anomaly"`, which finds section §23.7 and misses content
inside differently-named primitives.

## 5. Consensus state

Developer ACCEPTS all three verdicts (steelman done: R-159's block independently read and
confirmed by the developer before withdrawal). The disposition (withdraw + relocate) was
resubmitted to the round's reviewer for sign-off; see `VERDICT_REVIEWER_OI1_ROUND2.md` in this
directory for the closing verdict. No calibration rows owed (no checker verdict overturned —
all three held).
