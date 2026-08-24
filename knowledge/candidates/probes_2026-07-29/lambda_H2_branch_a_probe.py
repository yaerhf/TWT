"""
Review item II-10 probe: is the DYNAMICAL reading of `Lambda ~ H^2` excluded?

Branch (a) DYNAMICAL: rho_vac(t) = 3*nu*Mpl_red^2 * H(t)^2 at ALL epochs (nu = O(1)).
Branch (b) COINCIDENCE: rho_vac = const, and rho_vac ~ Mpl_red^2 H_0^2 is a statement
           about TODAY only.

Every empirical input is named + primary-source-verified (see the report). No invented
numbers. READ-ONLY probe; no project file is modified.
"""
import math

# ------------------------------------------------------------------ VERIFIED INPUTS
# [V1] Planck 2018 VI, arXiv:1807.06209 (abstract, verbatim-checked):
#      Omega_m = 0.315 +/- 0.007 ; H0 = (67.4 +/- 0.5) km/s/Mpc ; N_eff = 2.99 +/- 0.17
Omega_m0 = 0.315
Omega_L0 = 1.0 - Omega_m0          # flat LCDM, radiation negligible today
h        = 0.674
N_eff_planck, N_eff_planck_sig = 2.99, 0.17

# [V2] Planck 2015 XIV (DE & modified gravity), arXiv:1502.01590 Sect. 5.1.5, VERBATIM:
#      "we find that it has to be below ~2% (at 95% confidence) of the critical density
#       even when forced to play a role for z<50 only."
Omega_e_bound_95 = 0.02            # and this is the RELAXED (late-onset) case

# [V3] BBN 2024 baryon-abundance update, arXiv:2401.15054 (abstract, verbatim-checked):
#      "These additional relics themselves are constrained to Delta N_eff = -0.10 +/- 0.21
#       by light element abundances alone."
dNeff_bbn_mean, dNeff_bbn_sig = -0.10, 0.21

# [V4] Running-vacuum state of the art: Sola Peracaula, Gomez-Valent, de Cruz Perez,
#      Moreno-Pulido, arXiv:2102.12758, Eq.(1):
#         rho_vac(H) = 3/(8 pi G_N) * ( c0 + nu H^2 + nutilde Hdot ) + O(H^4),
#      "the additive constant c0 is fixed by the boundary condition rho_vac(H0)=rho_vac^0".
#      Table 1 baseline: nu_eff = 0.00024 (+0.00039/-0.00040), with nu_eff == nu/4.
nu_eff_fit, nu_eff_hi = 0.00024, 0.00039
nu_rvm_fit   = 4*nu_eff_fit
nu_rvm_95_up = 4*(nu_eff_fit + 2*nu_eff_hi)

# radiation composition (standard, for the equivalent-energy translation)
f_nu = 7.0/8.0 * (4.0/11.0)**(4.0/3.0)
N_eff_std = 3.044

print("="*78); print("PART 1 -- what branch (a) FORCES (pure algebra, no data)"); print("="*78)
print("""
Flat Friedmann:      3 Mpl^2 H^2 = rho_m + rho_r + rho_vac
Branch (a) ansatz:   rho_vac     = 3 nu Mpl^2 H^2        (nu constant)
Substitute:          3 Mpl^2 H^2 (1 - nu) = rho_m + rho_r

  =>  Omega_vac(z)  ==  rho_vac / (3 Mpl^2 H^2)  ==  nu     FOR EVERY z.

This is an identity, not an approximation. Under branch (a) the vacuum FRACTION is
epoch-independent: it cannot be ~0.69 today and negligible at recombination/BBN.
Reproducing today therefore forces""")
nu = Omega_L0
print(f"        nu = Omega_Lambda,0 = {nu:.4f}")
print(f"   and hence Omega_vac(z) = {nu:.4f} at z = 0, 0.6, 1090, 3400, 1e9  -- all epochs.")

print("""
Consequence 2: the expansion history collapses to ONE power law.
Total conservation with w_vac = -1 and rho_vac = (nu/(1-nu)) rho_fluid gives
   rho_fluid ~ a^-3(1+w)(1-nu),  a(t) ~ t^{2/[3(1+w)(1-nu)]},
   q = -1 - Hdot/H^2 = -1 + (3/2)(1+w)(1-nu) = CONSTANT.""")
for label, w in (("matter-like fluid (w=0)", 0.0), ("radiation-like fluid (w=1/3)", 1/3)):
    q = -1.0 + 1.5*(1.0+w)*(1.0-nu); p = 2.0/(3.0*(1.0+w)*(1.0-nu))
    print(f"   {label:28s}:  q = {q:+.4f} (const),  a ~ t^{p:.3f}")
# LCDM transition redshift from the SAME Planck parameters (qddot=0: 2 Om_L = Om_m (1+z)^3)
z_t = (2*Omega_L0/Omega_m0)**(1/3) - 1
print(f"""   => q is CONSTANT: NO deceleration->acceleration transition at any redshift.
      Flat LCDM with the SAME Planck 2018 parameters puts the transition at
        1+z_t = (2 Omega_L / Omega_m)^(1/3)  =>  z_t = {z_t:.3f}
      (consistent with the SNe+BAO kinematic measurements z_t ~ 0.6-0.7).
      A constant q is not "a transition at the wrong z"; it is NO transition at all.""")

print(); print("="*78); print("PART 2 -- confront Omega_early = %.4f with the data" % nu); print("="*78)
print(f"""
 [CMB]  Planck 2015 XIV Sect. 5.1.5 (verbatim): early DE "has to be below ~2% (at 95%
        confidence) of the critical density even when forced to play a role for z<50 only."
        That {Omega_e_bound_95:.2%} is the WEAKEST case; for DE present since recombination it is tighter.
        branch (a):  Omega_e = {nu:.4f}   ->  exceeds the bound by {nu/Omega_e_bound_95:.0f}x""")

rho_vac_over_rho_r = nu/(1.0-nu)
rho_r_over_rho_gamma = 1.0 + f_nu*N_eff_std
dNeff_equiv = rho_vac_over_rho_r * rho_r_over_rho_gamma / f_nu
bbn_95_up = dNeff_bbn_mean + 2*dNeff_bbn_sig
planck_95_up = (N_eff_planck + 2*N_eff_planck_sig) - N_eff_std
print(f"""
 [BBN]  extra energy density at T ~ MeV, as an EQUIVALENT Delta N_eff:
        rho_vac/rho_rad = nu/(1-nu)               = {rho_vac_over_rho_r:.4f}
        rho_rad/rho_gamma = 1 + {f_nu:.4f}*{N_eff_std}      = {rho_r_over_rho_gamma:.4f}
        => Delta N_eff(equivalent)                = {dNeff_equiv:.2f}
        vs BBN light elements alone (arXiv:2401.15054): Delta N_eff = {dNeff_bbn_mean:+.2f} +/- {dNeff_bbn_sig:.2f}
           => 95% upper ~ {bbn_95_up:+.2f};  branch (a) exceeds it by {dNeff_equiv/bbn_95_up:.0f}x
        vs Planck 2018 VI N_eff = {N_eff_planck} +/- {N_eff_planck_sig}
           => 95% upper Delta N_eff ~ {planck_95_up:+.2f};  branch (a) exceeds it by {dNeff_equiv/planck_95_up:.0f}x
        CAVEAT (stated, not hidden): a w=-1 component is not radiation, so this is an
        EQUIVALENT-ENERGY translation, quoted only to size the violation. The conclusion
        does not rest on it -- the CMB Omega_e comparison above is direct.""")

# matter-radiation equality under branch (a)
Omega_r0 = 4.15e-5/h**2
a_eq_std = Omega_r0/Omega_m0
a_eq_a   = (Omega_r0/Omega_m0)**(1.0/(1.0-nu))
print(f"""
 [z_eq]  independent of the above: with rho_m ~ a^-3(1-nu), rho_r ~ a^-4(1-nu),
         equality moves to a_eq = (Omega_r0/Omega_m0)^(1/(1-nu)).
         standard   z_eq = {1/a_eq_std - 1:,.0f}   (Planck 2018 VI measures z_eq to <1%)
         branch (a) z_eq = {1/a_eq_a - 1:.3e}   -> off by {(1/a_eq_a-1)/(1/a_eq_std-1):.1e}x""")

print(); print("="*78); print("PART 3 -- branch (a) vs the studied model class (RVM)"); print("="*78)
print(f"""
Running-vacuum models are EXACTLY this form -- and the literature form always keeps the
additive constant:   rho_vac(H) = (3/8 pi G_N)( c0 + nu H^2 + nutilde Hdot ) + O(H^4),
c0 fixed by rho_vac(H0) = rho_vac^0   [arXiv:2102.12758 Eq.(1), verbatim].
That is BRANCH (b) PLUS a small H^2 running. Branch (a) is the c0 = 0 corner with nu = O(1).
Best fits (arXiv:2102.12758 Table 1, baseline, nu_eff = nu/4):
   nu_eff = {nu_eff_fit} (+{nu_eff_hi}/-0.00040)  =>  nu = {nu_rvm_fit:.5f}, 95% upper nu <~ {nu_rvm_95_up:.5f}
   branch (a) needs nu = {nu:.4f}  ->  exceeds the fitted 95% upper by {nu/nu_rvm_95_up:,.0f}x""")

print(); print("="*78); print("PART 4 -- the fork, and why BOTH prongs kill the dark-energy claim"); print("="*78)
print(f"""
(a1)  nu = O(1), i.e. the Lambda~H^2 residual IS the observed dark energy.
      EXCLUDED: {nu/Omega_e_bound_95:.0f}x over the Planck early-DE bound, {dNeff_equiv/bbn_95_up:.0f}x over the BBN
      Delta N_eff bound, z_eq off by ~1e8, and no acceleration transition at all.

(a2)  nu <~ 1e-3, i.e. the residual survives the data.
      Then Omega_vac(today) = nu <~ 1e-3, NOT {nu:.3f}. The residual is a sub-per-mille
      correction and is NOT the observed dark energy. The claim "dark energy is small,
      nonzero, and tied to the front dynamics" does not follow; something else must
      supply 69% of the energy budget, and TWT does not supply it.

So the dynamical reading is a strict dichotomy: EXCLUDED, or NOT DARK ENERGY.
Either way the dark-energy claim cannot stand as stated.

(b)   rho_vac = const, with rho_vac = c Mpl_red^2 H_0^2, c = 3 Omega_Lambda,0 = {3*Omega_L0:.3f}.
      Survives trivially -- but note it is near-DEFINITIONAL: in a flat FRW universe
      rho_vac/(Mpl_red^2 H_0^2) = 3 Omega_Lambda,0 is the definition of Omega_Lambda,0
      rearranged. Its physical content is one bit -- that Omega_Lambda,0 is O(1) rather
      than 1e-120, i.e. the coincidence problem restated, not a predicted value.
      The engine's C6b_spin0_target already uses H_0 (not H(t)), so the ENGINE is already
      on branch (b); it is the PAPER prose that reads dynamical.""")
print("="*78)
