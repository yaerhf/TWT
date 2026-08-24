"""04_fcnc_bounds_v2.py — post-adjudication revision (2026-08-24, external review r4).

Changes from v1, per the merge record's two corrections:

  1. CRITERION SEMANTICS. v1's assert was labeled a "reproduction" of the
     Isidori-Nir-Perez table (arXiv:1002.0900). The primary read found the agreement is
     CRITERION-ROBUST rather than a reproduction: INP bound new physics against the SM
     short-distance amplitude; this script bounds it against the measured value. The two
     criteria coincide at O(1) only where the SM short-distance saturates experiment
     (K mixing, eps_K, B mixing) and diverge most where it does not (D mixing, which is
     long-distance dominated in the SM) -- which is exactly the row that drifted in v1.
     The assert below is renamed and documented accordingly.

  2. DELTA-M_D ROW. Headline value now quoted at the primary's own conservative bound,
     Lambda >~ 1.2e3 TeV (INP Table row), with this script's measured-value computation
     (x = 0.407%, f_D*sqrt(B) as named below) printed as a labeled secondary. The v1
     headline (1.8e3 TeV) sat 1.5x above the primary and is retired as a headline.

Everything else is unchanged from v1 (no-GIM lemma; K/eps_K/B floors; mu->3e).
Run: python 04_fcnc_bounds_v2.py
"""
import numpy as np

# ---------------- PART A: the no-GIM lemma (unchanged) ----------------
eps = np.zeros((3, 3, 3))
for a, b, c in [(0,1,2),(1,2,0),(2,0,1)]:
    eps[a,b,c], eps[a,c,b] = 1.0, -1.0
T = [-1j*eps[a] for a in range(3)]

rows = [np.kron(np.eye(3), T[a]) - np.kron(T[a].T, np.eye(3)) for a in range(3)]
u, s, vh = np.linalg.svd(np.vstack(rows))
assert int(np.sum(s < 1e-10)) == 1, "commutant must be {c*1}"

w, U = np.linalg.eigh(T[2])
Tp = U.conj().T @ (T[0] + 1j*T[1]) @ U
assert np.abs(Tp - np.diag(np.diag(Tp))).max() > 1.0   # ladder ops: O(1) FC couplings

# ---------------- PART B: tree-level floors ----------------
TEV = 1e3
hbar_GeV_s = 6.58212e-25
mK, fK, BK   = 0.497611, 0.1557, 0.7625
dMK          = 3.484e-15
epsK         = 2.228e-3
mBd, fBd_sqB = 5.27966, 0.225
dMBd         = 0.5065e12*hbar_GeV_s
mBs, fBs_sqB = 5.36692, 0.274
dMBs         = 17.765e12*hbar_GeV_s
mD, fD, BD   = 1.86484, 0.212, 0.75
dMD_measured = 6.53e-15            # x = 0.407% (HFLAV-scale), Gamma_D = 1/410.3 fs
GF           = 1.166379e-5
BR_mu3e, BR_mu3e_next = 1.0e-12, 1.0e-16

def lam_mix(dM, m, f_sqB):
    return np.sqrt((1/3)*f_sqB**2*m/dM)

def lam_epsK():
    O = (1/3)*(fK*np.sqrt(BK))**2*mK
    return 1/np.sqrt(2*np.sqrt(2)*epsK*dMK/O)

def lam_mu3e(BR):
    return 1/np.sqrt(2*GF*np.sqrt(BR))

computed = {
    "dMK (Re, 1<->2)":      lam_mix(dMK,  mK,  fK*np.sqrt(BK)),
    "epsK (Im, 1<->2)":     lam_epsK(),
    "dMD  (u, 1<->2)":      lam_mix(dMD_measured, mD, fD*np.sqrt(BD)),
    "dMBd (1<->3)":         lam_mix(dMBd, mBd, fBd_sqB),
    "dMBs (2<->3)":         lam_mix(dMBs, mBs, fBs_sqB),
    "mu->3e (SINDRUM)":     lam_mu3e(BR_mu3e),
    "mu->3e (Mu3e proj.)":  lam_mu3e(BR_mu3e_next),
}

# --- primary rows (Isidori-Nir-Perez, arXiv:1002.0900), quoted as primary ---
PRIMARY = {"dMK (Re, 1<->2)": 9.8e2*TEV, "epsK (Im, 1<->2)": 1.6e4*TEV,
           "dMD  (u, 1<->2)": 1.2e3*TEV}

# CRITERION-CONSISTENCY CHECK (not a reproduction): NP-vs-SM-short-distance (INP)
# and NP-vs-measured (here) must agree at O(1) where the SM saturates experiment,
# and within factor 2 even where it does not (D). Headlines defer to the primary.
for k, ref in PRIMARY.items():
    assert 0.5 < computed[k]/ref < 2.0, (k, computed[k]/TEV, ref/TEV)

headline = dict(computed); headline.update(PRIMARY)   # primary wins where it exists
assert headline["epsK (Im, 1<->2)"] == max(v for k, v in headline.items() if "Mu3e" not in k)

print("04_fcnc_bounds_v2: ALL CHECKS PASSED")
print("no-GIM lemma: commutant of adjoint su(2)_H is {c*1}; hierarchy => O(1) FC couplings\n")
print(f"{'channel':22s}  {'headline floor':>16s}   {'this script (vs measured)':>26s}")
for k in computed:
    h = headline[k]/TEV; c_ = computed[k]/TEV
    tag = " [primary, INP]" if k in PRIMARY else ""
    print(f"{k:22s}  > {h:11.0f} TeV{tag:16s}  ({c_:7.0f} TeV)")
print("\noperative floors: eps_K ~ 1e4 TeV (O(1) phase); dM_K ~ 1e3 TeV (real couplings)")
