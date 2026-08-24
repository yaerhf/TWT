# READ-ONLY anchor verification for the consolidated patch list (2026-07-29).
# Counts each proposed v3_anchor in its target file. No file is modified.
import io, os
BASE = os.path.join(os.path.dirname(__file__), '..', '..', 'corpus')

F = {
 'twt':    'twt.py',
 'test':   'twt_test.py',
 'paper':  'TWT_foundational_paper.md',
 'comp':   'TWT_foundational_paper_companion.md',
 'legacy': 'TWT_V3_result_index.md',
}
S = {k: io.open(os.path.join(BASE, v), encoding='utf-8').read() for k, v in F.items()}

A = []

# ---- c_reg second pass ----
A.append(('CREG-P1', 'twt', '''    values is therefore IDENTICALLY c_lat (checked below to ~1e-14 for ARBITRARY c_lat) — the
    factor "~21.6" IS c_lat = (Lambda_eff * a)^2, the squared number of lattice spacings in the
    effective cutoff. R-163 says as much itself ("lands exactly on the sakharov_induced_gravity
    form"; its cross-tie Lambda_eff/M_red = 4 pi is c_lat-INDEPENDENT).'''))

A.append(('CREG-P2', 'twt', '''    E = 0 is forced by the SAME left-Spin(4) shift symmetry R-041 uses for xi = 0: an endomorphism
    is a NON-DERIVATIVE quadratic operator phi.W.phi, exactly the class the symmetry forbids
    (checked below on the Weitzenbock shape as well as a generic W). Hence'''))

A.append(('CREG-P3', 'twt', '''    THE TEXTBOOK VALUE IS TWT'S OWN MODE-CONTENT VALUE — and that was NOT a foregone conclusion.
    The excluded readings are computed here and one of them FLIPS THE SIGN OF G:'''))

A.append(('CREG-P4', 'twt', '''        "three_way_resolution": {
            "verdict": "NOT three values of one coefficient — ONE value in three variables/states",
            "1/12": "c_reg in the proper-time-cutoff variable = TWT's own mode-content value (here)",
            "~1.82": "the SAME coefficient with Lambda := 1/a; the excess factor is IDENTICALLY "
                     "c_lat = (Lambda_eff * a)^2 (residual %.1e over arbitrary c_lat)" % ident,
            "~1": "a never-computed paper placeholder — SUPERSEDED, not a rival",'''))

A.append(('CREG-P5', 'test', '''    _ck("THE RECONCILIATION: the two BANKED values are NOT rivals — 1/(16 pi G) = N_eff c_lat/"
        "(192 pi^2 a^2) reads c_reg = c_lat/12 at Lambda := 1/a and c_reg = 1/12 at Lambda := "
        "Lambda_eff = sqrt(c_lat)/a, so their ratio is IDENTICALLY c_lat = (Lambda_eff*a)^2 for "
        "ARBITRARY c_lat (residual < 1e-12) — the factor '~21.6' IS c_lat. The '~1' paper placeholder "
        "was never computed and is SUPERSEDED. What remains OPEN is NOT c_reg but c_lat",
        "IDENTICALLY" in crg["three_way_resolution"]["~1.82"]
        and "SUPERSEDED" in crg["three_way_resolution"]["~1"]
        and "ONE value in three variables" in crg["three_way_resolution"]["verdict"]
        and "c_lat" in crg["three_way_resolution"]["what is actually OPEN"])'''))

A.append(('CREG-P6', 'test', '''    print("        => c_reg = 1/12 for TWT's OWN mode content (6 minimal/Bochner channels, E=0 by the "
          "R-041 shift symmetry); the '~21.6 disagreement' IS c_lat, a change of Lambda-variable; the "
          "OA-LF-ii exposure lives entirely in c_lat/a, NOT in the induced-G coefficient.")'''))

# ---- which-lambda ----
A.append(('LAM-P2', 'comp', '''| `Λ` | Planckian within O(1) | Substrate cutoff; §B.6 bracket `[0.13, 2.5] M_Pl` (widened 2026-07-28: reduced-vs-non-reduced `M_Pl` unit fix + an **OPEN**, unreconciled three-way regulator coefficient `c_reg ∈ {~1 paper, 1/12 engine, ≈1.8 engine}`; no branch settled — R-037) |'''))

A.append(('LAM-P3', 'paper', '''**Two normalizations, kept apart.** `η⁽⁴⁾` is by definition the coefficient of `p⁴/M²_Pl` — the
convention the published bounds are quoted in. The substrate's own natural form is `c · p⁴/Λ²` with
`c = O(1)`, since `Λ` is the substrate cutoff. The two are related by `η⁽⁴⁾ = c · (M_Pl/Λ)²`, so
"the substrate's natural coefficient is unity" means `c = 1`, **not** `η⁽⁴⁾ = 1`. That factor is
the entire content of what follows.'''))

# ---- rhetoric residue ----
A.append(('RHET-P1', 'comp', '''geometric-algebra formulation directly. Numerically standard Hestenes-form electromagnetism. **Reinterpretation:** TWT inherits the
geometric-algebra formulation directly. The no-monopoles result'''))

A.append(('RHET-P2', 'comp', '''(§B.5.2, corrected 2026-07-28).
in standard EM — a consequence of `F` being a bivector with vector source `J`. What TWT *adds*
is a structural reason for the field/source grading: `F` is grade-2 because EM acts on observers
via the spatial bivectors `γⁱ = e_4 e_i` of §A.5; the wavefront current `J` is grade-1 because
it is the wavefront projection of the soliton's substrate-level *bivector winding*. And
grade-1 + grade-3 are the only grades produced by `∇F` with `F` bivector. "No magnetic
monopoles" in TWT comes with a substrate-level derivation of the field grading itself, not just
the standard Maxwell consequence.'''))

A.append(('RHET-P3', 'comp', '''is a
coherence success — one geometric overlap underlies three independently-measured lengths — not
a value over-determination (`α` cancels in `r_e · a_0 = λ̄_C²`, an algebraic identity).'''))

A.append(('RHET-P4', 'paper', '''(R-039). The slow-motion limit gives Newton's law `V_{12} = −G M_1 M_2 / R`, attractive (R-038).'''))

A.append(('RHET-P5', 'paper', '''leading-order scaling derived at leading order (conditional on the `K_c` ingredient),
**The rest-frame extent.**'''))

A.append(('RHET-P6', 'comp', '''| R-028 | Multipartite MK bound `\\|M_n\\| = 2^{(n+1)/2}`, engine-verified n=2-5 | DERIVED-structural | mermin_klyshko_value + mermin_value | B.4 | R-027 | — | GHZ class. W (non-GHZ) class is a located construction gap (`w_state_located_gap`). |'''))

A.append(('RHET-P7', 'legacy', '''| R-033 | No magnetic monopoles: grade-3 part of `∇F` vanishes because `J` is grade-1 only | DERIVED-A | maxwell_grade_structure | B.5 | R-032 | — | Geometric forbiddance, not mere observation. |'''))

bad = 0
for pid, f, anc in A:
    n = S[f].count(anc)
    flag = 'OK ' if n == 1 else '*** '
    if n != 1:
        bad += 1
    print('%s%-9s %-6s count=%d' % (flag, pid, f, n))
print('\nnon-unique anchors:', bad)
