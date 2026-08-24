# READ-ONLY PROBE — the DEFECT background side: does R-126's (2,4) commutant split
# coincide with the ad(B) charge split of the six set-aside blades?
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
from twt import MV, e, I4, SCALAR
import twt

BIV = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
BL  = {b: MV.from_dict({b: 1.0}) for b in BIV}
def nm(b): return "e"+"".join(map(str,b))
def eq(x,y,tol=1e-12): return all(abs(v)<tol for v in (x-y).as_dict().values())
Z = MV.from_dict({})
B = e(1,2)

print("="*78)
print("A — commutant / anticommutant of the defect rotor axis u = B = e12 in the bivectors")
print("="*78)
commuting, anticommuting, neither = [], [], []
for b in BIV:
    X = BL[b]
    c = B*X - X*B
    a = B*X + X*B
    if eq(c, Z):   commuting.append(b)
    elif eq(a, Z): anticommuting.append(b)
    else:          neither.append(b)
    print(f"   {nm(b):>5}: [B,X] = {c!r:>12}   {{B,X}} = {a!r:>14}")
print(f"\n   COMMUTING 2-plane   : {[nm(b) for b in commuting]}   (dim {len(commuting)})")
print(f"   ANTICOMMUTING 4-plane: {[nm(b) for b in anticommuting]}   (dim {len(anticommuting)})")
print(f"   neither              : {[nm(b) for b in neither]}")
assert len(commuting)==2 and len(anticommuting)==4 and not neither
print("   => EXACTLY R-126's (2,4) commutant dims, and EXACTLY the ad(B) charge split:")
print("      commuting 2-plane == the two ad(B)-NEUTRAL bivectors {e12, e34}")
print("      anticommuting 4-plane == the four ad(B)-CHARGED blades {e13,e14,e23,e24}")

print()
print("="*78)
print("B — the banked frequency labels R-126 already assigns to those two blocks")
print("="*78)
r126 = twt.defect_zero_mode_multiplet_labels()
def show(d, ind="   "):
    for k, v in d.items():
        if isinstance(v, dict):
            print(f"{ind}{k}:"); show(v, ind+"  ")
        else:
            s = str(v)
            print(f"{ind}{k}: {s[:300]}{'...' if len(s)>300 else ''}")
show(r126)

print()
print("="*78)
print("C — the conjugation identity R-126 uses for the anticommuting block, re-checked")
print("="*78)
import math
w, t5 = 1.7, 0.83
Q  = MV.from_dict({(): math.cos(w*t5/2), (1,2): math.sin(w*t5/2)})     # exp(B w t5/2)
Qm = MV.from_dict({(): math.cos(w*t5/2), (1,2): -math.sin(w*t5/2)})    # Q(-t5)
for b in anticommuting:
    X = BL[b]
    lhs = X*Q; rhs = Qm*X
    print(f"   {nm(b):>5} * Q(t5)  == Q(-t5) * {nm(b):<5} ?  {eq(lhs, rhs)}")
for b in commuting:
    X = BL[b]
    print(f"   {nm(b):>5} * Q(t5)  == Q(+t5) * {nm(b):<5} ?  {eq(X*Q, Q*X)}")
print("   => the 4 CHARGED set-aside blades are exactly the ones that read the CONJUGATE")
print("      branch -omega; the neutral e34 rides the same +omega branch as the kept B.")

print()
print("="*78)
print("D — R-125's phase collective mode, and where it sits among the eight")
print("="*78)
r125 = twt.defect_phase_collective_mode_at_k4()
show({k: v for k, v in r125.items() if k in
      ("tier","mode","k4","label","zero_mode","frequency","status","claim","result")} or r125)
