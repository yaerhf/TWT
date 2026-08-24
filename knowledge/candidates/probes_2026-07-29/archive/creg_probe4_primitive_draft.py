"""PROBE 4 — draft + timing test of a candidate engine primitive
`c_reg_from_substrate_mode_content`. Run standalone against the live twt module.
READ-ONLY probe (nothing in the corpus is edited).
"""
import sys, os, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import twt
from twt import e, SCALAR, sakharov_induced_gravity, sakharov_xi_minimal_coupling


def c_reg_from_substrate_mode_content():
    """[DERIVED-A (the a_1 TYPE-SUM arithmetic, exact S^4 spectra) + DERIVED-given-(R-112 linear
    face AND R-041 xi=0, whose FRAMING+CONDITIONAL status is INHERITED)] — c_reg computed for
    TWT's OWN mode content, and the three-way c_reg 'disagreement' identified as a
    Lambda-VARIABLE artifact, not a physics disagreement.

    THE OLD STATE (sakharov_induced_gravity()['c_reg_reconciliation_OPEN']): three values of the
    R-linear regulator coefficient in the paper's parametrization
        1/(16 pi G) = c_reg * N_eff * Lambda^2 / (16 pi^2)
    were carried as unreconciled — ~1 (paper placeholder), 1/12 (textbook heat kernel), ~1.82
    (induced_G_from_linear_face_band / R-163, = c_lat/12) — the two banked ones a factor ~21.6
    apart. That entry's own would_change_if named the exit: "the two primitives' measures are
    shown to be the same object in different variables." THIS PRIMITIVE MEETS THAT CONDITION.

    (1) THE TYPE-SUM, FOR TWT'S ACTUAL MODE CONTENT. a_1 is a SIGNED weighted sum over mode
    TYPES, not a count: for a Laplace-type D = -(nabla^2 + E) on a bundle V,
        a_1 = tr_V( E + (R/6) 1_V ),      c_reg = (1/2) * (a_1/R) / N_eff.
    TWT's linear face (R-112 / D.4.6 Face 1, banked): the 6 grade-2 so(4) coefficient fields,
    free operator, NO endomorphism and NO mass at quadratic order; the kinetic term is the
    sigma-model <Omega_mu Omega^mu>_0 (R-109), whose curved continuation is the BOCHNER operator
    (delta_AB is the target Killing form, metric-independent). No fermionic channel exists on the
    linear face (matter = defect = soliton, canon SS0/SS5, not a linear-face field); the photon is
    already ONE OF the 6 grade-2 strain modes (B.5.4) — not a separate gauge sector, so there is
    no double count and no gauge/ghost weight.
    E = 0 is forced by the SAME left-Spin(4) shift symmetry R-041 uses for xi = 0: an endomorphism
    is a NON-DERIVATIVE quadratic operator phi.W.phi, exactly the class the symmetry forbids
    (checked below on the Weitzenbock-shaped W as well as a generic one). Hence
        a_1 = 6 * R/6 = R      =>      c_reg = 1/12   EXACTLY.
    THE TEXTBOOK VALUE IS TWT'S OWN MODE-CONTENT VALUE — and this was NOT a foregone conclusion:
    the excluded readings are computed here and one of them FLIPS THE SIGN OF G.
        conformal (xi = 1/6):                 a_1 = 0    -> c_reg = 0     (no induced gravity)
        Lambda^2 with the HODGE operator:     a_1 = -R   -> c_reg = -1/12 (REPULSIVE, G < 0)
        6 minimal / Bochner (TWT's):          a_1 = +R   -> c_reg = +1/12 (attractive)
    So the mode-TYPE question was capable of zeroing or reversing induced gravity; the substrate's
    content lands on +1/12.

    (2) THE '~1.82' IS THE SAME NUMBER IN A DIFFERENT VARIABLE. R-163 assembles
    1/(16 pi G) = N_eff*c_lat/(192 pi^2 a^2). Reading Lambda := 1/a gives c_reg = c_lat/12; reading
    Lambda := Lambda_eff = sqrt(c_lat)/a gives c_reg = 1/12. The ratio of the two banked values is
    therefore IDENTICALLY c_lat (checked to 0 below, for arbitrary c_lat) — the factor "~21.6" IS
    c_lat = (Lambda_eff * a)^2, i.e. the squared number of lattice spacings in the effective
    cutoff. R-163 says so itself ("lands exactly on the sakharov_induced_gravity form"; the
    cross-tie Lambda_eff/M_red = 4 pi is c_lat-INDEPENDENT).
    => c_reg is ONE value, 1/12, in the Sakharov proper-time-cutoff variable. The '~1' placeholder
    is superseded (it was never computed). WHAT REMAINS OPEN IS NOT c_reg BUT c_lat.

    (3) AND c_lat IS EXACTLY THE OA-LF-ii-SENSITIVE OBJECT. Deforming the monad-scale curvature
    weight as w(s) = (R/6)*f(s/a^2) with f -> 1 for s >> a^2 and f = kappa for s < a^2 gives an
    EXACTLY AFFINE c_lat(kappa) whose slope is R-163's own ~93% proper-time support fraction
    (checked below to ~1e-14). OA-LF-ii's own stated tolerance ("up to O(1)"), read as
    kappa in [1/2, 2], moves c_lat by a factor ~3.6 — where R-163's quoted refinement window is
    only -5%..-25% (that window addresses the GAP/state question, i.e. OA-LF-i-class, not the
    OPERATOR clause). So the SAME quantity is (a) the whole of the alleged factor-21.6 and (b) the
    whole of the OA-LF-ii exposure: decisive that the two are not rival values of one coefficient.
    CONSEQUENCE, both ways: c_reg = 1/12 carries ZERO OA-LF-ii sensitivity; "c_reg ~ 1.82" carries
    ~93%-linear OA-LF-ii sensitivity. R-163's branch is WEAKER as a c_reg determination than its
    quoted window suggests, and correspondingly its content is relocated to where it belongs — the
    monad spacing a, which is what actually moves.

    SCOPE FENCE. This does NOT derive G, does NOT move N_eff (still GENERIC-given-dim-4), does NOT
    retire OA-LF-i/ii, and does NOT by itself re-cut the [0.13, 2.5] M_Pl bracket (a separate
    adjudication: which Lambda each downstream consumer needs — Lambda_eff for the Sakharov
    coefficient, 1/a for lattice-dispersion quantities). It removes ONE recorded OPEN item: the
    c_reg three-way disagreement. Tier is capped by R-041 (FRAMING+CONDITIONAL) — the xi=0/E=0
    step is symmetry-protected, not #1-gap-derived.

    self-checks: exact S^4 spectra reproduce a_1 = R/6 (1 scalar), R (6 scalars), -R (Lambda^2
    Hodge) and -R/3 (Lambda^1 Hodge) with a_0 = 1/6/6/4; Weitzenbock-shaped and generic
    endomorphisms are shift-NON-invariant while <Omega Omega>_0 is invariant; the c_reg ratio
    equals c_lat identically; c_lat(kappa) affine with slope = the s<a^2 support fraction.
    """
    import math
    import numpy as np

    Rc, Vol = 12.0, 8 * math.pi ** 2 / 3.0          # unit S^4

    def _a01(levels, a0_expect):
        F, A0 = [], []
        for s in (1e-3, 5e-4):
            lmax = int(math.sqrt(200.0 / s)) + 60
            K = sum(d * math.exp(-s * lam) for lam, d in levels(lmax))
            x = K * (4 * math.pi * s) ** 2 / Vol
            A0.append(x); F.append((x - a0_expect) / s)
        return 2 * A0[1] - A0[0], 2 * F[1] - F[0]   # Richardson in s

    def _scalars(lmax, n):
        return [(l * (l + 3), n * (l + 1) * (l + 2) * (2 * l + 3) / 6.0) for l in range(lmax + 1)]

    def _coexact(lmax, p, n=4):                      # coexact p-forms on S^4
        return [((l + p) * (l + n - p - 1),
                 (2 * l + n - 1) * math.factorial(l + n - 1)
                 / ((l + p) * (l + n - p - 1) * math.factorial(p)
                    * math.factorial(n - p - 1) * math.factorial(l - 1)))
                for l in range(1, lmax + 1)]

    a0_1, a1_1 = _a01(lambda L: _scalars(L, 1), 1.0)
    a0_6, a1_6 = _a01(lambda L: _scalars(L, 6), 6.0)
    a0_2f, a1_2f = _a01(lambda L: _coexact(L, 2) + _coexact(L, 1), 6.0)
    a0_1f, a1_1f = _a01(lambda L: _coexact(L, 1) + _coexact(L, 0), 4.0)
    assert abs(a0_1 - 1) < 1e-4 and abs(a1_1 - Rc / 6) < 1e-4, (a0_1, a1_1)
    assert abs(a0_6 - 6) < 1e-3 and abs(a1_6 - Rc) < 1e-3, (a0_6, a1_6)
    assert abs(a0_2f - 6) < 1e-3 and abs(a1_2f + Rc) < 1e-3, (a0_2f, a1_2f)   # HODGE: a_1 = -R
    assert abs(a0_1f - 4) < 1e-3 and abs(a1_1f + Rc / 3) < 1e-3, (a0_1f, a1_1f)
    assert int(_coexact(2, 1)[0][1] + 0.5) == 10, "S^4 Killing-vector level must be 10"

    N_eff = 6
    creg = lambda a1: 0.5 * (a1 / Rc) / N_eff
    c_min, c_conf, c_hodge = creg(a1_6), creg(0.0), creg(a1_2f)
    assert abs(c_min - 1 / 12) < 1e-4 and abs(c_hodge + 1 / 12) < 1e-4 and c_hodge < 0 < c_min

    # --- E = 0 is forced by the SAME shift symmetry as xi = 0 (R-041) -----------------
    xi = sakharov_xi_minimal_coupling()
    assert xi["left_invariance_err"] < 1e-8 and xi["xi_term_breaks_shift_symmetry"] is True
    assert xi["N_eff"] == 6
    rng = np.random.default_rng(7)
    Wg = rng.normal(size=(6, 6)); Wg = 0.5 * (Wg + Wg.T)
    Ww = (Rc / 3.0) * np.eye(6)                       # the Lambda^2 Weitzenbock shape, p(n-p)K
    phi = np.array([0.31, -0.17, 0.44, 0.09, -0.28, 0.36])
    sh = np.array([0.10, 0.0, -0.05, 0.07, 0.0, 0.0])
    endo_shift_breaks = {}
    for nm, W in (("generic", Wg), ("Weitzenbock R/3", Ww)):
        b, a = float(phi @ W @ phi), float((phi + sh) @ W @ (phi + sh))
        endo_shift_breaks[nm] = abs(a - b) > 1e-9
    assert all(endo_shift_breaks.values()), "an endomorphism must break the left-Spin(4) shift"

    # --- the parametrization identity: ratio == c_lat, identically -------------------
    def _cregs(c_lat_val):
        A = (16 * math.pi ** 2) / (192 * math.pi ** 2)                       # Lambda = proper-time cutoff
        B_inv_a = (16 * math.pi ** 2) * c_lat_val / (192 * math.pi ** 2)     # Lambda = 1/a
        B_eff = B_inv_a / c_lat_val                                          # Lambda = Lambda_eff
        return A, B_inv_a, B_eff
    ident = max(abs(_cregs(c)[1] / _cregs(c)[0] - c) for c in (1.0, 5.0, 21.8285, 137.0))
    assert ident < 1e-12, "c_reg ratio must be IDENTICALLY c_lat; residual %.3e" % ident
    A0, B0, Be0 = _cregs(21.8285)
    assert abs(A0 - 1 / 12) < 1e-12 and abs(Be0 - 1 / 12) < 1e-12 and abs(B0 - 1.819) < 1e-3
    sg = sakharov_induced_gravity()
    assert abs(math.sqrt(math.pi / (A0 * N_eff)) - sg["Lambda_over_MPl_nonreduced"]) < 1e-12, \
        "c_reg = 1/12 must reproduce sakharov's Lambda/M_Pl(non-reduced) = sqrt(2 pi)"

    # --- OA-LF-ii sensitivity: c_lat(kappa) is EXACTLY affine, slope = s<a^2 support --
    prs = [tuple(1 if k == i else (sg_ if k == j else 0) for k in range(4))
           for i in range(4) for j in range(i + 1, 4) for sg_ in (+1, -1)]
    assert len(prs) == 12
    Ng = 16
    x = 2 * math.pi * (np.arange(Ng) + 0.5) / Ng
    axes = [x.reshape([Ng if k == m else 1 for k in range(4)]) for m in range(4)]
    om2 = np.zeros((Ng,) * 4)
    for b in prs:
        om2 += 2.0 * (1.0 - np.cos(sum(bi * ax for bi, ax in zip(b, axes) if bi != 0)))
    q = om2 / 6.0
    C = lambda arr: 16 * math.pi ** 2 * 0.5 * float(arr.mean())
    c_base = C(1.0 / q)
    c_k = lambda kap: C(kap * (1.0 - np.exp(-q)) / q + np.exp(-q) / q)
    c_at0 = c_k(0.0)
    slope = c_base - c_at0
    lin = max(abs(c_at0 + slope * k - c_k(k)) for k in (0.5, 2.0, 4.0))
    assert lin < 1e-9, "c_lat(kappa) must be affine; residual %.3e" % lin
    frac_s = slope / c_base
    assert 0.90 <= frac_s <= 0.95, "OA-LF-ii support slope out of range: %.4f" % frac_s
    O1_lo, O1_hi = c_k(0.5), c_k(2.0)
    assert O1_hi / O1_lo > 3.0, "O(1) tolerance on OA-LF-ii must move c_lat by > 3x"

    a_of = lambda cl: math.sqrt(N_eff * cl / (12 * math.pi))
    Leff = lambda cl: math.sqrt(cl) / a_of(cl)
    assert max(abs(Leff(cl) - math.sqrt(2 * math.pi)) for cl in (1.5, 21.83, 90.0)) < 1e-12, \
        "Lambda_eff must be EXACTLY c_lat-independent"

    return {
        "tier": ("DERIVED-A (the a_1 TYPE-SUM arithmetic — exact S^4 spectra) + "
                 "DERIVED-given-(R-112 linear face AND R-041 xi=0/E=0), INHERITING R-041's "
                 "FRAMING+CONDITIONAL status. NOT a derivation of G; N_eff stays "
                 "GENERIC-given-dim-4; OA-LF-i/ii NOT retired"),
        "c_reg": 1 / 12,
        "c_reg_variable": ("Lambda = the SAKHAROV PROPER-TIME CUTOFF. State the variable every time "
                           "c_reg is quoted — that is the whole of the old 'disagreement'"),
        "mode_content": {
            "channels": 6, "type": "real bosonic, massless, E = 0 (Bochner), sigma-model kinetic",
            "fermionic channels": "NONE on the linear face (matter = defect = soliton, not a field)",
            "gauge sector": "NONE separate — the photon is one of the 6 grade-2 strain modes (B.5.4)",
            "why E = 0": "an endomorphism is a NON-DERIVATIVE quadratic phi.W.phi — the exact class "
                         "the left-Spin(4) shift symmetry forbids (R-041); checked on the "
                         "Weitzenbock shape too",
            "endomorphism_shift_breaks": endo_shift_breaks,
        },
        "a1_type_sum_S4": {
            "1 minimal scalar": round(a1_1, 6), "R/6": Rc / 6,
            "6 minimal scalars (TWT)": round(a1_6, 6), "R": Rc,
            "Lambda^2 HODGE (Weitzenbock)": round(a1_2f, 6),
            "Lambda^1 HODGE (cross-check)": round(a1_1f, 6),
        },
        "excluded_readings_would_have": {
            "conformal xi=1/6": {"a_1": 0.0, "c_reg": c_conf, "consequence": "NO induced gravity"},
            "Hodge / 2-form": {"a_1": round(a1_2f, 4), "c_reg": round(c_hodge, 6),
                               "consequence": "G < 0 — REPULSIVE gravity (the mode-TYPE question "
                                              "was capable of flipping the sign)"},
            "TWT (6 minimal / Bochner)": {"a_1": round(a1_6, 4), "c_reg": round(c_min, 6),
                                          "consequence": "G > 0 attractive"},
        },
        "three_way_resolution": {
            "verdict": "NOT three values of one coefficient — ONE value in three variables/states",
            "1/12": "c_reg in the proper-time-cutoff variable = TWT's own mode-content value (here)",
            "~1.82": "the SAME coefficient with Lambda := 1/a; excess factor is IDENTICALLY c_lat "
                     "= (Lambda_eff * a)^2 (residual %.1e over arbitrary c_lat)" % ident,
            "~1": "a never-computed paper placeholder — SUPERSEDED, not a rival",
            "what is actually OPEN": "c_lat, i.e. how many lattice spacings the effective cutoff "
                                     "is — a DIFFERENT question, and the OA-LF-ii-sensitive one",
        },
        "OA_LF_ii_sensitivity": {
            "c_lat(kappa) affine": "c_lat = %.4f + %.4f*kappa (residual %.1e)" % (c_at0, slope, lin),
            "slope fraction (= R-163's s<a^2 support)": round(frac_s, 4),
            "O(1) tolerance kappa in [1/2,2]": "c_lat in [%.2f, %.2f] — factor %.1f"
                                               % (O1_lo, O1_hi, O1_hi / O1_lo),
            "=> a in": "[%.2f, %.2f] ell_Planck" % (a_of(O1_lo), a_of(O1_hi)),
            "=> 1/a in": "[%.3f, %.3f] M_Pl" % (1 / a_of(O1_hi), 1 / a_of(O1_lo)),
            "R-163's quoted window": "-5%..-25% — that is the GAP/state (OA-LF-i-class) question, "
                                     "NOT the OPERATOR clause; it UNDERSTATES the OA-LF-ii exposure "
                                     "by more than an order of magnitude",
            "what does NOT move": "Lambda_eff = sqrt(c_lat)/a = sqrt(2 pi) M_Pl EXACTLY, for every "
                                  "c_lat — so c_reg = 1/12 carries ZERO OA-LF-ii sensitivity while "
                                  "'c_reg ~ 1.82' carries ~93%-linear sensitivity",
        },
        "scope_fence": ("removes ONE recorded OPEN item (the c_reg three-way disagreement). Does NOT "
                        "derive G, does NOT move N_eff, does NOT retire OA-LF-i/ii, and does NOT by "
                        "itself re-cut the [0.13, 2.5] M_Pl bracket — that needs a separate ruling on "
                        "WHICH Lambda each consumer needs (Lambda_eff for the Sakharov coefficient; "
                        "1/a for lattice-dispersion quantities such as the E1/VG-6 eta4 exposure)"),
    }


t0 = time.time()
out = c_reg_from_substrate_mode_content()
dt = time.time() - t0
import json
print(json.dumps(out, indent=1, default=str))
print("\nRUNTIME: %.2f s" % dt)
