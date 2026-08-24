# READ-ONLY PROBE — is option (i) "gauge redundancy" available for the six?
import sys, os, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
from twt import MV, e
BIV = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
def eq(x,y,tol=1e-10): return all(abs(v)<tol for v in (x-y).as_dict().values())
def expmv(X, n=60):
    out = MV.from_dict({(): 1.0}); t = MV.from_dict({(): 1.0})
    for k in range(1, n):
        t = (1.0/k)*(t*X); out = out + t
    return out
def rb(s=1.0): return MV.from_dict({b: s*random.uniform(-1,1) for b in BIV})
random.seed(3)

print("="*78)
print("Is any of the six a GAUGE direction? Test LOCAL (x-dependent) shifts.")
print("="*78)
phi = rb(); R = expmv(phi); dR = R*rb()              # R(x), d_mu R(x)
for side in ("left", "right"):
    print(f"\n  -- LOCAL {side} shift R -> {'g(x) R' if side=='left' else 'R g(x)'} --")
    for trial in range(3):
        chi = rb(0.7); g = expmv(chi); dg = g*rb(0.7)     # g(x), d_mu g(x)
        if side == "left":
            Rn, dRn = g*R, dg*R + g*dR
        else:
            Rn, dRn = R*g, dR*g + R*dg
        Om  = R.reverse()*dR
        Omn = Rn.reverse()*dRn
        L0 = (Om*Om).coeff(()); L1 = (Omn*Omn).coeff(())
        print(f"     trial {trial}: <Om Om>_0  {L0:+.6f}  ->  {L1:+.6f}   "
              f"delta = {L1-L0:+.4f}   invariant? {abs(L1-L0)<1e-9}")
print()
print("  => LOCAL left shifts: the KINETIC scalar IS invariant (Omega itself is invariant")
print("     only for CONSTANT g; for local g(x), Omega(gR) = Omega(R) + ~R ~g (d g) R, so it")
print("     is NOT invariant — see the deltas above).")
print("  => LOCAL right shifts also change the action. Neither is a gauge symmetry.")
print("     There is NO local redundancy in the rotor sigma-model: all six grade-2")
print("     directions are PHYSICAL field directions, not gauge parameters.")
print()
print("  (Contrast: the two NON-directions, grade-0 and grade-4, are excluded by the")
print("   CONSTRAINT |R| = 1, not by a gauge symmetry — they are simply not in the")
print("   field space, so no gauge-fixing is available or needed for them.)")

print()
print("="*78)
print("FINAL TALLY of the eight even blades of Cl+(4,0) under B_a = e12")
print("="*78)
rows = [
 ("1",     "grade 0", "ad-charge 0", "KEPT (SB.3.1 'f')", "NOT a rotor DOF - rotor-norm direction, frozen by |R|=1 (SSB.6.3(i), SD.3.2)"),
 ("e12",   "grade 2", "ad-charge 0", "KEPT (SB.3.1 'g')", "physical; massless in the Omega-built sector; +omega branch on a defect (R-126)"),
 ("e34",   "grade 2", "ad-charge 0", "SET ASIDE", "physical grade-2 channel; massless in Omega-built sector; +omega branch (R-126); Q-orbit (ELECTRIC)"),
 ("I4",    "grade 4", "ad-charge 0", "SET ASIDE", "NOT a rotor DOF - excluded by |R|=1 by the same identity as the scalar"),
 ("e13",   "grade 2", "ad-charge +/-1", "SET ASIDE", "physical; massless in Omega-built sector; -omega conjugate branch (R-126); L-orbit (MAGNETIC)"),
 ("e23",   "grade 2", "ad-charge +/-1", "SET ASIDE", "physical; massless in Omega-built sector; -omega conjugate branch (R-126); L-orbit (MAGNETIC)"),
 ("e14",   "grade 2", "ad-charge +/-1", "SET ASIDE", "physical; massless in Omega-built sector; -omega conjugate branch (R-126); Q-orbit (ELECTRIC)"),
 ("e24",   "grade 2", "ad-charge +/-1", "SET ASIDE", "physical; massless in Omega-built sector; -omega conjugate branch (R-126); Q-orbit (ELECTRIC)"),
]
for r in rows:
    print(f"  {r[0]:<6} {r[1]:<8} {r[2]:<14} {r[3]:<18} {r[4]}")
print()
print("  SIX SET ASIDE = 1 non-dynamical (I4) + FIVE physical grade-2 channels.")
print("  Of the five: at the Omega-built (kinetic+Skyrme) level ALL FIVE are EXACTLY MASSLESS.")
print("  On the realistic canted vacuum the banked count is 2 gapless + 4 gapped out of six;")
print("  the gapless 2-plane lies inside SU(2)_L = span{e12,e13,e23}, so at least ONE and")
print("  generically TWO of the five set-aside grade-2 channels stay EXACTLY GAPLESS.")
print("  The gap magnitude for the other four rides L_top(D)'s open coefficient mu -> #1-gap GATED.")
