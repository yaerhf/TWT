# -*- coding: utf-8 -*-
import io, os
base = os.path.join(os.path.dirname(__file__), '..', '..', 'corpus')
paper = io.open(os.path.join(base, 'TWT_foundational_paper.md'), encoding='utf-8').read()
engine = io.open(os.path.join(base, 'twt.py'), encoding='utf-8').read()

A = """- **Q** is fixed independently of GMN by the **topological-winding chain** (§C.5.1 / R-054 /
  §C.1.5): `π_3(SU(2))` supplies integer-valuedness (`B ∈ ℤ`). The specific anchor `Q_p = +1`,
  `Q_n = 0` need not be imported: given two structural premises — **(P4)** measured electric
  charge is the eigenvalue of *one* universal linear generator `Q = T_3 + c·Y` across all
  sectors, and **(P5)** `Q` is chirality-independent per defect — the proton–electron relation
  follows for *every* `c` (R-159, below), so the neutrality-of-atoms datum this anchor used to
  consume is **conditionally replaced** rather than imported. Either way it enters no GMN step,
  so the `c = 1/2` check below stays non-circular."""

B = """With these three independent determinations, the relation `Q = T_3 + c · Y` must hold for some
`c` on every blade. **The lepton doublet alone determines `c`** gate-free: `(ν_L: Q = 0,
T_3 = +1/2; e_L: Q = −1, T_3 = −1/2)` with `Y_L = −1` from the e_4-bilinear gives
`Q = T_3 − 1/2 = T_3 + (1/2)·Y` on both members. So `c = 1/2`, fixed by the lepton doublet alone
without any quark content or facet structure."""

C = """— the geometric-algebra form of the consolidated Maxwell equations. The source `J` is the
wavefront projection of a substrate-level **bivector winding** — the L-orbit topological winding
number of the defect, integer-valued, with algebraic carrier in grade 2. Integrated over a
3-surface on the wavefront, this bivector winding gives the integer enclosed charge."""

D = """The source of this strain is the L-orbit winding (per B.5.1), so the topological winding charge
*is* the electric charge — this is what licenses reading the §C.2 charge spectrum `Q` as
electromagnetism."""

E = '''    """[DERIVED-STRUCTURAL, given algebraic Q_e=-1 + Spin(4) B-L + charge neutrality]
    Q from the winding: integer baryon charges (Q_p=+1 anchored via Q_e=-1 from the
    e_4-bilinear on the e_123 lepton blade, §18.2; then Spin(4) B-L conservation +
    overall charge neutrality of an atom force Q_p=+1, Q_n=0) + quark composition
    p=uud, n=udd.  No use of GMN anywhere — the GMN c=1/2 check is downstream.
    Solve 2Qu+Qd=Qp, Qu+2Qd=Qn  (det=3): Qu=(2Qp-Qn)/3, Qd=(2Qn-Qp)/3.

    Tier note (post audit 2026-06-30): pi3_S3_integer_completion only proves B ∈ Z
    (integers), not the specific +1 nor which baryon is positive. The Q_p=+1 anchor
    is the Q_e=-1 algebraic chain + B-L conservation, not gate-free topology alone."""'''

for name, anc, tgt, fn in [("A (C.2.7 bullet Q)", A, paper, "paper"),
                           ("B (C.2.7 c-fixing)", B, paper, "paper"),
                           ("C (B.5.1 source)", C, paper, "paper"),
                           ("D (B.5.4 source)", D, paper, "paper"),
                           ("E (winding_charge doc)", E, engine, "twt.py")]:
    print("anchor %-24s in %-7s : count = %d" % (name, fn, tgt.count(anc)))
