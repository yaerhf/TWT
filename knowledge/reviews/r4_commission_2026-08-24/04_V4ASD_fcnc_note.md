# 04 — V4-ASD under existing data: the FCNC/LFV floor for a gauged horizontal su(2)

Prepared 2026-08-24 by Claude (Anthropic). Status: **SUBMITTED FOR ADJUDICATION**, landing on family-tree node **V4-ASD** (mirrored candidate: ASD gauged, SD as generation index). Companion code: `04_fcnc_bounds.py` (runs standalone; asserts the lemma and cross-checks the mixing floors against the Isidori–Nir–Perez benchmark table, arXiv:1002.0900, at factor-2 tolerance).

## 1. What is being tested

The family tree records V4-ASD as a mirrored open branch: gauge the anti-self-dual su(2) — the factor V3 uses as the generation seat — and let the self-dual triple index generations instead. The core paper's fault-line table says this branch is "recorded open." This note shows the branch already has an **empirical floor from existing data**, because a gauged su(2) whose triplet is the generation triple is a horizontal gauge symmetry, and horizontal gauge bosons with generation-charged couplings face four decades of flavor data.

## 2. The no-GIM lemma (proved in code, Part A)

If the three generations sit in the adjoint (triplet) of a gauged su(2)_H, then a fermion mass matrix M invariant under the gauged symmetry must commute with all three generators, and the commutant of the adjoint action is exactly the multiples of the identity (`04_fcnc_bounds.py` verifies the commutant is one-dimensional). So **unbroken su(2)_H forces exact three-fold degeneracy of the generations** — refuted by the observed hierarchy at the first digit. Once M is hierarchical, the gauge couplings in the mass basis are flavor-changing at O(1): at best one generator can be made generation-diagonal (charges −1, 0, +1), and the other two are then pure ladder operators — 100% generation-changing (also asserted in code). There is no alignment freedom and no GIM-like cancellation available: the couplings are the structure constants, and su(2) is not abelian. Every escape that works for generic Z′ models (small mixing angles, MFV structure) is structurally unavailable here.

## 3. The floor (Part B of the code; tree-level exchange, O(1) flavor-changing coupling)

| channel | transition | Λ = M_H/g_H floor |
|---|---|---|
| ε_K (O(1) CP phase) | 1↔2, down | **≳ 1.2×10⁴ TeV** |
| ΔM_D | 1↔2, up | ≳ 1.8×10³ TeV |
| ΔM_K (real couplings) | 1↔2, down | ≳ 9×10² TeV |
| ΔM_Bd | 1↔3 | ≳ 5×10² TeV |
| μ→3e (SINDRUM, BR < 1.0×10⁻¹²) | leptonic 1↔2 | ≳ 2×10² TeV |
| μ→3e at Mu3e target (10⁻¹⁶) | leptonic 1↔2 | ≳ 2×10³ TeV |

The kaon rows reproduce the Isidori–Nir–Perez benchmark values (9.8×10² / 1.6×10⁴ TeV) within the vacuum-insertion normalization tolerance, which the code asserts. μ→eγ arises only at loop level for a pure vector horizontal coupling and is subleading to the tree μ→3e channel here, though for the record the current limit is the MEG II 2021–2022 result, BR < 1.5×10⁻¹³. μ–e conversion (SINDRUM II, R < 7×10⁻¹³ on gold) sits at a comparable scale to μ→3e today; Mu2e/COMET push that channel by roughly another order of magnitude in Λ.

## 4. What the floor does to V4-ASD

**Branch (i): su(2)_H unbroken.** Dead twice over — massless generation-changing gauge bosons (long-range flavor forces, infinite-range contributions to every mixing observable) and the degeneracy theorem of §2 against the observed hierarchy. This branch does not need the table; it fails at the lemma.

**Branch (ii): su(2)_H broken.** Then M_H/g_H must clear ~10⁴ TeV for generic phases (~10³ TeV if the sector is exactly CP-conserving in the 1–2 block, which nothing in the framework arranges). Three structural consequences follow inside TWT specifically:

1. **Decoupling from the physics it was invoked for.** A horizontal factor at ≥10⁴ TeV is inert for the generation phenomenology the ASD triple organizes in V3 (δ_L, the Brannen structure, the mass ladder all live at ≤ GeV). Gauging the generation seat buys nothing observable and costs a breaking sector.
2. **A breaking-sector debt.** The framework would owe a mechanism that breaks su(2)_H at ≥10⁴ TeV — a scale the corpus does not own; §C.4.5's own scale audit ("a Planckian layer and a hadronic layer and no third one," §D.3.5) now cuts against this branch too, and the Majorana-seesaw route to an intermediate scale is structurally forbidden by exact B−L exactly as in the sin²θ_W analysis.
3. **The orientation-pinning tension.** V3 holds the SD/ASD orientation as a convention (§2.4: two classes up to Aut; the swap is a relabeling). A world with the SD factor gauged and light (the weak sector, ~10² GeV) while the ASD factor is gauged and broken at ≥10⁴ TeV is a world where the orientation is **physically pinned** by an enormous asymmetry — which contradicts the unpinned status the classification note assigns it, and would demand its own derivation. Conversely, if only one factor is ever gauged, the family owes an account of why gauging respects the orientation asymmetry it elsewhere calls a convention. Either way, V4-ASD converts a labeling freedom into a dynamical liability.

## 5. Proposed adjudication

Family-tree node V4-ASD: from "recorded open" to **OPEN-WITH-FLOOR**, carrying: (a) the lemma (unbroken variant REFUTED outright); (b) the table above (broken variant viable only above ~10⁴ TeV for generic phases, with the three structural costs named); (c) a forward pointer from R-064/R-098 (the double-booking rows) to this node, per finding F-12 of ledger 01. Retirement handle for the floor itself: none needed — these are measurements; the node's numbers tighten automatically as Mu3e, Mu2e/COMET, and lattice mixing inputs improve. What would *reopen* the branch: an alignment mechanism evading §2 (none exists for an adjoint triple — that is a theorem-shaped obstacle, and any proposal should be checked against the commutant computation first).

## 6. Scope

Nothing here touches V3, which does not gauge the ASD factor; the note prices a named alternative. The bounds assume tree-level exchange with the O(1) couplings §2 forces; loop-suppressed or radiatively-generated horizontal couplings would scale the floors down by the suppression factor, but §2 closes the door on arranging such suppression by alignment. Input values are PDG/FLAG-standard and named in the code with provenance comments; the two kaon rows are cross-checked against the published benchmark table and the rest follow the same normalization.
