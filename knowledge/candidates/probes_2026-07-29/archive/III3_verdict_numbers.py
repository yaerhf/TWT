"""III-3 final arithmetic: what the paper's C.1.6 numbers become if the SKYRME hedgehog
eigenvalue is replaced by the FADDEEV-SKYRME (hopfion) one.

Inputs used (each sourced):
  * Skyrme hedgehog B=1, matched c2=c4=1 units: Etil_S = 145.847 (computed here-adjacent,
    III3_skyrme_hedgehog_matched.py) = 4 x 36.462, i.e. reproduces the banked 36.47.
  * Faddeev-Skyrme H=1, SAME matched units: Etil_F = 1.236 x 32 pi^2 sqrt(2)
    [Foster, arXiv:1012.2595 'Massive Hopfions', massless mu=0 value, units 32 pi^2 sqrt(2)].
    Independently bracketed here: rigorous Vakulenko-Kapitanski lower bound
    32 pi^2 (3/16)^(3/8) = 168.59, and this session's variational UPPER bound 635.3.
  * Paper C.1.6 inputs: f_pi = 129 MeV, D/J = 0.79, m_e = 0.51099895 MeV, nu = 9/2.
"""
import math

E_S = 145.847                     # Skyrme hedgehog B=1, c2=c4=1  (= 4 x 36.462)
UNIT = 32 * math.pi ** 2 * math.sqrt(2)
E_F = 1.236 * UNIT                # Faddeev-Skyrme H=1, c2=c4=1
VK = 32 * math.pi ** 2 * (3 / 16) ** 0.375
UPPER = 635.27                    # this session's variational upper bound

print("MATCHED NORMALISATION  E = c2 INT |d n|^2 + c4 INT |d n ^ d n|^2, c2 = c4 = 1")
print(f"  Skyrme hedgehog  B=1 : Etil_S = {E_S:8.3f}   (= 4 x {E_S/4:.3f}; banked coeff 36.47)")
print(f"  Faddeev-Skyrme   H=1 : Etil_F = {E_F:8.3f}   (= 1.236 x {UNIT:.2f})")
print(f"  rigorous VK lower bound        = {VK:8.3f} x |H|^(3/4)")
print(f"  this session's upper bound     = {UPPER:8.3f}")
print(f"  --> Etil_S = {E_S:.2f}  is BELOW the rigorous VK floor {VK:.2f}: "
      f"{'YES' if E_S < VK else 'NO'}")
print(f"  ratio Etil_F / Etil_S          = {E_F/E_S:.3f}")

# the 'coefficient' in ANW form  M = coeff * f/e   (since sqrt(c2 c4) = f/(4e))
c_S, c_F = E_S / 4, E_F / 4
print(f"\nANW-form coefficient (M = coeff * f/e):")
print(f"  Skyrme  hedgehog B=1 : {c_S:7.3f}   <- the paper's 36.47")
print(f"  Faddeev hopfion  H=1 : {c_F:7.3f}   <- the correct object's analogue")
print(f"  ratio                : {c_F/c_S:.3f}")

# the paper writes m_e = f_L * e_L with e_L = sqrt(36.47) -- i.e. it SETS the L-sector
# Skyrme coupling to sqrt(coeff).  Propagate that same move with the hopfion coefficient.
eL_paper, eL_hopf = math.sqrt(36.47), math.sqrt(c_F)
print(f"\ne_L = sqrt(coeff):  paper {eL_paper:.4f}   hopfion analogue {eL_hopf:.4f}"
      f"   (factor {eL_hopf/eL_paper:.3f})")

f_pi, DoJ, m_e, nu = 129.0, 0.79, 0.51099895, 4.5
delta = 1 - DoJ
f_L_pred = f_pi * delta ** nu
print(f"\npredicted f_L = f_pi (1-D/J)^(9/2) = {f_L_pred:.5f} MeV   (paper: 0.115)")
for label, eL in (("paper  e_L=sqrt(36.47)", eL_paper), ("hopfion e_L=sqrt(138.0)", eL_hopf)):
    tgt = m_e / eL
    nu_emp = math.log(tgt / f_pi) / math.log(delta)
    print(f"  {label}: m_e/e_L = {tgt:.5f} MeV | f_L_pred/target = {f_L_pred/tgt:.3f} "
          f"| nu_emp = {nu_emp:.4f} | (nu_emp-4.5)/4.5 = {(nu_emp-nu)/nu*100:+.2f}%")

print("\nCHARGE SCALING (why a one-charge coincidence would not license the identification):")
print("  Skyrme  : M(B) ~ linear in B (B=1 hedgehog; B>1 near-additive)")
print("  Faddeev : E(H) ~ H^(3/4) -- the exponent is RIGOROUS (Vakulenko-Kapitanski)")
for H in (1, 2, 3, 4):
    print(f"    H={H}: linear-in-B would give {c_S*H:7.2f} f/e ;  "
          f"H^(3/4) hopfion gives {c_F*H**0.75:7.2f} f/e")
