"""04_fcnc_bounds.py — empirical floor for a gauged horizontal su(2) acting on the
generation triple (TWT family-tree node V4-ASD).

Two parts:
  PART A — the no-GIM lemma, checked numerically: with the three generations in the
           adjoint (triplet) of su(2)_H, a mass matrix commuting with the full gauged
           algebra is forced proportional to the identity; hierarchical masses therefore
           imply O(1) flavor-changing gauge couplings in the mass basis (at best one
           generator can be made diagonal; the other two are then maximally off-diagonal).
  PART B — tree-level bounds Lambda = M_H/g_H from Delta F = 2 mixing and mu -> 3e,
           cross-checked against the Isidori-Nir-Perez benchmark table
           (arXiv:1002.0900, Table: Re C_K -> 9.8e2 TeV, Im C_K -> 1.6e4 TeV) at the
           factor-2 level (vacuum-insertion normalization; good enough for a floor).

Run: python 04_fcnc_bounds.py     (asserts + printed table)
Inputs are PDG/FLAG-standard values, named inline with provenance comments.
"""
import numpy as np

# ---------------- PART A: the no-GIM lemma ----------------
eps = np.zeros((3, 3, 3))
for a, b, c in [(0,1,2),(1,2,0),(2,0,1)]:
    eps[a,b,c], eps[a,c,b] = 1.0, -1.0
T = [-1j*eps[a] for a in range(3)]            # adjoint generators (T^a)_{bc} = -i eps_{abc}

# commutant of {T^a} is 1-dimensional (only multiples of the identity)
rows = []
for a in range(3):
    Ta = T[a]
    # vec([M,Ta]) = (I (x) Ta - Ta^T (x) I) vec(M)
    rows.append(np.kron(np.eye(3), Ta) - np.kron(Ta.T, np.eye(3)))
A = np.vstack(rows)
ns = np.linalg.svd(A)[2].conj().T[:, np.abs(np.linalg.svd(A)[1]) < 1e-10] if False else None
u, s, vh = np.linalg.svd(A)
null_dim = int(np.sum(s < 1e-10))
assert null_dim == 1, f"commutant dim {null_dim}, expected 1 (identity only)"
# hence: gauge-invariant mass term => degenerate generations. Observed hierarchy kills it.

# best-case alignment: diagonalize T^3 (complex basis); then T^{1,2} are pure ladder ops
w, U = np.linalg.eigh(T[2])
T3d = U.conj().T @ T[2] @ U
Tp  = U.conj().T @ (T[0] + 1j*T[1]) @ U
assert np.allclose(np.diag(np.diag(T3d)), T3d, atol=1e-9)      # T^3 diagonal: charges -1,0,+1
offdiag = np.abs(Tp - np.diag(np.diag(Tp)))
assert offdiag.max() > 1.0, "ladder generators must carry O(1) generation-changing entries"
# => at least two of the three horizontal bosons couple with O(1) flavor change. No GIM.

# ---------------- PART B: tree-level bounds ----------------
GEV = 1.0; TEV = 1e3*GEV
hbar_GeV_s = 6.58212e-25

# --- inputs (PDG 2024 / FLAG-standard; stable, slow-moving numbers) ---
mK, fK, BK   = 0.497611, 0.1557, 0.7625      # GeV, GeV, RGI bag (FLAG)
dMK          = 3.484e-15                     # GeV  (PDG: 3.484e-12 MeV)
epsK         = 2.228e-3
mBd, fBd_sqB = 5.27966, 0.225                # GeV; f_Bd*sqrt(B) (FLAG)
dMBd         = 0.5065e12*hbar_GeV_s          # 0.5065/ps -> GeV
mBs, fBs_sqB = 5.36692, 0.274
dMBs         = 17.765e12*hbar_GeV_s
mD, fD, BD   = 1.86484, 0.212, 0.75
dMD          = 6.4e-15                       # GeV (x ~ 0.4% of Gamma_D; HFLAV-average scale)
GF           = 1.166379e-5                   # GeV^-2
BR_mu3e      = 1.0e-12                       # SINDRUM (1988)
BR_mu3e_next = 1.0e-16                       # Mu3e target

def lam_mix(dM_exp, m, f_sqB):
    """Lambda = 1/sqrt(C) from requiring C*(1/3)*f^2*B*m < dM_exp (VIA, LL operator)."""
    O = (1/3)*f_sqB**2*m
    return np.sqrt(O/dM_exp)

def lam_epsK():
    O = (1/3)*(fK*np.sqrt(BK))**2*mK
    Cmax = 2*np.sqrt(2)*epsK*dMK/O           # |eps_NP| = ImM12/(sqrt2 dMK), M12 = C O/2
    return 1/np.sqrt(Cmax)

def lam_mu3e(BR):
    Cmax = 2*GF*np.sqrt(BR)                  # BR = C^2/(4 G_F^2) for (e_L g^mu mu_L)(e_L g_mu e_L)
    return 1/np.sqrt(Cmax)

results = {
    "dMK (Re, 1<->2)":      lam_mix(dMK,  mK,  fK*np.sqrt(BK)),
    "epsK (Im, 1<->2)":     lam_epsK(),
    "dMD (u-sector 1<->2)": lam_mix(dMD,  mD,  fD*np.sqrt(BD)),
    "dMBd (1<->3)":         lam_mix(dMBd, mBd, fBd_sqB),
    "dMBs (2<->3)":         lam_mix(dMBs, mBs, fBs_sqB),
    "mu->3e (SINDRUM)":     lam_mu3e(BR_mu3e),
    "mu->3e (Mu3e proj.)":  lam_mu3e(BR_mu3e_next),
}

# --- cross-check against Isidori-Nir-Perez (arXiv:1002.0900) benchmark rows ---
INP = {"dMK (Re, 1<->2)": 9.8e2*TEV, "epsK (Im, 1<->2)": 1.6e4*TEV}
for k, ref in INP.items():
    ratio = results[k]/ref
    assert 0.5 < ratio < 2.0, f"{k}: {results[k]/TEV:.0f} TeV vs INP {ref/TEV:.0f} TeV"

# --- ordering sanity: epsK is the strongest, all mixing floors above 100 TeV ---
assert results["epsK (Im, 1<->2)"] == max(v for k, v in results.items() if "Mu3e" not in k)
assert all(v > 1e2*TEV for k, v in results.items() if "mu->3e" not in k)

print("04_fcnc_bounds: ALL CHECKS PASSED")
print("no-GIM lemma: commutant of adjoint su(2)_H is {c*1}; hierarchy => O(1) FC couplings\n")
print(f"{'channel':24s}  Lambda = M_H/g_H  (tree exchange, O(1) FC coupling)")
for k, v in results.items():
    print(f"{k:24s}  > {v/TEV:9.0f} TeV")
print("\nfor an O(1) CP phase the operative floor is eps_K:  M_H/g_H  >~ 1e4 TeV")
print("with real couplings the floor is dM_K:              M_H/g_H  >~ 1e3 TeV")
