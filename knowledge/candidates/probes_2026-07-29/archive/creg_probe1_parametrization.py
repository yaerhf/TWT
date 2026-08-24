"""PROBE 1 — is the ~21.6 'c_reg disagreement' a PHYSICS disagreement or a Lambda-DEFINITION artifact?

Both banked primitives state 1/(16 pi G). Write each in the paper's parametrization
    1/(16 pi G) = c_reg * N_eff * Lambda^2 / (16 pi^2)
and see what Lambda each one means.

READ-ONLY probe; nothing is edited.
"""
import math, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import twt

N = 6

print("=" * 78)
print("PROBE 1 — the parametrization identity")
print("=" * 78)

# ---- branch A: sakharov_induced_gravity ---------------------------------
sg = twt.sakharov_induced_gravity()
print("sakharov_induced_gravity: formula =", sg["formula"])
# G^-1 = N Lambda^2/(12 pi)  =>  1/(16 pi G) = N Lambda^2/(192 pi^2)
cregA = (16 * math.pi**2) / (192 * math.pi**2)
print("  => c_reg(A) = 16pi^2/192pi^2 =", cregA, "= 1/12 =", 1/12)
print("  Lambda meant by A  : the PROPER-TIME CUTOFF Lambda (s > 1/Lambda^2)")

# ---- branch B: induced_G_from_linear_face_band (R-163) -----------------
fb = twt.induced_G_from_linear_face_band()
c_lat = fb["c_lat"]
print("\ninduced_G_from_linear_face_band: assembly =", fb["assembly"])
print("  c_lat =", c_lat)
# 1/(16 pi G) = N c_lat/(192 pi^2 a^2).  With Lambda := 1/a:
cregB_at_inv_a = (16 * math.pi**2) * c_lat / (192 * math.pi**2)
print("  => with Lambda := 1/a          : c_reg(B) = c_lat/12 =", round(cregB_at_inv_a, 4))
# With Lambda := Lambda_eff = sqrt(c_lat)/a:
cregB_at_Leff = (16 * math.pi**2) * c_lat / (192 * math.pi**2 * c_lat)
print("  => with Lambda := Lambda_eff   : c_reg(B) =", cregB_at_Leff, "= 1/12 =", 1/12)

print("\nRATIO of the two BANKED c_reg values:")
print("  c_reg(B, Lambda=1/a) / c_reg(A) =", round(cregB_at_inv_a / cregA, 4))
print("  c_lat                           =", round(c_lat, 4))
print("  difference                      =", abs(cregB_at_inv_a / cregA - c_lat))

# ---- what each branch implies for Lambda/M_Pl (non-reduced) ------------
# paper parametrization: M_Pl^2/(16 pi) = c_reg N Lambda^2/(16 pi^2)
#   => Lambda/M_Pl = sqrt(pi/(c_reg N))
def lam_over_MPl(c_reg, Neff=N):
    return math.sqrt(math.pi / (c_reg * Neff))

print("\nLambda/M_Pl (non-reduced) implied by each c_reg at N_eff = 6:")
for name, c in (("A: c_reg = 1/12 (Lambda = proper-time cutoff)", 1/12),
                ("   paper placeholder c_reg ~ 1", 1.0),
                ("B: c_reg = c_lat/12 = 1.82 (Lambda = 1/a)", c_lat/12)):
    print("   %-46s -> Lambda/M_Pl = %.4f" % (name, lam_over_MPl(c)))

# ---- the key structural check: Lambda_eff is c_lat-INDEPENDENT ---------
print("\nIs Lambda_eff c_lat-dependent?  a/ell_Pl = sqrt(N c_lat/(12 pi)),  Lambda_eff = sqrt(c_lat)/a")
for cl in (5.0, 10.0, c_lat, 40.0, 100.0):
    a = math.sqrt(N * cl / (12 * math.pi))          # in ell_Pl(full)
    Leff = math.sqrt(cl) / a                        # in M_Pl(full)
    print("   c_lat = %7.3f -> a = %.4f ell_Pl,  1/a = %.4f M_Pl,  Lambda_eff = %.6f M_Pl"
          % (cl, a, 1/a, Leff))
print("   sqrt(2*pi) =", math.sqrt(2*math.pi))
print("\n=> Lambda_eff is EXACTLY c_lat-independent; only a and 1/a move with c_lat.")
