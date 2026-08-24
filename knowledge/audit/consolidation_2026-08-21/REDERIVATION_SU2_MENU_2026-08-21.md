# RE-DERIVATION — the su(2) subalgebra menu of so(4) ≅ Cl(4,0) grade-2

**Agent:** re-derivation agent (`knowledge/prompts/rederivation_agent.md`, v1)
**Date:** 2026-08-21
**Round:** consolidation_2026-08-21

---

## 0. Diet declaration (mandatory)

I received the **bare statement only**. I did **not** open the derivation, any probe file, any
worker report, or any verdict. I did **not** read `knowledge/corpus/twt.py` **at all** — not the
function I was warned off, not any other part of it — and I did not read the paper, the companion,
the ledgers, `knowledge/audit/` (other than writing this file into that directory) or
`knowledge/candidates/`. I listed the output directory to confirm it existed and did not read any
file in it.

**In place of the engine I wrote my own Cl(4,0) arithmetic from scratch** (blade Cayley table over
4-bit masks, `e_i² = +1`). This was cheaper than reading someone else's engine and removes the
contamination risk entirely. Scratch files (scratchpad, not in the repo):
`clif.py`, `step1_setup.py`, `step2b_claim1.py`, `step3_claims23.py`.

---

## 1. VERDICT

> ### REPRODUCED-WITH-DELTA
>
> All three claims reproduce. The deltas are **scope/wording refinements, not corrections**:
> four of them, listed in §6. None of them touches the truth of any claim as stated.

**Partial-recall disclosure (required by the role file).** I must be honest about which parts were
derived and which recalled:

| component | status |
|---|---|
| the *method* for Claim 1 (subdirect products / Goursat, plus "su(2) has no 2-dim subalgebra") | **RECALLED** — this is standard Lie theory and I recognised the shape of the problem immediately |
| the *case analysis* executed on so(4) with that method | **DERIVED** here, case by case (§3.1) |
| the *conclusion* "SD, ASD, diagonals, nothing else" | **partly recalled.** I would probably have asserted it from familiarity with so(4) |
| Claims 2 and 3 | **DERIVED** — short Clifford computations I performed here, not recalled |
| the numerical Grassmannian search (§3.2) | **GENUINELY INDEPENDENT** — see the calibration note below |

**Calibration note that matters.** My recall of so(4)'s subalgebra structure is demonstrably
**not reliable**: I predicted, as a "known-answer" control, that so(4) has **no** 4-dimensional
subalgebra. The unbiased search found 60/60. My prediction was **wrong** — `s₊ ⊕ ℝ·u` with
`u ∈ s₋` is closed, because `[s₊, s₋] = 0`; I had wrongly required the `u(1)` to sit in the centre
of the whole algebra rather than merely to commute with `s₊`. I verified the corrected statement
directly (closure defect 3.9e-16). This is recorded because it **raises the evidential weight of
the numerical route and lowers the recall concern for the k=3 result**: the search is not echoing
my priors — it contradicted one of them.

---

## 2. Setup, re-established independently

Six grade-2 basis elements `{e12,e13,e14,e23,e24,e34}` of Cl(4,0), bracket `[A,B] = ½(AB − BA)`.

Computed from my own Cayley table:

- grade-2 is **closed** under the commutator (every product purely grade 2) → a 6-dim real Lie algebra `g`.
- Killing form `= −4·𝟙₆` — **negative definite**, so `g` is **semisimple of compact type**.
  (This is the fact that does the work later: *every subalgebra of a compact Lie algebra is
  reductive*.)
- `I₄ = e1234`, `I₄² = +1`; `I₄` **commutes** with every bivector (central in `Cl⁺`) and
  **anticommutes** with every vector.
- Left multiplication by `I₄` on the bivector 6-space is an involution `D`, `D² = 𝟙`, eigenspaces
  of dimension **3 + 3** (SD `= +1`, ASD `= −1`).
- `[SD, ASD] = 0` (max 2.8e-16) and each factor, after normalisation, has **exactly `ε_ijk`**
  structure constants ⇒ `g ≅ su(2) ⊕ su(2) ≅ so(4)`, with SD and ASD as **ideals**. ✔

---

## 3. CLAIM 1 — the three families

### 3.1 Analytic route (subdirect products)

**Lemma A. The subalgebras of `su(2)` have dimension 0, 1 or 3 — never 2.**
*Proof (derived here, not assumed).* `su(2)` is compact type, so any subalgebra `k` is reductive:
`k = z(k) ⊕ [k,k]` with `[k,k]` semisimple. There is no semisimple Lie algebra of dimension 1 or 2,
so a 2-dim `k` would have `[k,k] = 0`, i.e. `k` abelian of dimension 2 — forcing `rank su(2) ≥ 2`.
But `rank su(2) = 1`. Contradiction. ∎

**The classification.** Let `h ⊆ s₊ ⊕ s₋` with `dim h = 3`. Put
`a = p₊(h)`, `b = p₋(h)`, `n₊ = h ∩ (s₊⊕0)`, `n₋ = h ∩ (0⊕s₋)`.
Then `n₊ ◁ a`, `n₋ ◁ b`, and — because `h ↠ b` has kernel `n₊` and `h ↠ a` has kernel `n₋` —

```
dim h = dim n₊ + dim b = dim n₋ + dim a  = 3.
```

By Lemma A, `dim a, dim b, dim n± ∈ {0,1,3}`. Enumerate:

| case | consequence |
|---|---|
| `a = 0` | `h ⊆ s₋`, `dim h = 3` ⇒ **`h = s₋`** |
| `b = 0` | **`h = s₊`** |
| `dim a = 1` | `dim n₋ = 3 − 1 = 2` — **impossible** by Lemma A |
| `dim b = 1` | `dim n₊ = 2` — **impossible** by Lemma A |
| `a = s₊, b = s₋` | `3 = dim n₊ + 3` ⇒ `n₊ = 0`; likewise `n₋ = 0`; so `p₊|_h` and `p₋|_h` are **injective**, `h` is the **graph of an isomorphism** `φ : s₊ → s₋` |

**Exactly three families. ∎** The "impossible" rows are precisely where a hypothetical *mixed /
unequal-weight* subalgebra would have to live, and Lemma A closes them.

**The unequal-weight sub-clause, explicitly.** Put `X_i = α A_i + β C_i`. Then
`[X_i, X_j] = ε_ijk (α² A_k + β² C_k)`, which lies in `span{X_l}` iff `α² = λα` and `β² = λβ`.
Eliminating `λ` (sympy): **`αβ(α − β) = 0`** — so `α = 0` (ASD factor), `β = 0` (SD factor), or
`α = β` (diagonal). **No unequal-weight combination closes.** ✔
(Consistently: `{(x, λφ(x))}` is a subalgebra iff `λ² = λ`, i.e. `λ ∈ {0,1}` — a graph admits no
free rescaling.)

**Why the diagonals are ONE class.** `Aut(su(2)) = Inn(su(2)) = SO(3)`, and the connected group
acts on `g` by `Inn(s₊) × Inn(s₋) = SO(3) × SO(3)`, sending `graph(φ) ↦ graph(Ad_{g₋} ∘ φ ∘ Ad_{g₊}⁻¹)`.
Choosing `Ad_{g₋} = φ₀φ⁻¹` (possible, since `φ₀φ⁻¹ ∈ Aut = Inn`) carries any graph to `graph(φ₀)`.
So all diagonals are conjugate: **one class, a 3-parameter family** (`SO(3)`-worth of
descriptions of one conjugacy class). `s₊` and `s₋` are ideals, hence **fixed** by every inner
automorphism — each is a class of size one. **Three conjugacy classes.** ✔

### 3.2 Numerical route (unbiased, independent of the above)

Search `Gr(3,6)` by minimising the closure defect `Σ_{i<j} ‖(1 − UUᵀ)[u_i,u_j]‖²` with
`scipy.optimize.least_squares` from **400 random starts**; keep residual `< 1e-10`
(worst kept: 5.7e-12).

```
converged closed 3-planes: 400/400
(rank p_SD, rank p_ASD):
   (3,3)  x393   graph SD->ASD (diagonal)
   (3,0)  x5     the SD factor
   (0,3)  x2     the ASD factor
subalgebras outside the three predicted families: 0
```

And for **all 393** graph solutions, `φ = U_ASD · U_SD⁻¹` was checked to be an actual **Lie algebra
isomorphism**: `φᵀφ = 𝟙` and `det φ = +1` (range `0.99999999999999 … 1.0000000000000149`),
**0 violations**. So every found (3,3) subalgebra is a graph of an isomorphism, exactly as the
analytic route predicts, and never a "skewed"/unequal-weight plane.

### 3.3 Controls (the search machinery is calibrated, not just agreeable)

| control | known answer | search returned |
|---|---|---|
| abelian ℝ⁶, k=3 | every 3-plane closed | defect 0.0 on all 50 random planes ✔ |
| so(3), k=3 | **only so(3) itself** — the requested control | the whole space, defect 0.0; nothing else exists to find ✔ |
| **so(3), k=2** | **none** (Lemma A) | **0/80 converged**; best random defect 1.0 ✔ (proves the searcher can return *nothing*) |
| so(4), k=2 | one class, the maximal torus | 80/80, **all abelian** (max bracket 6.9e-15), all `(rank p_SD, rank p_ASD) = (1,1)` = one Cartan line per factor ✔ |
| so(3)⊕ℝ³, k=3 | rich moduli | 24/40 converged ✔ (searcher can return *many*) |
| so(4), k=4 | *I predicted none* | **60/60 — my prediction was wrong**; corrected in §1 |

The so(3),k=2 control is the important one: a searcher that always "finds something" would be
worthless, and this one correctly finds nothing.

**CLAIM 1: REPRODUCED** (analytic route: Goursat/subdirect products + "no 2-dim subalgebra of
su(2)"; numerical route: Grassmannian defect minimisation with controls).

---

## 4. CLAIM 2 — orientation reversal, and the two classes

For a unit vector `v`, the twisted adjoint `x ↦ −v x v` is the reflection in `v^⊥`
(`det = −1` on ℝ⁴). On **even** elements the two sign flips cancel, giving `X ↦ v X v`.

**Analytic.** `I₄` **anticommutes** with vectors in even dimension (verified: `I₄ e_i = −e_i I₄`),
so `v I₄ v = −I₄ v v = −I₄`. Hence for `B` self-dual (`I₄B = B`):

```
I₄ (vBv) = −v I₄ B v = −v B v   ⇒  vBv is ANTI-self-dual.
```

So an orientation-reversing conjugation carries **SD → ASD** and flips `I₄`. ∎

**Computed**, for three different reflection vectors (`e4`, `e1`, `(e1+e2+e3+e4)/2`): `R` exactly
orthogonal, `det R = −1.000000` in each case; `I₄ ↦ −e1234` in each case; conj(SD) lands in ASD
with residual ≤ 1.8e-16 and conj(ASD) in SD with residual 2.4e-16. ✔

**The connected group cannot do it.** `s±` are **ideals**, so every inner automorphism preserves
each. Verified over **200 random rotors** `R = exp(t·B)`: worst deviation of `Ad_R(SD)` from SD is
4.2e-16. ✔

**Counting.** `g ≅ su(2) ⊕ su(2)` with two isomorphic simple ideals, so
`Aut(g) = (Aut su(2) × Aut su(2)) ⋊ ℤ₂ = (SO(3) × SO(3)) ⋊ ℤ₂` and `Inn(g) = SO(3) × SO(3)`; hence
`Out(g) = ℤ₂`, generated by the factor swap — **and the swap is realised by an orientation-reversing
orthogonal conjugation**, as just computed. The swap sends `graph(φ) ↦ graph(φ⁻¹)`, i.e. maps the
diagonal class to itself (verified: image of a diagonal still has `(rank p_SD, rank p_ASD) = (3,3)`).
So the three Inn-classes fuse to **exactly two Aut-classes: {a chiral factor} and {the diagonal
class}**. ✔

**CLAIM 2: REPRODUCED.**

---

## 5. CLAIM 3 — the Weyl-half rank signature

`Cl⁺(4,0)` is 8-dimensional (verified). `P± = ½(1 ± I₄)` are **central** idempotents in `Cl⁺`
(central because `I₄` commutes with all even elements), complementary, each of rank 4 — the two
minimal two-sided ideals `S± = Cl⁺P±`, each `≅ ℍ ≅ ℂ²`. ✔

**Analytic.** For `B` self-dual, `B P₋ = ½(B − B I₄) = ½(B − B) = 0`. For any `u ∈ S₋` we have
`u = uP₋`, and `P₋` is **central**, so `Bu = B P₋ u = 0`. So **SD annihilates `S₋` identically**.
On `S₊`, the map `s₊ → End(S₊)` is the fundamental (spin-½) representation — faithful — so its
image is 3-dimensional. Mirror for ASD. For a diagonal `h = {x + φ(x)}`: on `S₊` the element acts
as `x` alone (its `φ(x) ∈ s₋` part is killed), and `x` sweeps all of `s₊`, giving rank 3; on `S₋`
it acts as `φ(x)`, sweeping all of `s₋`, again rank 3. ∎

**Computed** (left-regular matrices on `Cl⁺`, restricted to each half; rank = `dim span{ρ(X)|_S}`
inside `End(S)`):

| subalgebra | rank on S₊ | rank on S₋ |
|---|---|---|
| SD factor | **3** (max op norm 2.000) | **0** (max op norm **0.000**) |
| ASD factor | **0** (0.000) | **3** (2.000) |
| diagonal `{A_i + C_i}` | **3** (2.000) | **3** (2.000) |

Swept over **150** independently re-found 3-dim subalgebras from the unbiased search: every
`chiral` one gave `(0,3)` or `(3,0)`, every `diagonal` one gave `(3,3)`; no exceptions.

Since Claim 1 says these are *all* the 3-dim subalgebras, the property "**trivial on one spinor
half, full rank on the other**" **selects exactly the two chiral factors and excludes every
diagonal embedding**. ✔

**CLAIM 3: REPRODUCED.**

---

## 6. The deltas (the finding)

Four, all refinements of *scope/wording*. **None contradicts anything as stated.**

**D1 — "three families" is three *conjugacy classes*, but they are not three of a kind.**
`s₊` and `s₋` are **ideals**, so under the connected group each is a **fixed point** (a class of
size 1); the diagonals are a genuine **3-parameter family** (an `SO(3)`-worth of graphs, all
conjugate). Calling all three "families" is fine but flattens a real structural asymmetry: two
rigid points and one moving class. This asymmetry is *why* Claim 2 works — an ideal cannot be
moved off itself by anything connected, so only an outer (orientation-reversing) automorphism can
reach across.

**D2 — the load-bearing lemma is "su(2) has no 2-dimensional subalgebra," and it is worth naming.**
The whole of Claim 1 turns on Lemma A; the `dim a = 1` and `dim b = 1` rows are the *only* place a
genuinely exotic subalgebra could hide, and they die solely because `rank su(2) = 1`. The
statement's phrase "no *mixed* subalgebra built from unequal-weight combinations closes" describes
a **sub-case** (the equal-index ansatz `αA_i + βC_i`, killed by `αβ(α−β)=0`); it is not by itself
the general argument. A reader could mistake the sub-case for the proof. **The general exclusion is
Lemma A, not the `α,β` computation.**

**D3 — "rank" needs one word of disambiguation in Claim 3.**
I read "acts with full rank (3)" as *the dimension of the image of the map `h → End(S)`* — i.e.
**faithfulness** — and that is what I verified. Under the *other* natural reading (the matrix rank
of an individual operator), a single nonzero SD bivector acts on `S₊ ≅ ℝ⁴` **invertibly**, so the
number would be **4**, not 3. Both readings give the same qualitative selection (chiral ⇒ trivial
on one half), but only the first makes "3" the right number. Worth pinning the word.

**D4 — Claim 2's `det = −1` element is any reflection, and the `I₄` flip is generic, not special
to `e4`.** I checked three inequivalent reflection vectors including a non-basis one; all give
`I₄ ↦ −I₄` and the SD↔ASD swap identically. The claim is not sensitive to the choice, which is
worth stating since a single-witness demonstration would look non-generic.

**Adjacent observation, not a delta** (offered because it is true and cheap, and because my being
wrong about it is on the record): so(4) **does** have 4-dimensional subalgebras, `s₊ ⊕ ℝu` with
`u ∈ s₋` (and mirror) — the only ones, by the same Goursat analysis. Nothing in the three claims
says otherwise; I note it only because I initially believed the opposite and the search corrected
me.

---

## 7. Non-powers observed

I did not tier, bank, rule, or edit anything. I have not read the original derivation and this
report contains **no statement about its quality** — only about what I obtained independently.

## 8. Reproduction

```
scratchpad/clif.py             from-scratch Cl(4,0) (blade Cayley table, e_i^2=+1)
scratchpad/step1_setup.py      g ~ so(4); Killing = -4*I; I4^2=+1; 3+3 Hodge split; [SD,ASD]=0
scratchpad/step2b_claim1.py    Gr(3,6) search, 400 restarts + 6 controls
scratchpad/step3_claims23.py   reflections, rotor invariance, Cl+ = 8-dim, P+/P-, Weyl-half ranks
```
