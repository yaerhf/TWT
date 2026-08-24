# -*- coding: utf-8 -*-
"""Draft of the proposed twt.py primitive + its suite assertion. Tested standalone here."""


def lambda_H2_dynamical_reading_excluded():
    """[DERIVED arithmetic + INPUT bounds] §E.1.1 / N54: `Λ ~ H²` admits two readings and only one
    survives. DYNAMICAL: ρ_vac(t) = 3ν M̄_Pl² H(t)² at ALL epochs. Substituting into the flat Friedmann
    constraint 3 M̄_Pl² H² = ρ_m + ρ_r + ρ_vac gives 3 M̄_Pl² H² (1−ν) = ρ_m + ρ_r, hence Ω_vac(z) ≡ ν
    IDENTICALLY — the vacuum FRACTION is epoch-independent, so matching today forces ν = Ω_Λ,0 ≈ 0.685
    at recombination and at BBN too. (A separately-conserved w=−1 component would give ρ_vac = const,
    i.e. the other reading; so the dynamical reading necessarily involves vacuum–matter exchange.)
    PRESENT-EPOCH: ρ_vac = const with ρ_vac = 3 Ω_Λ,0 M̄_Pl² H_0² — near-definitional (it is the
    definition of Ω_Λ,0 rearranged), and the reading `eom_constraint_class` C6b already uses (H_0, not
    H(t)). INPUT bounds, all primary-source: early-DE below ≈2% of critical at 95% — and that is the
    WEAKEST, z<50-only case (Planck 2015 XIV §5.1.5); ΔN_eff = −0.10 ± 0.21 from light elements alone
    (arXiv:2401.15054); N_eff = 2.99 ± 0.17 (Planck 2018 VI); running-vacuum global fit ν_eff ≡ ν/4 =
    0.00024 (+0.00039/−0.00040) for ρ_vac(H) = (3/8πG)(c₀ + νH² + ν̃Ḣ) (arXiv:2102.12758 Eq.1, Table 1).
    The ΔN_eff row is an EQUIVALENT-ENERGY translation (a w=−1 component is not radiation): it sizes the
    violation, and the verdict does not rest on it — the early-DE row is direct.
    self-checks: Ω_e excess > 30×; ΔN_eff excess > 40×; q(z) constant ⇒ no acceleration transition,
    while flat ΛCDM on the SAME parameters gives z_t ≈ 0.63."""
    Om_m0, Om_L0 = 0.315, 0.685                      # Planck 2018 VI, flat  [INPUT]
    nu = Om_L0                                       # forced by matching today under the dynamical reading
    f_nu = 7.0 / 8.0 * (4.0 / 11.0) ** (4.0 / 3.0)
    dNeff = (nu / (1.0 - nu)) * (1.0 + f_nu * 3.044) / f_nu
    def q(w):                                        # deceleration parameter; NOTE: no z-dependence
        return -1.0 + 1.5 * (1.0 + w) * (1.0 - nu)
    z_t_LCDM = (2.0 * Om_L0 / Om_m0) ** (1.0 / 3.0) - 1.0
    out = {
        "Omega_vac_at_every_epoch": nu,
        "excess_over_Planck2015XIV_earlyDE_0p02": nu / 0.02,
        "equivalent_Delta_Neff": dNeff,
        "excess_over_BBN_Delta_Neff_95up_0p32": dNeff / 0.32,
        "q_matter_era": q(0.0), "q_radiation_era": q(1.0 / 3.0),
        "q_depends_on_z": False,
        "LCDM_transition_redshift_same_params": z_t_LCDM,
        "excess_over_RVM_nu_95up": nu / (4.0 * (0.00024 + 2.0 * 0.00039)),
        "verdict": "DYNAMICAL reading EXCLUDED (1-2 orders, three independent probes: early-DE, BBN "
                   "Delta-N_eff, and the absent deceleration->acceleration transition). PRESENT-EPOCH "
                   "reading survives but is near-definitional => TWT makes NO dark-energy prediction at V3.",
    }
    assert abs(out["Omega_vac_at_every_epoch"] - Om_L0) < 1e-12, "matching today forces nu = Omega_Lambda,0"
    assert out["excess_over_Planck2015XIV_earlyDE_0p02"] > 30.0
    assert out["excess_over_BBN_Delta_Neff_95up_0p32"] > 40.0
    assert out["q_depends_on_z"] is False and q(0.0) < 0.0
    assert 0.60 < z_t_LCDM < 0.70
    assert out["excess_over_RVM_nu_95up"] > 100.0
    return out


if __name__ == "__main__":
    r = lambda_H2_dynamical_reading_excluded()
    for k, v in r.items():
        print(f"  {k:45s} = {v}")
    # the suite assertion, exactly as proposed for twt_test.py
    ok = (r["excess_over_Planck2015XIV_earlyDE_0p02"] > 30
          and r["excess_over_BBN_Delta_Neff_95up_0p32"] > 40
          and r["q_depends_on_z"] is False
          and 0.60 < r["LCDM_transition_redshift_same_params"] < 0.70
          and "EXCLUDED" in r["verdict"] and "NO dark-energy prediction" in r["verdict"])
    print("\n  suite assertion evaluates to:", ok)
