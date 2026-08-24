# 01 — External review ledger: §C.4.5 and §C.3

Reviewer: Claude (Anthropic, model claude-opus-4-6-fable), 2026-08-24, at the invitation of the author.
Status: **SUBMITTED FOR ADJUDICATION — nothing here is banked.**
Basis: TWT repo at public HEAD (2026-08-24); dossier §C.4.5 (lines 5263–5452) and §C.3 (4635–5127) read in full; independent recomputation in `01_verification.py` (this submission), which runs standalone and asserts every V-row below.
Format note: `knowledge/reviews/` is not present at public HEAD, so the requested body-frame-submission format could not be read. This file mirrors the engine's own ledger-dict fields (tier / headline / conditioning / controls / does_not_license) and the companion Section-13 import-row fields. Adjudication should re-map labels where my usage drifts from house convention.

---

## Part 1 — §C.4.5 (sin²θ_W = 3/8 and the crossing descent)

### Verified rows (independent recomputation; every number reproduced without consulting the probe scripts)

| id | claim in §C.4.5 | my recomputation | status |
|---|---|---|---|
| V-1 | descent coefficient `sin²θ_W(M_Z) = 3/8 − 0.0355·t` | analytic: coefficient = (109/24)/α_em⁻¹(M_Z) = 109/(24·127.951) = 0.035497, from b₁ = 41/10, b₂ = −19/6, (5/3)b₁ + b₂ = 11/3 | CONFIRMED |
| V-2 | middle-row band 0.154–0.158 on Λ_L = [0.39, 0.73] M_Pl | 0.1540–0.1575 with M_Pl = 1.2209×10¹⁹ GeV (this also fixes which Planck convention the dossier uses — full, not reduced; the section should say so) | CONFIRMED |
| V-3 | three-coupling row 6.8×10¹⁴ GeV → 0.208 | imposing g₁=g₂ and g₂=g₃ at one scale: M_X = 6.83×10¹⁴, sin²θ_W(M_Z) = 0.2075 at one loop | CONFIRMED |
| V-4 | required crossing ≈ 1.0×10¹³ GeV (one loop) | 1.031×10¹³ GeV = 8.4×10⁻⁷ M_Pl | CONFIRMED (the two-loop 1.09×10¹³ not independently rerun; plausible against my one-loop) |
| V-5 | 3/8 = ΣT₃²/ΣQ² = 2/(16/3) | 2 and 16/3 recomputed from the 15-Weyl table | CONFIRMED |
| V-6 | Trayling precedent (hep-th/9912231; Trayling & Baylis, J. Phys. A 34 (2001) 3309) | known-real to me; not re-fetched this session | CONSISTENT (not re-verified) |

The two-loop shift (+4×10⁻⁴), the threshold window (≤0.011), the monomial-scan statistics (38/148), and the new-states requirement (δb₁−δb₂ ≈ −102) were **not** independently rerun; see F-3.

### Findings and proposed changes

**F-1 — Promote the common-trace-form assumption to a first-class premise row (proposed: P8).**
§C.4.5 already says the quiet part: the single common trace form for Y and T₃ "is the same physical assumption the embedding encodes, in different clothes." At present that assumption lives in prose. The charge sector's premises (P4–P7) are numbered rows the separator can act on; this one should be too, with its counterfactual exhibited: **without a common trace form, c² = ΣT₃²/Σ(Y/2)² is form-dependent and sin²θ_W at crossing is unconstrained on (0,1)** — deleting the premise breaks the result for every parameter value, which is exactly the separator's shape. Proposed decomposition of R-082 in the Result Index:
- R-082a — `3/8` normalization identity. Tier: DERIVED-conditional on {§C.4.2 weak assignment, P8 common-trace-form}. does_not_license: any statement about the measured angle.
- R-082b — the crossing placement / descent. Tier: the lattice-scale reading is **REFUTED-as-reading** (N55 already records this); see F-2 for what the refutation itself conditions on.

**F-2 — A fifth escape route, unlisted, and it cuts both ways.**
All four computed closures, and the middle-row band itself, consume an import nowhere registered: **validity of elementary-field SM RGEs from M_Z to ~0.4 M_Pl for a gauge sector this candidate holds to be emergent/composite at Λ_L.** Near a compositeness scale the gauge two-point function develops form factors and "running" in the Machacek–Vaughn sense is undefined. Two horns:
- the import holds → the lattice-crossing reading is refuted at 33% (the current wound, unchanged);
- the import fails → the candidate has **no computable descent at all**, and R-082b reverts from REFUTED-as-reading to GATED.
Neither horn removes the wound; the second is arguably deeper. Proposed action: a companion Section-13 row — *premises:* SM β-functions valid over the 17 decades M_Z→Λ_L for emergent gauge fields; *level:* inside-frame; *retirement handle:* exhibit the emergent gauge propagator's form factor from the kernel (this is the constructive version of §D.3.5's own emergent-layer handle, so the row and the handle close together). The four escape-route closures then carry "inherits Section-13 row [n]" in their cells.

**F-3 — Reproducibility gap: the probe scripts are not public.**
§C.4.5 cites `knowledge/candidates/probes_2026-07-29/` for the two-loop shooting, the threshold scan, the 148-monomial scan, and the new-states requirement. That path is absent from public HEAD, so the four closures are currently **not outsider-checkable** — the exact reproducibility standard the rest of the corpus meets. Recommend either shipping the probes directory or porting the two-loop shooting into the repo as an unbanked-but-runnable script. Until then, proposed marking on the four closure bullets: COMPUTED-UNPUBLISHED.

**F-4 — The g₁ = g₂-from-D4-isotropy step: say in the Result Index what the prose says.**
The dim-4 isotropy theorem equalizes plane stiffnesses; converting stiffness equality into **coupling** equality per factor is where P8 enters (U(1)_Y's generator is a specific bivector combination, and its effective stiffness is the trace-form-weighted combination). §C.4.5's prose names the two extra premises; the R-082 row should carry them, so a reader of the index alone cannot read `g₁ = g₂` as riding the isotropy theorem unaccompanied.

**Assessment of §C.4.5 overall.** The section's honesty is high and its arithmetic is right — I verified the load-bearing numbers independently and they all land. The section needs no softening and no hardening; it needs the premise promoted (F-1), the running import registered (F-2), and the probes shipped (F-3).

---

## Part 2 — §C.3 (lepton masses, generation phase, cross-sector D/J)

### Verified rows (`01_verification.py` asserts all of these)

| id | claim | my recomputation | status |
|---|---|---|---|
| V-7 | K = 2/3 to 10⁻⁵ at pole masses | K = 0.6666645, rel. dev. −3.3×10⁻⁶ (PDG pole 0.51099895 / 105.6583755 / 1776.93 MeV) | CONFIRMED |
| V-8 | Foot angle 45.000° | 44.9999° | CONFIRMED |
| V-9 | δ_L = 12.73° one-parameter fit | δ_L = 12.7325° = 0.222225 rad | CONFIRMED |
| V-10 | arc-ratio candidate δ_L = 2/9 rad | 2/9 rad = 12.7324°; fitted vs 2/9 agree to 1.4×10⁻⁵ relative | CONFIRMED (as an agreement; see F-6 on its packaging) |
| V-11 | D/J = tan(3δ_L) ≈ 0.787; tan(2/3) = 0.786843 | both reproduced | CONFIRMED |
| V-12 | arc-ratio demand e = √18/tan(2/3) = 5.391979 | reproduced to all quoted digits | CONFIRMED |
| V-13 | R-134: μ² = 313.85 MeV vs m_N/3 = 312.97 MeV, 0.28% | reproduced (m_N = (m_p+m_n)/2 = 938.92) | CONFIRMED |
| V-14 | GST: m_d/m_s = 0.0500 vs |V_us|² = 0.0503 | reproduced | CONFIRMED |

### Findings and proposed changes

**F-5 — R-068's "<0.01% residual" holds in √m-measure only; the row should name its measure.**
My one-parameter fit gives max relative residual **1.6×10⁻⁴ in mass** and **7.9×10⁻⁵ in √m**. The corpus already knows the √m-halving (§C.3.11 applies it explicitly to R-134); apply it here too. Proposed row text: "< 0.01% residual in the √m measure (0.016% in mass)."

**F-6 — The arc-ratio candidate should ship bare, without the ladder.**
§C.3.11 states the candidate as "the n = 3 rung 6/27 of the 2:4:6 ladder." The arithmetic is fine (6/27 = 2/9), but a ladder is a family of rationals, and a family of admissible rationals is a **look-elsewhere multiplier**: the probability that some rung sits within 1.4×10⁻⁵ of a fitted phase scales with the number of rungs on offer. Unless the ladder has an engine primitive with its own counterfactual (I found none), propose the candidate be recorded as the bare statement δ_L = 2/9 rad [CANDIDATE], with the ladder demoted to a remark. The bare statement is stronger, not weaker: one rational, one agreement, one demanded consequence (e = 5.392).

**F-7 — Quantify the look-elsewhere caveat on R-134 using the campaign's own telemetry.**
The 0.28% convergence carries a prose caveat. The programme logs its attempts (the negatives ledger holds 68 entries); it can therefore do better than prose: record **N_tried**, the number of zero-parameter cross-scale pairings examined across the campaign, and state the expected number of ≤0.28% false hits under a log-uniform null (≈ 0.006 × N_tried per two-sided window at this width, order-of-magnitude). If N_tried is in the dozens, an expected false-hit count of O(0.1–1) is the honest companion number to 0.28%. This converts the caveat from a gesture into a statistic, in the house style.

**F-8 — The mass-definition scope of §C.3.3/C.3.3a is the sharpest audit in Part C; extend it two rows.**
The pole-vs-MS-bar analysis (K moving 520–570× its pole deviation under the one-loop QED conversion) is exactly right and I endorse its OPEN status (N57). Two extensions: (i) R-134 inherits the same scope — μ² is built from pole masses — and its row should say so; (ii) R-073/GST does **not** inherit it in the dangerous way, and this is worth a line in its favor: light-quark mass **ratios** are renormalization-scale-invariant at leading order in QCD (flavor-blind anomalous dimension), which is why m_d/m_s ≈ 0.050 is quotable without a scale tag while K = 2/3 is not. Stating this protects R-073 from the same referee objection C.3.3 raises against R-068.

**F-9 — Retire ε-language from result rows; promote the invariant.**
§C.3.10 demonstrates that ε is defined only jointly with the epicycle parametrization's conventions, that ε_u is set by the 2^{3/2} rule rather than testing it, and that the rule is untestable on the framework's own terms (no top hadrons). That is a completed self-refutation of ε as a recorded object. The section also names the parametrization-invariant content: the down-sector resultant amplitude A_d ≈ 1.546 (equivalently K_d ≈ 0.73). Proposal: the companion registry row for this sector records **A_d** (tier: FIT, with its mass-definition scope per F-8), and the ε_u/ε_d rule is moved to the negatives ledger as "tried → not parametrization-invariant → changes if an invariant restatement is exhibited." Knowability tag for the rule as stated: UNPINNABLE.

**F-10 — The arc-ratio test's bite condition may be unreachable in principle; tag it.**
§C.3.11 correctly says the e = 5.392 demand bites only against a sub-percent determination of the Skyrme stabilizer. The historical spread is worse than the section implies: ANW's massless-pion fit gives e = 5.45, Adkins–Nappi with the pion mass gives e ≈ 4.84 (an 11% move from one physical refinement), and profile/quantization variants span roughly 4.5–6. Deeper than the spread: **e is a coupling of an effective theory** and absorbs the effect of omitted higher-order terms, so a "true value of e at the 1% level" may not be a well-posed object in any scheme-independent sense. Proposed knowability tag for the arc-ratio test: **UNKNOWN-KNOWABILITY**, with the tagging task itself named — determine whether any scheme-invariant functional of hadron data pins the pitch functional cot q to sub-percent. If the answer is no, the test moves to UNPINNABLE and the 1.06% residual becomes permanently non-discriminating; better to know that before more effort lands on it.

**F-11 — §C.3.5's FIT-tier honesty: no change proposed.** The direction-of-derivation statement (masses → δ_L → D/J, forward route refuted at the bridge) is exactly right and is the template other sections should follow.

**F-12 — Cross-reference the double-booking.**
§C.3.1's identification (generations = ASD triple) and §C.4.2's weak host live one orientation-swap apart; the core paper (§2.3) records the double-claim. The R-064/R-098 rows should carry a forward pointer to the V4-ASD family-tree node, because item 04 of this submission shows that node now has an empirical floor (FCNC/LFV), which changes its status from "recorded open" to "open with one branch constrained by existing data."

### Proposed tier summary (Part 2)

| object | current | proposed | delta |
|---|---|---|---|
| R-068 lepton triple fit | FIT, "<0.01%" | FIT, "<0.01% in √m (0.016% in mass)" | measure named (F-5) |
| δ_L = 2/9 rad | CANDIDATE via ladder | CANDIDATE, bare | ladder demoted (F-6) |
| R-134 convergence | recorded candidate + prose caveat | recorded candidate + N_tried statistic | caveat quantified (F-7) |
| R-073 GST reading | CANDIDATE | CANDIDATE + RG-invariance note | protection added (F-8ii) |
| ε_u/ε_d = 2^{3/2} | counted fit in registry | negatives ledger; A_d promoted to the recorded object | (F-9) |
| arc-ratio e-test | "bites at ≤1% determination" | UNKNOWN-KNOWABILITY, tagging task named | (F-10) |

End of ledger. Attack invited at F-2 (the import framing) and F-10 (the knowability demotion) first — those are the two rows where I am asserting something the corpus does not already say.
