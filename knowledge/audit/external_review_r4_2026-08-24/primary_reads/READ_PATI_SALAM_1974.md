# PRIMARY READ — Pati & Salam, "Lepton number as the fourth 'color'" (1974)

**Date of read:** 2026-08-24
**Worker:** TWT primary-read worker (own web tools; diet = brief only, starved of TWT derivations)
**Target:** J. C. Pati and Abdus Salam, *Lepton number as the fourth "color"*, Phys. Rev. D **10**, 275–289 (1974); Erratum Phys. Rev. D **11**, 703 (1975).
**Occasion:** Round-4 finding F3 (OURS-CONFIRMED) — quarantined prior-art import row. Nothing here is banked. Tier of this file: **read record**. Adjudication stays with the coordinator.

---

## 0. Sources actually fetched, with read-depth tags

| # | Source | URL | Depth | Note |
|---|--------|-----|-------|------|
| S1 | **ICTP preprint IC/74/7**, Pati & Salam, "Lepton number as the fourth colour", Miramare–Trieste, January 1974, 38 pp., marked "*To be submitted for publication*" | `http://web.archive.org/web/20131023143903if_/http://library.ictp.trieste.it/DOCS/P/74/007.pdf` (Wayback capture of `library.ictp.trieste.it/DOCS/P/74/007.pdf`) | **[PRIMARY-FULL — PREPRINT]** | The full 38-page scan. Whole text extracted; **six pages independently re-read as page images** to defeat OCR error (preprint pp. 2, 3, 21, 22, 29, 31). This is the fulltext link INSPIRE itself attaches to record 89207 (= the PRD paper). ICTP's own host is now dead (`ENOTFOUND`); the Wayback capture is the live route. |
| S2 | **Published abstract**, Phys. Rev. D 10, 275 (1974) | `https://inspirehep.net/api/literature/89207` (INSPIRE record 89207) | **[ABS — PUBLISHED]** | Abstract retrieved verbatim. Confirms the published version's four enumerated consequences. |
| S3 | **Published full text (APS)** | `https://link.aps.org/doi/10.1103/PhysRevD.10.275` | **[UNREACHABLE]** | HTTP 403. Not circumvented. |
| S4 | **Erratum**, Phys. Rev. D 11, 703 (1975) — metadata | `http://web.archive.org/web/20260211101010/https://journals.aps.org/prd/abstract/10.1103/PhysRevD.11.703.2` | **[ABS — metadata only]** | Existence, authors, date (1 Feb 1975), DOI `10.1103/PhysRevD.11.703.2` confirmed. APS errata pages carry **no abstract text**. |
| S5 | **Erratum full text** | `https://link.aps.org/pdf/10.1103/PhysRevD.11.703.2` | **[UNREACHABLE]** | HTTP 403; no Wayback capture of the PDF. **The erratum's content was NOT read.** |
| S6 | J. C. Pati (solo), "Lepton number as the fourth colour", conference proceedings pp. III-85–III-88 (1974) | `https://inspirehep.net/files/3e03067e904f967d6c18f412650d8200` | **[PRIMARY-FULL — DIFFERENT DOCUMENT]** | **Not the paper.** A Pati-only conference talk whose own ref. 4 is "*J C Pati and Abdus Salam, Phys. Rev. D, 1 July 1974*" — i.e. it *cites* the target paper. Used **corroboratively only**; no verdict below rests on it. |

### Read-depth caveat (must travel with any citation from this dossier)

**What was read in full is the PREPRINT (S1), not the published PRD article (S3, unreachable).** The published abstract (S2) and the preprint abstract agree essentially word-for-word, including the enumerated consequence (3) that carries the whole of Claim 2 — strong evidence the body is unchanged. But **page-level wording of the published article was not verified.** Every verbatim quote below is therefore cited to **IC/74/7 page N**, never to "PRD 10, 275 p. N". Separately, **the 1975 erratum was not read** (S5); a residual, unquantified risk that it touches one of these three claims remains open.

---

## 1. Claim-by-claim verdicts

### CLAIM 1 — "Lepton number as the fourth 'color': a four-element set (three colours + lepton), i.e. SU(4)_c ⊃ SU(3)_c × U(1)_{B−L}, with B−L the U(1) inside SU(4)."

**Verdict: VERIFIED-AT-PRIMARY on the four-element set and on SU(4) ⊃ SU(3) × U(1). PARTIAL / NOT-IN-PRIMARY on the specific label "U(1)_{B−L}".**

Evidence, IC/74/7 §II, p. 3 — the four-element set is the paper's opening move. Three colours (a,b,c) "represent baryonic matter (B = 1)", and:

> "the fourth (d or lilac) represents lepton number L" — *IC/74/7, §II, p. 3*

and the group statement:

> "extending the gauge symmetry SU(3') of the three colours (a,b,c) to SU(4')" — *IC/74/7, §II, p. 3*

The **SU(4) ⊃ SU(3) × U(1)** decomposition is explicit twice. In §II, p. 4, contrasting with their earlier paper I:

> "only the subgroup SU(3') x U(1') of SU(4') was gauged" — *IC/74/7, §II, p. 4*

and in footnote 11, p. 31, naming the U(1)'s generator inside SU(4') outright:

> "the U(1) is given by the charm-generator √(2/3) (F′₁₅) of SU(4')" — *IC/74/7, fn. 11, p. 31*

The concrete fermion realization is a 4×4 array, verified from the page image (p. 3): valency column (p, n, λ, χ) ⊗ colour row (a, b, c, d), whose **fourth-colour column is the lepton quartet** — the paper prints `p_d = ν`, `n_d = e⁻`, `λ_d = μ⁻`, `χ_d = ν′`.

**Two precisions the coordinator should not lose:**

1. **The paper never writes "U(1)_{B−L}".** It names the generator `F′₁₅` of SU(4') and calls it — by analogy with the flavour-SU(4) charm generator — the "charm-generator". `F′₁₅ ∝ diag(1,1,1,−3)` in colour space *is* the B−L direction, so the modern identification is substantively right; but it is **later terminology, not the 1974 paper's own**. The string "B−L" occurs in the paper exactly once, and there it names the **violated** quantity, not the gauge generator (see Claim 2).
2. **Normalization differs from the modern convention.** The 1974 paper sets **B = 1 per quark** (see p. 2: "baryonic quarks (B = 1)"; and §6.7 treats the proton as "a three-quark composite (B = 3)"). Modern B−L is normalized to B = 1/3 per quark. Quoting a "B−L" statement from this paper without carrying that normalization is a live referent-drift hazard.

---

### CLAIM 2 — the adjudication's sharpening: "minimal Pati–Salam conserves B−L exactly and does NOT predict proton decay — its leptoquarks mediate ΔB=ΔL processes such as K_L→μ±e∓, not p→e⁺π⁰."

**Verdict: SPLIT. The "does NOT predict proton decay" half is CONTRADICTED as an attribution to the 1974 primary. The "conserves B−L exactly" half is CONTRADICTED for the paper's main branch and true only of its other branch. The "not p→e⁺π⁰" half is VERIFIED. The "K→μe" half is VERIFIED with a wording caveat.**

**This is a finding: the adjudication's sentence over-attributes to the 1974 paper.** It is a fair description of *modern minimal Pati–Salam*; it is not a description of Pati & Salam 1974.

#### (a) The 1974 paper predicts proton decay — explicitly, prominently, and in its own abstract. CONTRADICTED.

The **published abstract** (S2, verbatim) lists as consequence (3):

> "the independent possibility of baryon-lepton number violation in quark and proton decays" — *published abstract, PRD 10, 275 (1974); identical in IC/74/7 abstract*

The Introduction's third general characteristic (p. 2, verified from page image):

> "though the fermion number F = B + L is still conserved" — *IC/74/7, §I, p. 2*

— the full sentence gives "the (logically independent) possibility of baryonic quarks transforming into leptons, with a violation of baryon and lepton number conservation", with that parenthesis attached.

§6.7 is titled **"Violation of baryon and lepton numbers"** and states that the scheme "can lead — through a spontaneous symmetry-breaking mechanism — to a violation of baryon and lepton numbers in the integer charge quark model." It then prints the decay modes (p. 29, verified from page image):

> p → 3ν + π⁺ ; → 4ν + e⁺ or 4ν + μ⁺ ; → 4ν + μ⁺ + e⁺ + e⁻ , etc. — *IC/74/7, eq. (30), §6.7, p. 29*

and urges experimental search: the paper says it is "essential to search for multi-particle decays of the proton". The concluding list's item 7 (same page) is:

> "baryon-lepton number non-conservation in quark and proton decays" — *IC/74/7, §6.7 conclusion, p. 29*

#### (b) "Conserves B−L exactly" — CONTRADICTED for the paper's main branch; and the conserved combination is F = B + L, not B − L.

The paper is **two-branched**, and it says so. The mechanism is spontaneous **W–X mixing**, possible only when the X's and W's can carry the same electric charge:

- **Integer-charge branch** (which the paper "concentrate[s] on, in the main"): §4.4 states the mixing is "leading to a non-conservation of baryon (and lepton) numbers", and then — the paper's single use of the symbol:
  > "The strength of lepton-baryon number (B-L) violating interaction is directly proportional to c₄" — *IC/74/7, §4.4(a), p. 19*
- **Fractional-charge branch**: §4.5 (p. 21, verified from page image) notes the X's are then fractionally charged so X's and W's "can never mix", concluding:
  > "baryon-lepton number conservation is a consequence of the twin postulates" — *IC/74/7, §4.5, p. 21* (the twin postulates being fermion-number and electric-charge conservation)

So B−L conservation in this paper is a **derived property of one branch**, not a property of the scheme. And what is exactly conserved *throughout*, including in the violating branch, is **F = B + L** — the opposite combination from the one the adjudication names. (Consistent with the exotic gauge boson's quantum numbers: footnote 12, p. 31 — "For the fractional charge model these would be (-2/3, -2/3, -2/3)", the modern leptoquark charge, versus (0, −1, −1) in the integer-charge model.)

#### (c) "not p→e⁺π⁰" — VERIFIED, and sharper in the primary than in the adjudication.

The primary excludes two-body proton decay *by selection rule*, exactly as the adjudication's contrast requires (p. 29, verified from page image):

> "The crucial point is that no two- or three-body decays are allowed." — *IC/74/7, §6.7, p. 29*

and footnote 36, p. 31, applying this against the Reines-era experiments:

> "Such decays are forbidden in the model presented in this paper." — *IC/74/7, fn. 36, p. 31*

The primary's reason is **fermion-number conservation**: the minimum final state for a three-quark proton is three neutrinos plus a pion. So the adjudication's "not p→e⁺π⁰" is right — but for a reason the adjudication does not give, and *alongside* a positive proton-decay prediction the adjudication denies.

#### (d) "leptoquarks mediate … K_L→μ±e∓" — VERIFIED in substance; three wording caveats.

The concluding list's item 5 (p. 29, verified from page image):

> "muon-electron number-violating transitions such as K → μ + e decays" — *IC/74/7, §6.7 conclusion, p. 29*

with the immediately following restriction:

> "this is relevant for the 'basic' model only" — *IC/74/7, §6.7 conclusion, p. 29*

Caveats: (i) the paper writes "K → μ + e", **not** the charge-and-CP-specific "K_L→μ±e∓"; (ii) the paper scopes it to the "basic" model only — it does **not** hold in the §2.4 variants where L_e and L_μ are distinct colours; (iii) calling K→μe a "**ΔB=ΔL** process" is loose: K→μe has ΔB = 0 and ΔL = 0 overall, being built from two quark↔lepton (ΔB=ΔL) vertices. The descriptor fits the *vertex*, not the process. Recommend the row say "quark↔lepton (ΔB=ΔL) vertices, giving e.g. K→μe".

---

### CLAIM 3 — "Whether the 1974 paper anticipates Dirac neutrinos / a right-handed neutrino as the fourth-colour lepton partner (the 16th Weyl seat)."

**Verdict: VERIFIED-AT-PRIMARY that a right-handed neutrino exists as the fourth-colour partner. CONTRADICTED that the paper endorses Dirac neutrinos — it treats them as a problem and engineers them away. NOT-IN-PRIMARY for the "16th Weyl seat" framing.**

**(i) ν_R exists, as the fourth-colour partner — VERIFIED.** Both chiralities are full 16-folds: the paper's §2.1 array (p. 3, verified from page image) is written `ψ_{L,R}` with the fourth-colour column `(p_d=ν, n_d=e⁻, λ_d=μ⁻, χ_d=ν′)`, so ν_R and ν′_R are present as the fourth-colour partners of p_R and χ_R. The transformation properties are given as (4,1,4) and (1,4,4) of SU(4)_L × SU(4)_R × SU(4').

**(ii) The neutrinos start as Dirac — VERIFIED verbatim.** Footnote 8, p. 31 (verified from page image):

> "Here ν and ν′ are 4-component objects." — *IC/74/7, fn. 8, p. 31*

**(iii) But the paper does NOT want them Dirac — CONTRADICTED.** §5.2 is titled **"The massless neutrinos"** and opens by calling the situation a problem (p. 22, verified from page image):

> "the model is presented with a dilemma of massive neutrinos" — *IC/74/7, §5.2, p. 22*

The resolution adds two gauge-singlet left-handed fermions ζ^e_L, ζ^μ_L, whose stated purpose is:

> "to ensure the emergence of 2-component massless neutrinos" — *IC/74/7, fn. 8, p. 31*

Diagonalizing the resulting mass matrix leaves, per §5.2, one massless 2-component left-handed state identified with the physical neutrino, plus a massive 4-component fermion. The paper's own field count closes the matter (fn. 8, p. 31):

> "thus contains a total of 16 + 16 + 2 = 34 2-component fields" — *IC/74/7, fn. 8, p. 31*

So the **final** 1974 "basic" model has **34** Weyl fields, not 32, and its physical neutrinos are **massless and 2-component by construction**. Footnote 11 (p. 31) even offers an alternative restricted gauge scheme motivated partly by preserving "masslessness of neutrinos without invoking ζ's".

**(iv) The "16th Weyl seat" framing is NOT-IN-PRIMARY — and is a referent hazard.** The 1974 "16-fold" is **4 valency × 4 colour**, not the SO(10)-style 16 = (15 of one generation) + ν_R. Its lepton quartet (ν, e⁻, μ⁻, ν′) spans what we would now call **two generations of leptons**, and the model contains no third generation. Reading "16-fold" here as "one generation's 16 Weyl seats with ν_R as the 16th" imports a post-1974 structure (Georgi's SO(10), 1974–75) that this paper does not have. If the quarantined row wants the 16th-seat statement, it must attribute it elsewhere.

---

## 2. What the quarantined row may now say (drafted conservatively)

Permitted, each traceable to a verified quote above. The **[PREPRINT-READ]** qualifier travels with all of it.

> **Pati & Salam, Phys. Rev. D 10, 275 (1974)** — "Lepton number as the fourth 'color'". *Read at primary in the ICTP preprint IC/74/7 (Jan 1974, "to be submitted for publication"), full 38-page scan, six pages re-verified as page images; the published PRD body was unreachable (APS 403), though the published abstract was read verbatim and matches. The 1975 erratum was NOT read.*
>
> 1. **Fourth-colour thesis — usable.** The paper's central assumption is that quarks carry four colours, three baryonic and a fourth that "represents lepton number L", the colour gauge group being SU(3') extended to SU(4'). The fourth-colour column of the fermion array is the lepton quartet.
> 2. **SU(4) ⊃ SU(3) × U(1) — usable.** Explicit in the paper (both as the earlier scheme's "SU(3') x U(1') of SU(4')" and in fn. 11, where the U(1) is the SU(4') generator F′₁₅). **The label "U(1)_{B−L}" is NOT the paper's own** — it names F′₁₅ (calling it, by flavour analogy, the "charm-generator"). Cite the substance, not the modern label. **Normalization warning: the paper uses B = 1 per quark (proton B = 3).**
> 3. **Proton decay — the paper PREDICTS it. Do not attribute the modern no-proton-decay statement to 1974.** Consequence (3) of the paper's own abstract is "baryon-lepton number violation in quark and proton decays"; §6.7 gives modes p → 3ν + π⁺, 4ν + e⁺, etc.
> 4. **What is exactly conserved is F = B + L, not B − L.** In the integer-charge branch — the one the paper mainly works — spontaneous W–X mixing violates B and L (the paper's only use of the symbol is "lepton-baryon number (B-L) violating interaction"). B−L conservation holds only in the **fractional-charge** branch, where it is *derived* from fermion-number plus electric-charge conservation. B−L conservation is therefore **branch-dependent in 1974**, not a property of the scheme.
> 5. **p→e⁺π⁰ exclusion — usable, and stronger than assumed.** The paper forbids it by selection rule: "no two- or three-body decays are allowed", on fermion-number grounds.
> 6. **K→μe — usable with scope.** Listed as "muon-electron number-violating transitions such as K → μ + e decays", explicitly "relevant for the 'basic' model only". Do **not** quote it as "K_L→μ±e∓" or describe the *process* as ΔB=ΔL (the vertex is; the process is not).
> 7. **ν_R — usable.** Both ψ_L and ψ_R are 16-folds, so a right-handed neutrino exists as the fourth-colour partner, and the neutrinos are initially "4-component objects".
> 8. **Dirac neutrinos — do NOT attribute to this paper.** §5.2 calls this "a dilemma of massive neutrinos" and adds two gauge-singlet left-handed fields to force massless 2-component physical neutrinos; the final model has "16 + 16 + 2 = 34 2-component fields".
> 9. **"16th Weyl seat" — NOT available from this paper.** Its 16-fold is 4 valency × 4 colour and its lepton quartet spans two lepton generations; the SO(10)-style one-generation 16 is a later structure. Attribute that framing elsewhere.

**Still quarantined / not discharged by this read:**
- The **published PRD body** (page-level wording) — unread; all quotes are preprint-cited.
- The **1975 erratum** (PRD 11, 703) — unread; residual risk it touches any of the above.
- Any claim about "**minimal Pati–Salam**" as a *modern* model (gauged SU(4)_c × SU(2)_L × SU(2)_R with B−L conserved and no proton decay). That statement may well be correct — **but it is not sourced to this paper**, and this read establishes that it cannot be. It needs its own primary or review source before use.

---

## 3. Corroboration (not load-bearing)

S6, the Pati-only 1974 conference talk (a *different* document, which cites the target paper as its ref. 4), independently states the same two-branch structure and the same proton-decay conclusion — quarks decaying to leptons in the integer-charge case, proton stability from the triple-conversion suppression, and allowed multi-body proton decay modes. It is consistent with S1 on every point above. **No verdict in §1 rests on it.**
