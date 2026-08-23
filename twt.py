"""TWT — the Time-Wave Theory math: the MAIN engine FACADE (family split 2026-08-23).

THE ENGINE IS FOUR FILES. Two splits, on two different axes:

  * the 2026-08-13 MAIN / COMPANION split (paper-spine vs deep-dive):
        twt.py + twt_core.py + twt_candidate_v3.py   =  the MAIN engine
        twt_companion.py                             =  the COMPANION engine
  * the 2026-08-23 CORE / CANDIDATE split (family vs instance — RUL-093/RUL-095):
        twt_core.py          FAMILY level: the axioms' consequences, the scale-free
                             structure, the ENDORSED-conditioned results, every GATED
                             raiser. No gravity result and no dimensionful number.
        twt_candidate_v3.py  V3 INSTANCE level: everything consuming a family-tree pick
                             (V3-1 … V3-11) — the pinned calibrations, the D4-sited
                             constructions, the gravity chain, the mass spectra, the
                             LV numerics, the CKM/meta-time material, the kernel dials.
    The companion engine carries the same two-way cut as an in-file SECTION split.

WHY THIS FILE STILL EXISTS. It is a pure compatibility FACADE: it defines no primitive
of its own and re-exports both halves, so `import twt` / `from twt import *` /
`twt.<anything>` keep working byte-for-byte as before for the ~40 probe scripts, the
simulator modules, both harnesses and the companion engine. The split is an
architecture statement, not a migration burden — nothing downstream had to move.

THE TWO DIRECTION INVARIANTS (both suite-guarded, both AST-checked):
  1. twt_core.py must NEVER reference a name defined in twt_candidate_v3.py — the
     family may not depend on the instance. The reverse edge is the allowed one.
  2. the MAIN engine (any of these three files) must NEVER import twt_companion.

WHERE THE TIERS LIVE. Nowhere in this file, and not in the file boundary either. Each
quantity is DERIVED / INPUT / GATED / FRAMING per its own docstring; the CORE side
additionally carries `CORE_PROVENANCE`, the registry of the THIRD commitment class —
CORE results that ride an ENTERED empirical datum or a POSITED premise rather than the
axioms alone (the charge anchor and P4-P7, the RH-singlet datum, A-P2'). CORE is not a
synonym for unconditional; read that registry before quoting a CORE result as such.

Verify with:  python twt_test.py && python twt_companion_test.py
(both harnesses; the check counts are printed at the end of each).
"""
from twt_core import *            # noqa: F401,F403  — the family half
from twt_candidate_v3 import *    # noqa: F401,F403  — the V3-instance half

import twt_core as _twt_core
import twt_candidate_v3 as _twt_candidate_v3

# CONSERVATION OF THE PRIVATE SURFACE. `import *` carries public names only, but the
# COMPANION engine imports six `_`-helpers BY NAME from `twt` (twt_companion.py:31),
# and probe scripts may do the same. Re-expose every module-level `_name` from both
# halves so the facade's namespace is a superset of the pre-split twt.py namespace —
# the harness pins this as an executable conservation check, it is not a convention.
# CORE wins a name collision (shared helpers live on the CORE side by construction).
for _m in (_twt_core, _twt_candidate_v3):
    for _n, _o in vars(_m).items():
        if _n.startswith("_") and not _n.startswith("__"):
            globals().setdefault(_n, _o)
del _m, _n, _o
