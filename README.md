# TWT verification engine

Executable verification suite for **Time-Wave Theory (TWT)** — a foundational framework deriving
Standard-Model *structure* (signature, quantum postulates, gauge content, charges, generation
count) from a four-dimensional Euclidean Clifford substrate carrying a wave.

**Yaer Aharon Haddad Fennech** · Independent Researcher · hfyaer@gmail.com

This repository holds the framework's **falsification surface**, not its prose. Every algebraic
claim the paper makes is encoded here as an executable assertion, so a reviewer can check the
mathematics without taking anything on trust.

> **Note on repository history.** This repository was rebuilt in July 2026. Its earlier contents —
> the April 2026 simulation suite (`TWT7.pdf`, the Pauli/Bell/covalent demonstrations, the
> `clifford.g4` and PyTorch algebra cores) — are preserved unchanged on the
> [`archive/pre-v3`](../../tree/archive/pre-v3) branch. That work is superseded, not retracted: the
> premise is the same, but the derivations, tiering and verification suite here replace it
> entirely. Nothing from the old tree is a current claim of the framework.

## Run it

```bash
pip install -r requirements.txt
python twt_test.py
```

Expected output: `ALL 463 CHECKS PASSED across 10 modules.` (On Windows, set `PYTHONUTF8=1` first.)

## What is in here

| File | Contents |
|---|---|
| `twt.py` | The substrate oracle — ~301 public primitives. Clifford `Cl(4,0)` / `Cl(4,1)` algebra, the D4 lattice layer, spinor and grade machinery, and one function per banked result. Each carries a docstring stating its **status tier** and the premises it consumes. |
| `twt_test.py` | The harness: 463 assertions across 10 modules. |
| `TWT_foundational_paper.md` | The paper (Parts A–E): the physics narrative. |
| `TWT_foundational_paper_companion.md` | The bookkeeping volume: result index with per-result tiers, dependency graph, engine ↔ paper map, import registry, falsifier registries, development log. |
| `D4_lattice_quartic_isotropy.md` | A standalone lattice result (dimension-eight rotational anisotropy on D4), written to stand without TWT; self-contained reproduction script in its Appendix A. |
| `COVER_NOTE.md` | **Start here if you are reviewing** — what to check, in what order, and where the work is weakest. Its §0 is addressed to language models. |

Every `(R-NNN)` marker in the paper resolves to a row in the companion's Result Index, which
names the result's tier, the engine primitive that checks it, and its dependencies. That chain —
prose claim → indexed tier → executable assertion — is the thing to audit.

## How to read a result

Every primitive's docstring opens with its tier, and the tiers are the point:

- **DERIVED** — computed from the substrate axioms. `-A` marks a closed algebraic identity;
  `-conditional` marks a result that holds given a *named* premise, stated in the docstring.
- **INPUT** — an empirical constant or discrete choice taken from data and **counted** against
  the framework's parameter budget (four counted substrate inputs, plus the measured `G_N` —
  see the paper's §E.2.1 for the counting convention).
- **FIT** — tuned to data. Labeled and counted; never presented as derived.
- **CANDIDATE / FRAMING** — a proposed mechanism or a structural identification whose value or
  closure is explicitly open.
- **GATED** — a magnitude that depends on the framework's open dynamics. These **raise an
  exception** instead of returning a number.

That last one is worth exercising directly:

```python
import twt
twt.weinberg_sin2()        # -> 0.375   (derived: sin²θ_W = 3/8 at unification)
twt.winding_charge()       # -> exact charge spectrum {0, ±1/3, ±2/3, ±1}
twt.alpha_em_value()       # -> raises: the fine-structure magnitude is NOT derived
twt.texture_tetrad()       # -> raises: the absolute gravitational coefficient is NOT derived
```

The framework refuses to hand you numbers it has not earned. If you are auditing it, that
boundary is the first thing to probe.

## Some checks worth running first

```python
import twt
twt.gammas()                        # observer γ-matrices satisfy the Cl(1,3) Dirac relations
twt.cl_dimension()                  # Cl(4,0) ≅ Cl(1,3) ≅ M₂(ℍ) — the signature-emergence algebra
twt.generation_spectrum()           # the 15-state Weyl spectrum of one generation
twt.charge_normalization_anchor_free()   # Q_p + Q_e = 0 identically in the charge normalization
twt.koide_from_c(2**0.5)            # Koide K = 2/3 at the Brannen coefficient c = √2
```

## Scope, stated plainly

The engine checks **mathematics**, not physics. A passing assertion establishes that an identity
holds in the algebra — it does not by itself establish that the identity means what the paper
says it means. That second question is what the paper and its companion argue, and where review
is genuinely wanted. Conversely, a failing assertion is a real refutation of the corresponding
claim, and reports of one are welcome.

The framework does **not** derive: coupling magnitudes, absolute mass scales, the CKM hierarchy,
the Higgs sector's scale, or QCD dynamics. These are gated on an explicitly named open object
(the driven-dissipative substrate dynamics) and are refused by the engine rather than estimated.

## Contributing / reporting

Refutations, failed assertions, and tier-mislabeling reports are the most valuable contributions.
Open an issue or email the address above.

## Licensing

- **Code** (`twt.py`, `twt_test.py`): **AGPL-3.0** — verbatim licence text in `LICENSE`,
  copyright and terms summary in `NOTICE`. Free to run, study, modify and share; derivatives
  and network services must share source under the same terms. A **commercial licence** is
  available for proprietary use — contact hfyaer@gmail.com.
- **Documents** (paper, companion): © 2026 Yaer Aharon Haddad Fennech, all rights reserved,
  readable for review, citation and discussion — see `LICENSE-DOCS`. Deliberately conservative
  pending formal publication.
- **The physics itself is not licensed and cannot be.** Copyright covers this expression of it,
  not the mathematics or the theory. Reimplementing, criticising, refuting or extending the
  physics needs no permission from anyone.

## Status

This is a framework under construction, and it says so throughout. The open frontier — the
driven-dissipative substrate dynamics that gates every coupling magnitude — has its own section
in the paper (§D.5), and the six named structural premises on which otherwise-derived results
still rest are tabulated at §E.2.2. Citation verification against primary sources is in progress
at this revision; the paper flags the affected citations in place.
