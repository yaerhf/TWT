# -*- coding: utf-8 -*-
"""PROBE 2: the singlet pairing eps(u,v) = <j u, v> -- LEFT vs RIGHT multiplication by j,
and whether the C^2 = Z(e4) repair actually carries the SU(2)-invariant symplectic form.
Read-only."""
import math, cmath, random
import numpy as np
import twt
from twt import MV, e

ONE = MV.from_dict({(): 1.0})
B = e(1, 2)
Zb = [ONE, e(1,2), e(1,3), e(2,3)]

def to_C2(x):
    return np.array([complex(x.coeff(()), x.coeff((1,2))),
                     complex(x.coeff((1,3)), x.coeff((2,3)))])
def from_C2(z):
    return (z[0].real*ONE + z[0].imag*e(1,2) + z[1].real*e(1,3) + z[1].imag*e(2,3))
def herm(x, y):
    return complex(np.vdot(to_C2(x), to_C2(y)))

rnd = random.Random(11)
def rvec():
    return from_C2(np.array([complex(rnd.gauss(0,1),rnd.gauss(0,1)),
                             complex(rnd.gauss(0,1),rnd.gauss(0,1))]))

print("="*78)
print("IS RIGHT-MULT BY j ANTILINEAR / LEFT-MULT BY j C-LINEAR?  (the C-structure is")
print("RIGHT multiplication by B_a = e12; ' i ' below means that right multiplication)")
print("="*78)
for nm, jb in [("e13", e(1,3)), ("e23", e(2,3)), ("e12", e(1,2))]:
    aL = aR = lL = lR = 0.0
    for _ in range(300):
        u = rvec()
        # right-mult by j : linear?  antilinear?
        lR = max(lR, np.max(np.abs(to_C2((u*B)*jb) - 1j*to_C2(u*jb))))       # linear test
        aR = max(aR, np.max(np.abs(to_C2((u*B)*jb) + 1j*to_C2(u*jb))))       # antilinear test
        lL = max(lL, np.max(np.abs(to_C2(jb*(u*B)) - 1j*to_C2(jb*u))))
        aL = max(aL, np.max(np.abs(to_C2(jb*(u*B)) + 1j*to_C2(jb*u))))
    print("  j=%-4s  RIGHT-mult:  C-linear dev=%.1e   antilinear dev=%.1e" % (nm, lR, aR))
    print("         LEFT -mult:  C-linear dev=%.1e   antilinear dev=%.1e" % (lL, aL))

print()
print("="*78)
print("THE PAIRING eps(u,v) = <j u, v>  --- both readings tested")
print("  bilinear?  antisymmetric?  SU(2)-invariant under the LEFT L-orbit rotor action?")
print("="*78)

def report(label, epsf):
    anti = bil1 = bil2 = inv = 0.0
    for _ in range(300):
        u, v, w = rvec(), rvec(), rvec()
        lam = complex(rnd.gauss(0,1), rnd.gauss(0,1))
        lamMV = lam.real*ONE + lam.imag*e(1,2)
        anti = max(anti, abs(epsf(u,v) + epsf(v,u)))
        bil1 = max(bil1, abs(epsf(u*lamMV, v) - lam*epsf(u,v)))
        bil2 = max(bil2, abs(epsf(u, v*lamMV) - lam*epsf(u,v)))
        cs = [rnd.gauss(0,1) for _ in range(3)]
        nn = math.sqrt(sum(c*c for c in cs)); cs = [c/nn for c in cs]
        ax = cs[0]*e(1,2)+cs[1]*e(1,3)+cs[2]*e(2,3)
        R = twt.exp_unit_bivector(ax, rnd.uniform(-3,3))
        inv = max(inv, abs(epsf(R*u, R*v) - epsf(u,v)))
    print("  %-34s antisym dev=%.1e  C-lin(1)=%.1e  C-lin(2)=%.1e  SU(2)-inv dev=%.1e"
          % (label, anti, bil1, bil2, inv))
    return anti, bil1, bil2, inv

for nm, jb in [("e13", e(1,3)), ("e23", e(2,3)), ("e12 (the PHASE blade)", e(1,2))]:
    report("RIGHT: eps(u,v)=<u*%s, v>" % nm, (lambda J: (lambda u,v: herm(u*J, v)))(jb))
for nm, jb in [("e13", e(1,3)), ("e23", e(2,3))]:
    report("LEFT : eps(u,v)=<%s*u, v>" % nm, (lambda J: (lambda u,v: herm(J*u, v)))(jb))

print()
print("="*78)
print("THE WORKING FORM ON THE C-BASIS {|0> = 1, |1> = e13}")
print("="*78)
k0, k1 = from_C2(np.array([1+0j, 0j])), from_C2(np.array([0j, 1+0j]))
for nm, jb in [("e13", e(1,3)), ("e23", e(2,3))]:
    E = lambda u, v: herm(u*jb, v)
    print("  j=%-4s : eps(0,0)=%-10s eps(0,1)=%-10s eps(1,0)=%-10s eps(1,1)=%s"
          % (nm, E(k0,k0), E(k0,k1), E(k1,k0), E(k1,k1)))
print("  => the standard SU(2)-invariant symplectic form on C^2 (up to an overall phase).")
print("     Its tensor  eps^{ab}  IS the two-wing singlet  (|01> - |10>)/sqrt2.")

print()
print("="*78)
print("AND WHAT HAPPENS IF THE STATE SPACE IS THE PHASE SECTOR C^1 INSTEAD")
print("="*78)
print("  On C^1 an antisymmetric bilinear form is IDENTICALLY ZERO:")
print("     Lambda^2(C^1) = 0  ->  dim = %d" % 0)
print("  Explicit: restrict eps to span{1,B} (z2 == 0) and evaluate on 200 random pairs:")
mx = 0.0
for _ in range(200):
    u = from_C2(np.array([complex(rnd.gauss(0,1),rnd.gauss(0,1)), 0j]))
    v = from_C2(np.array([complex(rnd.gauss(0,1),rnd.gauss(0,1)), 0j]))
    mx = max(mx, abs(herm(u*e(1,3), v)))
print("     max |eps(u,v)| over the phase sector = %.3e   (identically zero)" % mx)
print("""
  THIS IS THE CONTRADICTION IN ITS SHARPEST FORM: the singlet IS the antisymmetric
  pairing, Lambda^2 of the one-wing space.  Lambda^2(C^1) = 0 and Lambda^2(C^2) = C.
  A one-wing space of complex dimension 1 has NO singlet to form.  The pairing exists
  exactly and only on the FULL commutant Z(e4), and it is carried by the two units
  {e13, e23} that the phase-sector cut throws away.""")

print()
print("="*78)
print("DIMENSION TABLE (for the report)")
print("="*78)
rows = [
 ("phase sector  span{1,B_a}", 2, 1, "no", "Lambda^2 = 0; all rotor-rotated states are ONE ray"),
 ("commutant Z_{Cl+}(e4) = span{1,e12,e13,e23} = H", 4, 2, "YES",
  "SU(2) = left L-orbit rotors; C = right mult by B_a; eps lives on {e13,e23}"),
 ("full even algebra Cl+(4,0)", 8, 4, "yes but too big",
  "(W) is violated by e14,e24,e34,I4 -- not in the wavefront frame"),
 ("charge-0 sector {1,e12,e34,I4}", 4, 2, "formally",
  "but e34,I4 fail (W); this is the (S)-commutant, not the (W)-commutant"),
 ("FR-odd collective band j=1/2 of L^2(SU(2))", 8, 4, "yes",
  "= C^2_spin (x) C^2_iso; but this is ALREADY a quantized space (circular for SSB.3)"),
]
print("%-50s %6s %6s %-16s" % ("space", "dim_R", "dim_C", "hosts a qubit?"))
for r in rows:
    print("%-50s %6d %6d %-16s" % (r[0], r[1], r[2], r[3]))
    print("%-50s %s" % ("", r[4]))
print("\nDONE.")
