# 05 — Route memo: a finite-grain deviation law for the Sorkin parameter

> ## ⚠ DATED HEADER ANNOTATION (2026-08-25, Sorkin L2 repair pass) — NUMBERS IN THIS MEMO'S BODY THAT DID NOT SURVIVE
>
> **This memo's BODY IS NOT EDITED — it is a filed submission and stands as its author wrote it.**
> This annotation exists because the memo is the Sorkin arc's cited **Authority**, so a reader following
> the pointer would otherwise take its unverified figures as operative. **The arc's operative records
> are `knowledge/audit/sorkin_arc_2026-08-25/PREREGISTRATION_FROZEN.md` and, for every claim,
> `SORKIN_L2_2026-08-25.md` in that directory.**
>
> **1. TWO LITERATURE NUMBERS FAILED PRIMARY FETCH AND ARE USED NOWHERE** (arc finding SK-F3; the
> "used nowhere" claim was independently keeper-verified by grep — they appear only at §0 and §"state
> of the art" of this memo, lines 9 and 11, and nowhere else in the corpus):
> - **"the quantum-regime Sorkin parameter has since been measured at the 2×10⁻³ level"** — NOT
>   CONFIRMED at abstract level against the fetched primaries.
> - **"engineered up to κ ≈ 0.25 in near-field-enhanced settings"** — NOT CONFIRMED at abstract level.
> - Consequently **this memo's operative window "κ_exp ≲ 10⁻³–10⁻⁴" is superseded** by the frozen,
>   fetched window: **κ_exp ≲ 10⁻² (Sinha et al., *Science* 329, 418 (2010)) and κ_exp ≲ 10⁻⁴ (Kauten
>   et al., *NJP* 19, 033017 (2017))** — and those two bounds are **not the same quantity**: Sinha's is
>   **raw**, Kauten's is **already detector-nonlinearity-corrected but not looped-path-corrected**
>   (L2 §5.5).
>
> **2. THE §2 HEADLINE SHAPE OVER-CLAIMED, AND WAS WEAKENED BY THE ARC AGAINST ITSELF.** *"Any
> saturation-type substrate produces an intensity-linear κ residual"* needs the `η₁ ≠ 0` condition
> attached; the registered shape is **κ_TWT ∝ u^{n\*}, n\* ≥ 1** with the first nonvanishing order
> setting the exponent (generically 1 — *generic over the substrate premise's own parameter space*).
>
> **3. THE §2 DISCRIMINATOR SENTENCE DOES NOT STAND AS PUT.** *"Existing triple-slit datasets taken at
> multiple intensities can already bound the slope dκ/dI"* — **there is no such dataset** (no published
> series is an intensity scan at fixed geometry, fixed detector **and** fixed photon statistics; Kauten's
> three points confound all three at once). And **the intensity slope is not by itself a discriminator**:
> detector dead time gives slope **0.998** and photodiode saturation **1.012**, both at the claimed
> `n* = 1`, at magnitudes comparable to Sinha's own published central value. The deliverable is
> re-registered as **the degeneracy-breaking protocol** (L2 §5.2), with **Rozema et al., *Phys. Rev. A*
> 103, 052204 (2021)** credited as prior art for nonlinearity-sourced `I₃` inside ordinary QM.
>
> **4. THE §2 SAFETY CLAIM IS CONDITIONAL, NOT CERTIFIED.** *"Thirty-plus decades below κ_exp: safe"*
> rides an **UNDERIVED localization volume** for `u` — 30.0 decades of swing across defensible readings,
> with a refutation corner at L = 0.088 fm — across an **un-built outside↔inside projection** (L2 §6).
>
> **5. DESCRIPTOR:** Route 1 is a **saturation** computation; "counting/measure" is **Route 3**'s
> descriptor. Both are kernel-free.
>
> *(Route 2 remains #1-gap-blocked and was not opened. Route 3's floor is quoted `d`-blind — the `1/d`
> prefactor is omitted, ≤0.8 decades.)*

Prepared 2026-08-24 by Claude (Anthropic). Status: **SUBMITTED FOR ADJUDICATION — attempt record, not a result.** Per the commission: a fresh route matters more than a finished result; this memo delivers three routes, two with derived scaling shapes and benchmark magnitudes, one honestly blocked, each with its consumed premises named and its level (family vs candidate) tagged.

## 0. Target and definitions

Sorkin's hierarchy: with P_S the detection probability with slit-set S open, the third-order interference term is I₃ = P_{ABC} − P_{AB} − P_{AC} − P_{BC} + P_A + P_B + P_C, and the normalized Sorkin parameter is κ = I₃ divided by the expected pairwise interference magnitude. Exact Born quadraticity ⇒ κ = 0 identically; every incumbent theory inputs the exact zero. TWT holds the Born exponent as a theorem conditional on premises (§2.7 of the core paper), so at finite grain the theorem's error term is a **derivable number** — the only channel in the corpus where the framework can beat the incumbents on agreement-counts rather than tie them.

**A definitional fence first, or the observable is wrong.** Standard quantum mechanics itself produces a small nonzero measured κ from non-classical looped trajectories (path-integral paths visiting multiple slits): this is a known effect, computable within QM, negligible in far-field geometries but engineered up to κ ≈ 0.25 in near-field-enhanced settings. Any TWT prediction must therefore be defined as κ_TWT := κ_measured − κ_looped-paths(QM), a *residual after the standard path-integral accounting*. A TWT claim that forgets this fence would be refuted by standard QM's own fine print.

**Experimental state of the art (for calibration, sources from this session's search):** the original three-slit bound ruled out third-order interference below 10⁻² of pairwise interference (Sinha et al., Science 2010); the quantum-regime Sorkin parameter has since been measured at the 2×10⁻³ level, optical interferometry pushes the ratio to roughly four orders below pairwise (~10⁻⁴), and matter-wave/BEC multipath tests sit at the few×10⁻³ level. Call the operative window κ_exp ≲ 10⁻³–10⁻⁴.

## 1. Where the Born theorem degrades — the three candidate seams

The corpus's Born-exponent argument consumes (at least): (i) a stationary configuration measure for the driven medium, (ii) exact U(1) equivariance of that measure along the forced complex line {1, B}, (iii) the continuum/linear superposition of small excitations. Finite grain attacks each seam differently, giving three routes.

## 2. Route 1 — carrier saturation (seam iii). **Derived shape; the near-term falsifiable content.**

*Consumes:* S1a (material medium) + the costed-carrier pick (finite carrier amplitude — "the amplitude notch" ontology). *Level:* family, up to the value of the saturation density.

A physical medium with bounded carrier amplitude is linear only asymptotically; the leading correction to the energy-density functional is quartic, P ∝ |ψ|²(1 + η|ψ|²/ρ_sat + …). A quartic term contains genuine three-path cross terms (a²b̄c̄ and permutations), so it feeds I₃ directly:

> **κ ≈ c₁ · u / ρ_sat**, u = energy density of the interfering excitation in the coherence volume, c₁ = O(1).

Two-scale fork on ρ_sat (the corpus owns two layers, §D.3.5): cell-scale saturation ρ_cell ~ f_π⁴/(ħc)³ ≈ 6×10³³ J/m³, or grain-scale ρ_Pl ≈ 4.6×10¹¹³ J/m³. Benchmarks for a 2.5 eV photon:

| coherence volume | κ (cell-scale ρ_sat) | κ (grain-scale ρ_sat) |
|---|---|---|
| (10 μm)³ | 7×10⁻³⁸ | 9×10⁻¹¹⁸ |
| 1 mm³ | 7×10⁻⁴⁴ | 9×10⁻¹²⁴ |

Thirty-plus decades below κ_exp: **safe, and it is a number where the incumbent writes zero**. The falsifiable content is the *shape*, not the magnitude: **κ ∝ beam intensity at fixed geometry** (u scales with intensity), while the QM looped-path κ is intensity-independent at fixed geometry. That is a clean discriminator: existing triple-slit datasets taken at multiple intensities can already bound the slope dκ/dI, and no reported analysis has looked at that axis. Proposed as the route's registered prediction-shape: *any* saturation-type substrate produces an intensity-linear κ residual; TWT's two-scale fork fixes the two admissible intercepts. **Proposed tier: CANDIDATE (shape DERIVED-conditional on the quartic truncation; magnitude pinned only up to the ρ_sat fork).**

## 3. Route 2 — Z_N equivariance breaking (seam ii). **Blocked; recorded as tried → failed-because → changes-if.**

*Consumes:* candidate pick #1 (D4 lattice) — this route is **candidate-level**, the only one of the three that could distinguish V3 from a continuum family member.

The Born theorem's U(1) equivariance is, microscopically, only a discrete symmetry: the lattice point group's stabilizer of the forced complex line {1, B} acts on the rotor phase as Z_N, with N read off the plane's polygonal sections — for the 24-cell/D4 geometry the natural candidates are N = 6 or 12 (hexagonal central sections; the exact N is a W(F4) stabilizer computation, half a page, not done here). A Z_N-invariant-but-not-U(1)-invariant measure adds harmonics: P(ψ) = |ψ|²[1 + Σ_k c_k cos(Nk·arg ψ + φ_k)], and the harmonics feed I₃ with coefficient c₁ damped by the accumulated phase variance along the path, c₁ ~ exp(−N²σ_Θ²/2).

**Failure point, stated exactly:** both the bare harmonic amplitudes c_k and the variance law σ_Θ²(L, a) are functionals of the driven kernel's stationary measure — the corpus's #1 gap. Without the kernel there is no honest estimate of either factor; with generic diffusive phase accumulation σ_Θ² ~ L/a, the damping exponent for any laboratory path is astronomically large and κ is exactly zero to all conceivable precision, but "generic" is doing unearned work in that sentence. *Changes if:* the stationary measure of §D.5 is exhibited even approximately; then this route yields the only **candidate-discriminating** Sorkin prediction on the table (N distinguishes lattices). Proposed negatives-ledger entry with that exact changes-if.

## 4. Route 3 — configuration counting (seam i). **Derived shape; the floor.**

*Consumes:* finite grain count (any lattice family member). *Level:* family.

If probability is a fraction of substrate microconfigurations, quadraticity holds only up to counting resolution: the functional cannot resolve probability differences below ~1/N_config, giving a systematic rounding-scale residual

> **κ ~ (a/L_coh)³ = 1/N_config.**

Benchmarks: grain-scale a (Planck): κ ~ 10⁻⁹⁰ per (10 μm)³ coherence volume; cell-scale a (fm): κ ~ 10⁻³⁰. Again decades-safe, again a definite nonzero floor where the incumbent inputs zero. This is the weakest of the three as physics (the counting reading of the measure is itself a premise the corpus holds at arm's length) but the cheapest to state and the hardest to evade: *any* finite-configuration substrate owes at least this floor. **Proposed tier: FRAMING with a derived floor formula, gated on the counting reading of the measure.**

## 5. Summary table and proposed ledger action

| route | seam attacked | shape | magnitude at bench | level | status |
|---|---|---|---|---|---|
| 1 saturation | linearity | κ = c₁u/ρ_sat, **κ ∝ intensity** | 10⁻³⁸–10⁻¹²⁴ | family (ρ_sat fork) | CANDIDATE; shape testable via intensity-slope reanalysis now |
| 2 Z_N | U(1) equivariance | κ ~ c₁(kernel)·e^{−N²σ_Θ²/2}, N ∈ {6,12} | not computable | **candidate (V3)** | BLOCKED on #1 gap; negatives-ledger row proposed |
| 3 counting | measure resolution | κ ~ (a/L_coh)³ | 10⁻³⁰–10⁻⁹⁶ | family | FRAMING + floor |

Proposed corpus actions: (a) register the definitional fence of §0 (κ_TWT = residual after QM looped-path accounting) before any route is banked — without it every route is unfalsifiable against standard QM's own nonzero prediction; (b) bank Route 1's shape claim with its intensity-slope discriminator and the two-scale intercept fork as the registered open fork; (c) file Route 2 as the negatives-ledger entry above — it is the only place in this memo where the D4 pick itself would ever become Sorkin-visible, which is worth preserving precisely because it is currently unreachable; (d) note that all three routes make the *sign* of the corpus's Sorkin exposure favorable: every derived magnitude sits far below current bounds, so the framework is not at risk from existing triple-slit data, while still owing — and now possessing, in two of three routes — an actual number where the incumbents write an axiom.

## Appendix — magnitudes (reproducible one-liner)

ρ_cell = f_π⁴/(ħc)³ with f_π = 130 MeV gives 5.95×10³³ J/m³; ρ_Pl = 4.63×10¹¹³ J/m³; κ₁ = E_γ/(ρV) and κ₃ = a³/V with E_γ = 2.5 eV, V ∈ {(10 μm)³, mm³}, a ∈ {l_P, fm} reproduce every number in §§2 and 4 (computed in-session; arithmetic, not simulation).
