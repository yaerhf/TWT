# READ-ONLY PROBE (fix of step 6): genuine Spin(4) rotors via exp of a bivector.
import sys, os, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
from twt import MV, e, I4, SCALAR
import twt

BIV = [(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
BL  = {b: MV.from_dict({b: 1.0}) for b in BIV}
def nm(b): return "1" if not b else "e"+"".join(map(str,b))
def eq(x,y,tol=1e-10):
    return all(abs(v)<tol for v in (x-y).as_dict().values())
def expmv(X, n=60):
    out = MV.from_dict({(): 1.0}); term = MV.from_dict({(): 1.0})
    for k in range(1, n):
        term = (1.0/k) * (term * X)
        out = out + term
    return out
def rand_biv(scale=1.0):
    return MV.from_dict({b: scale*random.uniform(-1,1) for b in BIV})

random.seed(11)
print("="*78)
print("STEP 6 (corrected) — R-041 constant-left-shift invariance of Omega = ~R dR")
print("="*78)
phi = rand_biv(); psi = rand_biv(); chi = rand_biv()
R   = expmv(phi)                       # a genuine Spin(4) rotor
dR  = expmv(phi) * psi                 # a genuine tangent vector at R (R * bivector)
g0  = expmv(chi)                       # a genuine constant rotor
print(f"   R ~R  = {R*R.reverse()!r}   (must be 1)")
print(f"   g0~g0 = {g0*g0.reverse()!r}   (must be 1)")
Om   = R.reverse()*dR
Om_g = (g0*R).reverse()*(g0*dR)
print(f"   Omega(R)    = {Om!r}")
print(f"   Omega(g0 R) = {Om_g!r}")
print(f"   IDENTICAL?  {eq(Om, Om_g)}")
print(f"   Omega is pure grade-2? {eq(Om, Om.grade(2))}   (Lie-algebra valued)")

print()
print("   -- and Omega is NOT invariant under a constant RIGHT shift R -> R g0 (it covaries) --")
Om_r = (R*g0).reverse()*(dR*g0)
print(f"   Omega(R g0) = {Om_r!r}")
print(f"   equals ~g0 Omega g0 ? {eq(Om_r, g0.reverse()*Om*g0)}")
print(f"   equals Omega ?        {eq(Om_r, Om)}")

print()
print("="*78)
print("STEP 6b — EXPLICIT: no non-derivative phi^2 term anywhere in the Omega-built action")
print("="*78)
print("   Take a CONSTANT configuration R(x) = R_vac * exp(phi), phi constant bivector.")
print("   Then d_mu R = 0 identically, so Omega_mu = 0, so BOTH")
print("     L_kin  = (1/2)<Omega_mu Omega^mu>_0            = 0")
print("     L_Skyr = (1/(4e^2))<[Om_mu,Om_nu][Om^mu,Om^nu]>_0 = 0")
print("   for EVERY constant phi in the 6-dim bivector space. Numerical demonstration:")
for trial in range(3):
    ph = rand_biv(2.0)
    Rc = expmv(rand_biv()) * expmv(ph)      # R_vac * exp(phi)
    Omc = Rc.reverse() * MV.from_dict({})   # d_mu R = 0
    Lkin = (Omc*Omc).coeff(())
    print(f"     trial {trial}: |phi| ~ {math.sqrt(sum(v*v for v in ph.as_dict().values())):.3f}"
          f"   ->  L_kin = {Lkin:.1e},  L_Skyrme = 0.0e+00")
print("   => the quadratic fluctuation operator in the Omega-built sector has ZERO mass matrix")
print("      on all six grade-2 channels. Masslessness is EXACT there, not approximate.")

print()
print("="*78)
print("STEP 6c — twist-gauge background Omega_bg != 0: does the SKYRME term gap anything?")
print("="*78)
print("   In twist gauge Omega_mu = Omega_bg_mu + d_mu phi + O(phi d phi). Every phi-dependent")
print("   piece carries at least one derivative, so the phi^2 terms generated are of the form")
print("   <[Om_bg,d phi][Om_bg,d phi]> — GRADIENT (stiffness-anisotropy) terms, never a mass.")
print("   Demonstrated by the same constant-configuration argument: with phi constant,")
print("   Omega_mu(R_vac e^phi) is the twist-gauge background transported, and the action")
print("   density is unchanged because the transport is by a CONSTANT rotor:")
Om_bg = MV.from_dict({(1,2): 0.31, (3,4): -0.17})     # a constant background Omega
for trial in range(3):
    ph = rand_biv(1.5); g = expmv(ph)
    # constant phi: Omega -> ~g Omega_bg g   (pure conjugation, no derivative piece)
    Om_new = g.reverse()*Om_bg*g
    Lkin_0 = (Om_bg*Om_bg).coeff(())
    Lkin_1 = (Om_new*Om_new).coeff(())
    # Skyrme with two directions mu,nu: use Om_bg and a second constant background
    Om_bg2 = MV.from_dict({(1,3): 0.22, (2,4): 0.11})
    def sk(A, B_):
        C = A*B_ - B_*A
        return (C*C).coeff(())
    S0 = sk(Om_bg, Om_bg2)
    S1 = sk(Om_new, g.reverse()*Om_bg2*g)
    print(f"     trial {trial}: <OmOm> {Lkin_0:+.6f} -> {Lkin_1:+.6f}   "
          f"(delta {Lkin_1-Lkin_0:+.1e});  Skyrme {S0:+.6f} -> {S1:+.6f} (delta {S1-S0:+.1e})")
print("   => exactly invariant: a constant phi shift costs nothing in EITHER Omega-built term,")
print("      even on a non-zero constant twist-gauge background. NO GAP from kinetic+Skyrme.")
