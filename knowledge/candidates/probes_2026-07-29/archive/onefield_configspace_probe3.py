# ONE-FIELD probe, part 3: the PER-DEFECT COMPLEX STRUCTURE obstruction,
# the rotational band, and the individuation scale in fm.
import sys, math
sys.path.insert(0, r"C:\Users\hfyae\Claude\Projects\Deepseek\knowledge\corpus")
import numpy as np, sympy as sp
import twt
from twt import MV, e, SCALAR, I4, exp_unit_bivector

print("="*78)
print("H. THE PER-DEFECT COMPLEX-STRUCTURE OBSTRUCTION")
print("   B.3.1/R-127: EACH defect selects its OWN winding blade B_a as the QM i.")
print("   Two defects with B_a != B_b give TWO complex structures on the joint space.")
print("="*78)

Ba, Bb = e(1,2), e(1,3)
print(f"   B_a = e12, B_b = e13 ;  B_a^2 = {(Ba*Ba)} ,  B_b^2 = {(Bb*Bb)}")
print(f"   do they commute inside Cl+(4,0)?  [B_a,B_b] = {Ba*Bb - Bb*Ba}   (NO)")
print("   -> so B_a and B_b cannot both act as 'the' i on ONE Cl+(4,0) module.")

print("\n   H1. The joint space: C_a (x)_R C_b  as a real algebra.")
# basis 1(x)1, ia(x)1, 1(x)ib, ia(x)ib ; Ja = left mult by ia(x)1, Jb = 1(x)ib
def kron(A,B): return np.kron(A,B)
i2 = np.array([[0.,-1.],[1.,0.]]); id2 = np.eye(2)
Ja = kron(i2, id2); Jb = kron(id2, i2)
print(f"      Ja^2 = -1 : {np.allclose(Ja@Ja, -np.eye(4))}")
print(f"      Jb^2 = -1 : {np.allclose(Jb@Jb, -np.eye(4))}")
print(f"      [Ja,Jb]=0 : {np.allclose(Ja@Jb, Jb@Ja)}")
K = Ja@Jb
print(f"      K = Ja Jb ;  K^2 = +1 : {np.allclose(K@K, np.eye(4))}   (a REAL structure, not a complex one)")
Pp, Pm = (np.eye(4)-K)/2, (np.eye(4)+K)/2
print(f"      P+ = (1-K)/2, P- = (1+K)/2 :  idempotent {np.allclose(Pp@Pp,Pp) and np.allclose(Pm@Pm,Pm)},"
      f"  orthogonal {np.allclose(Pp@Pm, 0)},  sum=1 {np.allclose(Pp+Pm, np.eye(4))}")
print(f"      ranks: rank(P+) = {np.linalg.matrix_rank(Pp)}, rank(P-) = {np.linalg.matrix_rank(Pm)}")
print(f"      on P+ :  Ja = Jb ? {np.allclose(Ja@Pp, Jb@Pp)}")
print(f"      on P- :  Ja = -Jb ? {np.allclose(Ja@Pm, -Jb@Pm)}")
# zero divisors
z1 = np.eye(4) - K   # (1(x)1 - ia(x)ib) up to factor
z2 = np.eye(4) + K
print(f"      zero divisors: (1-K)(1+K) = 0 ? {np.allclose(z1@z2, 0)}   => C (x)_R C = C (+) C, NOT a field")

print("\n   H2. Dimension bookkeeping for two qubits.")
print("      QM      : C^2 (x)_C C^2 = C^4 = 8 real dimensions")
print("      TWT raw : R^4 (x)_R R^4 = 16 real dimensions  (TWICE too many)")
print("      after projecting with P+ (or P-): 16/2 = 8 real  => matches QM exactly")
print("      => the tensor product REQUIRES an inserted idempotent (the Doran-Lasenby")
print("         'correlator'); there are exactly TWO (P+, P-), related by conjugating")
print("         one factor. That idempotent is EXTRA STRUCTURE, not derived here.")

print("\n   H3. Is there a global complex unit that would fix it?")
# E = I4 e5 in Cl(4,1). Engine has Cl(4,0); check centrality of I4 in Cl+(4,0) as the proxy
print(f"      I4 commutes with every even blade?", end=" ")
EVEN = [SCALAR, e(1,2), e(1,3), e(1,4), e(2,3), e(2,4), e(3,4), I4]
print(all((I4*v - v*I4).terms == () for v in EVEN))
print(f"      I4^2 = {I4*I4}   (+1: a real duality, NOT a complex unit -- canon Sec.1)")
print("      The genuine central unit is E = I4*e5 in Cl(4,1) with E^2 = -1 (canon Sec.1).")
print("      => a joint state space that IS a complex Hilbert space must be a module over")
print("         the CENTRAL E, not over the per-defect winding blade B_a.  That is a")
print("         STRUCTURAL REQUIREMENT the construction generates, and it is in tension")
print("         with R-127's per-defect B_a mass-phase lock. Named, not resolved.")

print()
print("="*78)
print("I. The rotational-moduli internal factor: L^2(SU(2)), not C^2")
print("="*78)
try:
    r = twt.skyrmion_rotational_band_nucleon_delta()
    for k,v in r.items(): print(f"   {k} = {str(v)[:260]}")
except Exception as ex:
    print("   RAISED", ex)

print()
print("="*78)
print("J. The individuation scale in physical units")
print("="*78)
Ls = twt.skyrme_length_fm()
ell = Ls['ell_S (fm)']
for nm, x in [("r50", 1.7526), ("r90", 3.0872), ("r99", 4.8355), ("peak of 4pi x^2 b", 1.5085)]:
    print(f"   {nm:20s} x = {x:7.4f} Skyrme units -> {x*ell:6.3f} fm")
print(f"   two-defect core-overlap separation d ~ 2*r50 = {2*1.7526*ell:.3f} fm ;"
      f"  2*r90 = {2*3.0872*ell:.3f} fm")
print("   (nucleon: the two-body chart is expected to fail at ~1-1.7 fm -- exactly where")
print("    the nuclear two-body description is known empirically to break down.)")

print()
print("="*78)
print("K. Where the product ansatz (= the tensor-product chart) is already known to fail")
print("="*78)
r135 = twt.multi_skyrmion_b2_classical_binding()
print(f"   R-135 : B=2 true(rational-map) = {r135['b2']['mass_coeff']:.4f} vs product-chart"
      f" asymptote 2*{r135['b1_regression']['mass_coeff']:.4f} = {2*r135['b1_regression']['mass_coeff']:.4f}")
print(f"           chart deficit = {r135['inequality']['margin']*100:.3f}%  (the chart MISSES the true configuration)")
r139 = twt.two_defect_asymptotic_tensor_force()
print(f"   R-139 : grid vs leading dipole law at R=8 and R=10:")
for R, dat in r139['grid_certificate'].items():
    for ch, vv in dat.items():
        if vv['pred'] != 0:
            print(f"           R={R} {ch:5s}: V={vv['V']:+.4f} vs asymptotic pred {vv['pred']:+.4f}"
                  f"  ({100*(vv['V']-vv['pred'])/abs(vv['pred']):+.1f}%)")
