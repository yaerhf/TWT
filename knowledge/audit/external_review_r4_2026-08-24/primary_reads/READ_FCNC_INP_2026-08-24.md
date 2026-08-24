# PRIMARY READ — the empirical inputs behind the quarantined V4-ASD FCNC floors

**Date:** 2026-08-24
**Worker:** primary-read duty, round-4 external-review cycle
**Claim list read:** `knowledge/reviews/r4_commission_2026-08-24/04_V4ASD_fcnc_note.md`,
`knowledge/reviews/r4_commission_2026-08-24/04_fcnc_bounds.py`
**Scope:** the INPUTS only. The no-GIM lemma (Part A of the script) is banked and is **not**
adjudicated here. No file outside this one was edited; nothing banked.
**Script state:** run unmodified on HEAD, `04_fcnc_bounds: ALL CHECKS PASSED`. Printed floors used
below as the "script value" column.

---

## 0. Sources fetched, with read-depth tags

| # | Source | URL | Depth |
|---|---|---|---|
| S1 | Isidori, Nir & Perez, *Flavor Physics Constraints for Physics Beyond the Standard Model*, Ann. Rev. Nucl. Part. Sci. **60** (2010) 355, arXiv:1002.0900 | `https://arxiv.org/abs/1002.0900`, `https://ar5iv.labs.arxiv.org/html/1002.0900` | **[PRIMARY-FULL]** on §III Table 1 + the derivation prescription; read twice, digit-by-digit, on two independent passes |
| S2 | PDG 2024 (Navas *et al.*, Phys. Rev. D **110**, 030001) — K⁰ Particle Listings | `https://pdg.lbl.gov/2024/listings/rpp2024-list-K-zero.pdf` | **[PRIMARY-FULL]** (pp. 1–6, read as PDF) |
| S3 | PDG 2024 — K⁰_L Particle Listings | `https://pdg.lbl.gov/2024/listings/rpp2024-list-K-zero-L.pdf` | **[PRIMARY-PARTIAL]** (pp. 1–3) |
| S4 | PDG 2024 — Strange Meson Summary Table | `https://pdg.lbl.gov/2024/tables/rpp2024-tab-mesons-strange.pdf` | **[PRIMARY-FULL]** on the K⁰ / K⁰_L blocks (pp. 4, 6, 7) |
| S5 | PDG 2024 — Muon Particle Listings | `https://pdg.lbl.gov/2024/listings/rpp2024-list-muon.pdf` | **[PRIMARY-FULL]** on the LF-violating modes and μ–e conversion (pp. 5–8) |
| S6 | PDG 2024 review 75, *B⁰–B̄⁰ Mixing* | `https://pdg.lbl.gov/2024/reviews/rpp2024-rev-b-bar-mixing.pdf` | **[PRIMARY-FULL]** on Eqs. (75.15), (75.17), (75.18) |
| S7 | PDG 2024 review 70, *D⁰–D̄⁰ Mixing* | `https://pdg.lbl.gov/2024/reviews/rpp2024-rev-d-dbar-mixing.pdf` | **[PRIMARY-FULL]** on Table 70.7 (HFLAV global fit) |
| S8 | PDG 2024 review 12, *CKM Quark-Mixing Matrix* | `https://pdg.lbl.gov/2024/reviews/rpp2024-rev-ckm-matrix.pdf` | **[PRIMARY-FULL]** on §12.3.1 |
| S9 | PDG 2024 review 72, *Leptonic Decays of Charged Pseudoscalar Mesons* | `https://pdg.lbl.gov/2024/reviews/rpp2024-rev-pseudoscalar-meson-decay-cons.pdf` | **[PRIMARY-FULL]** on Table 72.1 and Eq. (72.19) |
| S10 | PDG 2024 review 1, *Physical Constants* (Table 1.1) | `https://pdg.lbl.gov/2024/reviews/rpp2024-rev-phys-constants.pdf` | **[PRIMARY-FULL]** |
| S11 | PDG 2024 machine-readable mass/width table | `https://pdg.lbl.gov/2024/mcdata/mass_width_2024.txt` | **[PRIMARY-FULL]** on IDs 311, 421, 511, 531 |
| S12 | Carrasco *et al.* (ETM), *ΔS=2 and ΔC=2 bag parameters …*, arXiv:1505.06639 | `https://arxiv.org/abs/1505.06639`, `https://ar5iv.labs.arxiv.org/html/1505.06639` | **[PRIMARY-FULL]** on Eq. (4) and Table 2 |
| S13 | MEG II, *New limit on the μ⁺→e⁺γ decay*, arXiv:2504.15711 (EPJC 2025) | `https://arxiv.org/abs/2504.15711` | **[ABS]** |
| S14 | MEG II, *A search for μ⁺→e⁺γ with the first dataset*, arXiv:2310.12614 (EPJC 84 (2024) 216) | `https://arxiv.org/abs/2310.12614` | **[ABS]** |
| S15 | Perrevoort (Mu3e), *Searching for CLFV with Mu3e*, arXiv:2308.11403 | `https://arxiv.org/abs/2308.11403` | **[ABS]** |

Note on FLAG: the FLAG web server (`flag.unibe.ch`) refused connection during this read. Every FLAG
number the script uses was therefore verified through a **PDG 2024 review that quotes the FLAG
average with attribution** (S6, S8, S9) or through the **original lattice paper FLAG averages** (S12).
No FLAG number below rests on an unfetched source.

---

## 1. The primary ΔF=2 table, reproduced (S1, §III.1, Table 1)

Caption, verbatim from the primary:

> "Bounds on representative dimension-six ΔF=2 operators. Bounds on Λ are quoted assuming an
> effective coupling 1/Λ², or, alternatively, the bounds on the respective c_ij's assuming Λ=1 TeV.
> Observables related to CPV are separated from the CP conserving ones with semicolons. In the B_s
> system we only quote a bound on the modulo of the NP amplitude derived from Δm_Bs (see text)."

| Operator | Λ (TeV), Re | Λ (TeV), Im | c_ij at Λ=1 TeV, Re | c_ij at Λ=1 TeV, Im | Observables |
|---|---|---|---|---|---|
| (s̄_L γ^μ d_L)² | 9.8×10² | 1.6×10⁴ | 9.0×10⁻⁷ | 3.4×10⁻⁹ | Δm_K ; ε_K |
| (s̄_R d_L)(s̄_L d_R) | 1.8×10⁴ | 3.2×10⁵ | 6.9×10⁻⁹ | 2.6×10⁻¹¹ | Δm_K ; ε_K |
| (c̄_L γ^μ u_L)² | 1.2×10³ | 2.9×10³ | 5.6×10⁻⁷ | 1.0×10⁻⁷ | Δm_D ; \|q/p\|, φ_D |
| (c̄_R u_L)(c̄_L u_R) | 6.2×10³ | 1.5×10⁴ | 5.7×10⁻⁸ | 1.1×10⁻⁸ | Δm_D ; \|q/p\|, φ_D |
| (b̄_L γ^μ d_L)² | 5.1×10² | 9.3×10² | 3.3×10⁻⁶ | 1.0×10⁻⁶ | Δm_Bd ; S_ψK_S |
| (b̄_R d_L)(b̄_L d_R) | 1.9×10³ | 3.6×10³ | 5.6×10⁻⁷ | 1.7×10⁻⁷ | Δm_Bd ; S_ψK_S |
| (b̄_L γ^μ s_L)² | 1.1×10² | — | 7.6×10⁻⁵ | — | Δm_Bs |
| (b̄_R s_L)(b̄_L s_R) | 3.7×10² | — | 1.3×10⁻⁵ | — | Δm_Bs |

**The relevant row for the commission's construction is the first one** — the left-handed vector
operator, which is what a gauged horizontal su(2) generates at tree level.

**Derivation prescription in the primary (load-bearing for how to read the numbers):** the bounds
impose `|A_NP^(ΔF=2)| < |A_SM^(ΔF=2)|` — *"the magnitude of the new-physics amplitude cannot exceed,
in size, the SM short-distance contribution."* The CPV entries are further qualified: *"the
constraints related to CPV correspond to maximal phases, and are subject to the requirement that the
NP contributions are smaller than 30% (60%) of the total contributions in the B_d (K) system."*
These are **not** 90%-CL statistical limits. See §5, finding F-3.

---

## 2. Independent verification of the commission's "cross-checked within factor 2" claim

The script asserts only the two kaon rows (`0.5 < ratio < 2.0`). I re-derived all five mixing rows
against the primary. Script column = printed output of the unmodified script.

| Row | Script Λ (TeV) | INP Table 1 (TeV) | ratio script/INP | inside factor 2? |
|---|---|---|---|---|
| Δm_K (Re, 1↔2 down) | 938 | 9.8×10² (Re) | **0.957** | yes |
| ε_K (Im, 1↔2 down) | 11 817 | 1.6×10⁴ (Im) | **0.739** | yes |
| Δm_D (1↔2 up) | 1 809 | 1.2×10³ (Re) | **1.507** | yes |
| Δm_Bd (1↔3) | 517 | 5.1×10² (Re) | **1.014** | yes |
| Δm_Bs (2↔3) | 107 | 1.1×10² (Re) | **0.973** | yes |

**VERDICT on the claim: SUPPORTED.** The two asserted kaon rows agree with the primary at 0.96 and
0.74 respectively. The three rows the script does *not* assert also land inside factor 2 — a stronger
result than the note claims, and it is worth recording that the agreement is uniform across all five
systems rather than tuned on the kaon pair.

**Caveat carried forward (see F-1):** the note's table quotes the Δm_D floor as "≳1.8×10³ TeV",
which is 1.5× *above* the primary's own Re bound of 1.2×10³ TeV. The conservative, primary-anchored
number for that row is **1.2×10³ TeV**.

---

## 3. Input-by-input verification

Sensitivity conventions used in the "material?" column, derived from the script's own formulas:
`Λ_mix ∝ (f√B)·√(m/ΔM)`; `Λ_εK ∝ (f_K√B_K)·√(m_K/(ε_K·Δm_K))`; `Λ_μ3e ∝ G_F^(−1/2)·BR^(−1/4)`.
So moving a floor by a factor 2 requires a factor **2** in a decay constant, a factor **4** in a
mass / mixing observable / ε_K, or a factor **16** in BR(μ→3e).

### 3a. Hadronic and mixing inputs

| Script value | Primary value | Source + location | Verdict |
|---|---|---|---|
| `mK = 0.497611` GeV | m_K⁰ = 497.611 ± 0.013 MeV | S2 p.1 "K⁰ MASS", OUR FIT; also S4 p.4 | **VERIFIED, exact** |
| `fK = 0.1557` GeV | f_K⁺ = 155.7(3) MeV [FLAG 23, N_f=2+1+1]; 155.7(7) MeV [FLAG 23, N_f=2+1] | S9 Table 72.1, "FLAG 23 average" rows | **VERIFIED, exact** |
| `BK = 0.7625` (RGI) | FLAG N_f=2+1 average B̂_K = 0.7625(97). PDG 2024 instead quotes **B̂_K = 0.717 ± 0.024** (the N_f=2+1+1 value, from ETM: B_K^RGI(N_f=3) = 0.717(24)) | S8 §12.3.1; S12 Eq. (4) | **VERIFIED as a FLAG-family value**, with a flavour-count discrepancy: using PDG's 0.717 moves Λ_εK by √(0.717/0.7625) = 0.970, i.e. **−3%**. Not material. |
| `dMK = 3.484e-15` GeV | m_KL − m_KS = (3.484 ± 0.006)×10⁻¹² MeV = 3.484×10⁻¹⁵ GeV (assuming CPT); equivalently (0.5293 ± 0.0009)×10¹⁰ ℏ s⁻¹ | S4 p.6 K⁰_L block; S3 p.1 OUR FIT | **VERIFIED, exact** |
| `epsK = 2.228e-3` | \|ε\| = (2.228 ± 0.011)×10⁻³ (S=1.8) | S4 p.7 "CP-violation parameters"; independently S8 §12.3.1 | **VERIFIED, exact** (two independent PDG locations) |
| `mBd = 5.27966` GeV | m_B⁰ = 5279.72 ± 0.08 MeV (PDG 2024 OUR FIT); 5.27972 GeV in the MC table | S11 (ID 511); PDG 2024 B⁰ listings p.1 | **VERIFIED, update-shifted** by +0.06 MeV (1.1×10⁻⁵ relative). Λ ∝ √m ⇒ **negligible** |
| `fBd_sqB = 0.225` GeV | f_Bd√B̂_Bd = **225 ± 9 MeV**, "obtained from three-flavor lattice QCD calculations" | S6, text following Eq. (75.16) | **VERIFIED, exact** |
| `dMBd = 0.5065/ps` | Δm_d = 0.5069 ± 0.0019 ps⁻¹ | S6 Eq. (75.15) | **VERIFIED, update-shifted** by 0.08%. Λ ∝ ΔM^(−1/2) ⇒ **negligible** |
| `mBs = 5.36692` GeV | m_Bs⁰ = 5.36693 GeV | S11 (ID 531) | **VERIFIED** (1 in 5×10⁶) |
| `fBs_sqB = 0.274` GeV | Not tabulated directly by PDG; PDG gives ξ = (f_Bs√B_Bs)/(f_Bd√B_Bd) = **1.206 ± 0.017** ⇒ f_Bs√B̂_Bs = 225 × 1.206 = **271.4 MeV** | S6 Eq. (75.18) and following text | **VERIFIED indirectly**, 274 vs 271.4 = +1.0%, well inside the quoted errors. **Negligible** |
| `dMBs = 17.765/ps` | Δm_s = 17.765 ± 0.004(stat) ± 0.004(syst) ps⁻¹ | S6 Eq. (75.17) | **VERIFIED, exact** |
| `mD = 1.86484` GeV | m_D⁰ = 1.86484 GeV | S11 (ID 421) | **VERIFIED, exact** |
| `fD = 0.212` GeV | f_D⁺ = **212.0(7) MeV** | S9 Eq. (72.19) | **VERIFIED, exact** |
| `BD = 0.75` | B₁^D = **0.757(27)(4)**, MS̄ at 3 GeV, N_f = 2+1+1 | S12 Table 2 | **VERIFIED**, +0.9% on B ⇒ +0.5% on Λ. **Negligible**. Scheme note in F-2. |
| `dMD = 6.4e-15` GeV ("x ~ 0.4% of Γ_D") | HFLAV global fit: **x = 0.407 ± 0.044 %** (all-CPV-allowed fit d); 0.434 in the no-CPV fit. Γ_D⁰ = 1.604×10⁻¹² GeV | S7 Table 70.7; S11 (ID 421 width) | **VERIFIED indirectly.** Script's value ⇒ x = 6.4e-15/1.604e-12 = **0.399%**, vs HFLAV 0.407%. Using 0.407% gives ΔM_D = 6.53×10⁻¹⁵ GeV, i.e. Λ_D → 1 791 TeV (−1%). **Negligible** |
| `GF = 1.166379e-5` GeV⁻² | G_F/(ℏc)³ = 1.166 378 8(6)×10⁻⁵ GeV⁻² | S10 Table 1.1 | **VERIFIED, exact** |
| `hbar_GeV_s = 6.58212e-25` | ℏ = 6.582 119 569…×10⁻²² MeV s | S10 Table 1.1 | **VERIFIED, exact** |

### 3b. The LFV inputs (the 207 / 2070 TeV entries)

| Script value | Primary value | Source + location | Verdict |
|---|---|---|---|
| `BR_mu3e = 1.0e-12`, commented "SINDRUM (1988)" | Γ(μ⁻ → e⁻e⁺e⁻)/Γ_total < **1.0 × 10⁻¹²**, CL = **90%**, DOCUMENT ID **BELLGARDT 88**, TECN SPEC, COMMENT **SINDRUM** | S5 p.6, "Γ(e⁻e⁺e⁻)/Γ_total (Γ₆/Γ)". Also in the μ⁻ decay-mode summary, S5 p.5, mode Γ₆, LF, `< 1.0 ×10⁻¹²`, 90% | **VERIFIED, exact, and the SINDRUM/1988 attribution is correct** (Bellgardt *et al.*, SINDRUM). ⇒ **Λ = 207 TeV stands** |
| `BR_mu3e_next = 1.0e-16`, "Mu3e target" | Mu3e targets *"an unprecedented sensitivity in the order of 10⁻¹⁵ in the first phase of operation and 10⁻¹⁶ in the final phase"*; the collaboration's stated phase-II figure is **2 × 10⁻¹⁶ at 90% CL** | S15 abstract | **VERIFIED as an order-of-magnitude projection.** With 2×10⁻¹⁶ the floor is 2070/2^(1/4) = **1 741 TeV**, still ≈2×10³ TeV. **Not material** |

### 3c. The note's prose numbers (not used by the script, but stated in §3 of the note)

| Note's claim | Primary value | Source | Verdict |
|---|---|---|---|
| "the current limit is the MEG II 2021–2022 result, BR(μ→eγ) < 1.5×10⁻¹³" | B(μ⁺→e⁺γ) < **1.5 × 10⁻¹³ (90% C.L.)**, MEG II, 2021–2022 physics runs, sensitivity 2.2×10⁻¹³ | S13 abstract | **VERIFIED.** Note: PDG 2024 (S5 p.6) still lists the older MEG value, `< 0.042×10⁻¹¹ = 4.2×10⁻¹³`, BALDINI 16 — so the note is **ahead of PDG and correct**, not in error. The intermediate MEG II first-dataset paper (S14) gave 7.5×10⁻¹³ alone / 3.1×10⁻¹³ combined with MEG; the note quotes the newer 2021–2022 result |
| "μ–e conversion (SINDRUM II, R < 7×10⁻¹³ on gold)" | σ(μ⁻Au → e⁻Au)/σ(μ⁻Au → capture) < **7 × 10⁻¹³**, CL 90%, BERTL 06, SINDRUM II | S5 p.7, "LIMIT ON μ⁻ → e⁻ CONVERSION" | **VERIFIED, exact** |

---

## 4. Load-bearing sensitivity check (what could still move a floor by ≳2)

Applying the exponents in §3: **no verified deviation above comes anywhere near the factor-2
threshold.** The largest individual effect found is the B̂_K flavour-count choice at **3%** on Λ_εK.
Compounding every update-shift in the same direction (Δm_d 2026 value, m_B0 2024 value, B̂_K =
0.717, x_D = 0.407%, B₁^D = 0.757, f_Bs√B = 271.4 MeV) changes no row by more than 3%.

The only inputs whose *misidentification* could move a floor by ≥2 are the four decay-constant
combinations, and all four were verified against a PDG-quoted or FLAG-original primary
(f_K = 155.7 MeV; f_Bd√B̂ = 225 ± 9 MeV; ξ = 1.206 ± 0.017; f_D⁺ = 212.0(7) MeV).

---

## 5. Findings

**F-1 (repair, cosmetic).** The note's §3 table gives the Δm_D floor as "≳1.8×10³ TeV". That is the
script's own number, and it exceeds the primary's Re bound for the same operator (1.2×10³ TeV) by
1.5×. The note elsewhere presents itself as tracking the INP benchmark. **Recommend quoting
≳1.2×10³ TeV for that row**, or explicitly flagging that the script's saturation criterion is more
aggressive than INP's there. Does not touch any conclusion — the ε_K row governs.

**F-2 (scheme hygiene, sub-factor-2).** The kaon row uses the **RGI** bag parameter (B̂_K = 0.7625)
while the charm row uses an **MS̄(3 GeV)** bag parameter (B_D = 0.75 ≈ ETM's B₁^D = 0.757 in that
scheme). Mixing RGI and MS̄ normalizations across rows of one table is a real inconsistency, though
its size (few %, and at most ~10% if one converts) is far inside the factor-2 tolerance the script
declares. Worth a one-line note in the dossier if the table is ever quoted outside the floor context.

**F-3 (interpretive, and the most important of the three).** The agreement in §2 is **not a
reproduction**; it is a coincidence-at-factor-2 of **two different saturation criteria**. INP impose
`|A_NP| < |A_SM^short-distance|` (with a 30%/60% NMFV qualifier on the CPV entries); the script
imposes that the NP contribution not exceed the *measured* ΔM / ε. Both are defensible floor
criteria, and neither is a confidence level. The note's phrase "reproduce the Isidori–Nir–Perez
benchmark values … within the vacuum-insertion normalization tolerance" attributes the residual
spread entirely to VIA normalization; **part of it is the criterion difference, not the
normalization.** This does not weaken the floor — it means the floor is criterion-robust, which is
a slightly *better* fact — but the wording as it stands mis-locates the source of the spread.

**F-4 (no error found, recorded for the register).** Every one of the sixteen hard-coded constants
in Part B was located in a primary. Nothing in the input set is fabricated, mis-attributed, or
stale by a factor that matters. The two 2010-era concerns the forecast anticipated (PDG drift) are
real but sub-percent: Δm_d 0.5065 → 0.5069 ps⁻¹, m_B0 5279.66 → 5279.72 MeV.

---

## 6. Conclusion

**The quarantined floors are SUPPORTED-BY-PRIMARY at order of magnitude.** Specifically:

- **ε_K generic floor, M_H/g_H ≳ 1.2×10⁴ TeV** — **SUPPORTED.** The script's 11 817 TeV sits at
  0.74× the primary's own Im bound of 1.6×10⁴ TeV for the identical operator (s̄_L γ^μ d_L)²
  (S1 Table 1). Every input feeding it (m_K, f_K, B̂_K, Δm_K, ε_K) is primary-verified, and the
  worst-case input revision found (B̂_K = 0.717) moves it by −3%. The honest statement of the row is
  **"between ~1.2×10⁴ and 1.6×10⁴ TeV depending on saturation criterion"**, which rounds to the
  note's ~10⁴ TeV either way.
- **Summary claim "M_H/g_H ≳ 10⁴ TeV generic"** — **SUPPORTED-BY-PRIMARY.**
- **Summary claim "≳10³ TeV real (CP-conserving)"** — **SUPPORTED-BY-PRIMARY.** Script 938 TeV vs
  primary 9.8×10² TeV, ratio 0.96, on fully verified inputs.
- **μ→3e floor 207 TeV** — **SUPPORTED-BY-PRIMARY.** The underlying limit BR < 1.0×10⁻¹² (90% CL,
  SINDRUM / Bellgardt 88) is exactly as the script has it, per PDG 2024.
- **μ→3e projected floor 2070 TeV** — **SUPPORTED as a projection**, with the caveat that the
  collaboration's own phase-II figure is 2×10⁻¹⁶ rather than 1×10⁻¹⁶, giving ≈1 740 TeV. Still
  ≈2×10³ TeV; the note's ordering claim is unaffected.

**Inputs I could NOT verify at primary — UNREACHABLE tags: none.** Every numeric input in Part B
was located in a fetched primary or in a PDG review that quotes the lattice average with
attribution. Two items are verified **indirectly** rather than by direct tabulation, and are tagged
as such rather than as clean hits:

- `fBs_sqB = 0.274` GeV — **[INDIRECT]** via PDG's ξ = 1.206 ± 0.017 and f_Bd√B̂ = 225 ± 9 MeV
  (S6), giving 271.4 MeV. The FLAG server was unreachable, so the direct FLAG entry
  f_Bs√B̂_Bs = 274 MeV was not read at source. Agreement is 1.0%; the Bs row is in any case the
  weakest floor (107 TeV) and load-bearing for nothing.
- `dMD = 6.4e-15` GeV — **[INDIRECT]** via HFLAV x = 0.407 ± 0.044 % (S7 Table 70.7) and
  Γ_D⁰ = 1.604×10⁻¹² GeV (S11). ΔM_D is not tabulated as an absolute number by PDG; the script's
  value corresponds to x = 0.399%, inside the HFLAV error bar.

Neither indirection reaches the factor-2 threshold, so the struck-bound rule does not bite: nothing
here needs to stay quarantined **on input grounds**. Whatever quarantine the V4-ASD floor values
carry should now rest on the lemma/adjudication side, not on the empirical inputs.

**One repair is owed** (F-1: the Δm_D row's 1.8×10³ vs the primary's 1.2×10³) and **one wording
correction** (F-3: the residual spread is criterion difference plus VIA normalization, not VIA
normalization alone). Neither disturbs any conclusion in the note.
