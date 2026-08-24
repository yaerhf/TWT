# -*- coding: utf-8 -*-
import io, os
base = os.path.join(os.path.dirname(__file__), '..', '..', 'corpus')
paper = io.open(os.path.join(base, 'TWT_foundational_paper.md'), encoding='utf-8').read()

F = """What TWT supplies is that nothing fills it. The framework's only current is `J`, the wavefront
projection of L-orbit bivector winding to grade 1 (§B.5.1), and a grade-2 → grade-1 projection
cannot produce grade-3 content."""
print("anchor F (B.5.2 source) count =", paper.count(F))
# sanity: how many places still say "L-orbit" in the EM section after patches C,D,F?
seg = paper[paper.index("## §B.5 — Electromagnetism"):paper.index("## §B.5b")]
import re
print("occurrences of 'L-orbit' inside §B.5:", seg.count("L-orbit"))
for m in re.finditer("L-orbit", seg):
    print("   ...", seg[max(0,m.start()-90):m.start()+60].replace("\n"," "))
