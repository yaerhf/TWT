# TWT verification engine

Papers and executable verification suite for **Time-Wave Theory (TWT)** — a structural-derivation
programme deriving Standard-Model *structure* (signature, quantum postulates, gauge content,
charges, generation count) from a four-dimensional Euclidean Clifford substrate carrying a wave,
with one named unbuilt object gating every magnitude in it.

**Yaer Aharon Haddad Fennech** · Independent Researcher · hfyaer@gmail.com

**If you are reviewing, read `TWT_core_paper.md` first** — about twenty-five pages, and it is the
whole argument: TWT-Core as a *family* of theories, what the family derives with no candidate at
all, what that costs against the alternatives, what would kill it, and its first candidate member
V3 with V3's two already-measured wounds stated by the author rather than found by the reader.
`TWT_foundational_paper.md` is the **instance dossier** behind it — V3 at full technical depth —
and is meant to be consulted by section, not read through.

This repository also holds the framework's **falsification surface**. Every algebraic claim the
papers make is encoded here as an executable assertion, so a reviewer can check the mathematics
without taking anything on trust.

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

Expected output: `ALL 434 CHECKS PASSED across 10 modules.` (On Windows, set `PYTHONUTF8=1` first.)

The engine is split in two. `twt_test.py` above runs the **main** harness; the deep-dive layer
has its own:

```bash
python twt_companion_test.py
```

Expected output: `ALL 87 COMPANION CHECKS PASSED across 7 modules.` — 521 checks in total.

## What is in here

| File | Contents |
|---|---|
| `TWT_core_paper.md` | **The paper — start here.** ~25 pp: TWT-Core as a *family* (seven axioms, one refusal), what the family derives with no candidate at all, what that costs against the Standard Model and against the interpretations of quantum mechanics, what would kill it, and its first candidate member V3 with V3's two already-measured wounds. Self-contained; it cites the dossier below by section but does not depend on it. |
| `TWT_foundational_paper.md` | The **instance dossier**: V3 at full technical depth, Parts A–E. Not a second paper — the reference volume behind the Core paper's claims. |
| `TWT_foundational_paper_companion.md` | The bookkeeping volume: result index with per-result tiers, dependency graph, engine ↔ paper map, import registry, falsifier registries, development log. |
| `twt.py` | The substrate oracle, main engine — the dossier's spine. Clifford `Cl(4,0)` / `Cl(4,1)` algebra, the D4 lattice layer, spinor and grade machinery, and one function per banked result. Each carries a docstring stating its **status tier** and the premises it consumes. |
| `twt_test.py` | The main harness — run it; the expected pass line is quoted above. |
| `twt_companion.py` | The companion engine: probe-layer algebra, deprecated items, fine demonstrations. It imports the main engine; the main engine never calls it. |
| `twt_companion_test.py` | The companion harness — likewise. |
| `TWT_NEGATIVES_LEDGER.md` | The negatives ledger — sixty-plus dead ends and located gaps recorded as tried → failed-because → would-change-if entries (N0–N57 with primed variants). Closed doors, published. |
| `TWT_FAMILY_TREE.md` | The candidate's pick register: every load-bearing choice V3 makes, the menu it came from, the result that required it, and what un-picks it. |
| `TWT_COMPARATIVE_LEDGER.md` | The comparative ontological-debt ledger — the itemized accounting behind the Core paper's §3, including the entries that grade against this framework. |
| `D4_lattice_quartic_isotropy.md` | A standalone lattice result (dimension-eight rotational anisotropy on D4), written to stand without TWT; self-contained reproduction script in its Appendix A. |
| `COVER_NOTE.md` | What to check, in what order, and where the work is weakest. Its §0 is addressed to language models. |

Every `(R-NNN)` marker in the dossier resolves to a row in the companion's Result Index, which
names the result's tier, the engine primitive that checks it, and its dependencies. That chain —
prose claim → indexed tier → executable assertion — is the thing to audit. The Core paper carries
no result numbers by design; its "Where the detail is" table maps its sections onto the dossier's.

## How to read a result

Every primitive's docstring opens with its tier, and the tiers are the point:

- **DERIVED** — computed from the substrate axioms. `-A` marks a closed algebraic identity;
  `-conditional` marks a result that holds given a *named* premise, stated in the docstring.
- **INPUT** — an empirical constant or discrete choice taken from data and **counted** against
  the framework's parameter budget (four counted substrate inputs, plus the measured `G_N`,
  plus one provisionally counted hadron-sector determination — see the paper's §E.2.1 for the
  counting convention and the retirement conditions).
- **FIT** — tuned to data. Labeled and counted; never presented as derived.
- **CANDIDATE / FRAMING** — a proposed mechanism or a structural identification whose value or
  closure is explicitly open.
- **GATED** — a magnitude that depends on the framework's open dynamics. These **raise an
  exception** instead of returning a number.

That last one is worth exercising directly:

```python
import twt
twt.alpha_em_value()       # -> raises: the fine-structure magnitude is NOT derived
twt.texture_tetrad()       # -> raises: the absolute gravitational coefficient is NOT derived
twt.qcd_collider_phenomenology()   # -> raises: gated on the open substrate dynamics
```

The framework refuses to hand you numbers it has not earned. If you are auditing it, that
boundary is the first thing to probe.

**And the boundary inside the charge sector is machine-readable, which is the other thing to
probe.** The charge results are two claims at two different strengths, and the engine partitions
them rather than asking you to take the split on trust:

```python
import twt
twt.charge_sector_provenance()   # the partition itself: which charge-block primitives COMPUTE
                                 # and which ASSIGN. The suite asserts it is total, so an
                                 # unclassified addition fails the harness.
twt.charge_normalization_anchor_free()
                                 # the derived half: Q_p + Q_e = 0 IDENTICALLY in the charge
                                 # normalization constant — it holds for every value of it, so
                                 # nothing was tuned to make the two cancel. Returns the breaking
                                 # counterfactual (2c != 0) in the same object.
twt.charge_assignment_from_anchor()
                                 # the entered half: the 15-value spectrum {0, ±1/3, ±2/3, ±1}
                                 # is an ASSIGNMENT riding four named structural premises (P4–P7)
                                 # plus an entered anchor — not a topological output. The anchor
                                 # is a parameter, so the counterfactual runs.
                                 # (`winding_charge` survives only as a labeled legacy alias so
                                 #  that older citations resolve; no winding is computed in it.)
twt.weinberg_sin2()              # 0.375 — sin²θ_W = 3/8, a normalization identity at unification
                                 # over that assigned table, NOT a prediction of the measured
                                 # 0.2312. `charge_sector_provenance` puts it on the assigned side.
```

## Some checks worth running first

```python
import twt
twt.gammas()                        # observer γ-matrices satisfy the Cl(1,3) Dirac relations
twt.cl_dimension()                  # Cl(4,0) ≅ Cl(1,3) ≅ M₂(ℍ) — the signature-emergence algebra
twt.weak_su2_menu_exhaustion()      # the weak host: the menu of 3-dim su(2) subalgebras of the
                                    # substrate's grade-2 rotation algebra, COMPUTED CLOSED at
                                    # three conjugacy classes — one the same assignment mirrored,
                                    # one refuted by the right-handed fermions' weak-singlet
                                    # character. So the weak sector is a chiral factor FORCED,
                                    # given one endorsed premise (that the host sits inside that
                                    # algebra at all) plus that one datum read from experiment.
twt.generation_spectrum()           # the 15-state Weyl spectrum of one generation (assigned side)
twt.koide_from_c(2**0.5)            # Koide K = 2/3 at the Brannen coefficient c = √2 (an INPUT)
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
- **Documents** (the Core paper, the dossier, the companion, the ledgers): © 2026 Yaer Aharon Haddad Fennech, all rights reserved,
  readable for review, citation and discussion — see `LICENSE-DOCS`. Deliberately conservative
  pending formal publication.
- **The physics itself is not licensed and cannot be.** Copyright covers this expression of it,
  not the mathematics or the theory. Reimplementing, criticising, refuting or extending the
  physics needs no permission from anyone.

## Status

This is a framework under construction, and it says so throughout. The open frontier — the
driven-dissipative substrate dynamics that gates every coupling magnitude — has its own section
in the dossier (§D.5), and the named structural premises on which otherwise-derived results still
rest are tabulated at §E.2.2. Citation verification against primary sources is in progress
at this revision; the dossier flags the affected citations in place.
