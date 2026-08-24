"""ENGINE COUNTER-COMPUTATION.  Claim under test (docstring of
continuous_anomaly_ledger): "The ledger is a property OF the banked slot pattern,
not of any nearby variant."   Feed the engine's own primitive a NEARBY variant table
and see whether the ledger still passes."""
import sys, twt_core as tc

orig = tc.generation_spectrum

def swapped_singlets():
    """SM table with the two RH-quark electric charges EXCHANGED:
    Q(u_R) = -1/3, Q(d_R) = +2/3, everything else untouched.
    This is a manifest violation of premise P5 (Q chirality-independent) and is
    NOT the Standard Model."""
    t = list(orig())
    out = []
    for lbl, t3, q, m in t:
        if lbl == "u_R": q = -1/3
        elif lbl == "d_R": q = 2/3
        out.append((lbl, t3, q, m))
    return out

def zero_doublet_world():
    """Yq = Yl = 0 branch of the solution surface: doublets neutral in Y,
    u_R^c/d_R^c opposite, e_R^c neutral.  Also not the Standard Model."""
    return [("nu_L", 0.5, 0.5, 1), ("e_L", -0.5, -0.5, 1),
            ("u_L", 0.5, 0.5, 3), ("d_L", -0.5, -0.5, 3),
            ("e_R", 0.0, 0.0, 1),
            ("u_R", 0.0, 0.5, 3), ("d_R", 0.0, -0.5, 3)]

for name, fn in [("SM (banked)", orig), ("u_R<->d_R charge swap (P5 VIOLATED)", swapped_singlets),
                 ("Y-neutral-doublet world", zero_doublet_world)]:
    tc.generation_spectrum = fn
    try:
        d = tc.continuous_anomaly_ledger()
        print(f"{name:38s} -> A1={d['A1 [SU(2)]^2 U(1)_Y']} A2={d['A2 [U(1)_Y]^3']} "
              f"A3={d['A3 grav^2 U(1)_Y']} doublets={d['doublet_count']} "
              f"n={d['n_states_gauged']}+1  LEDGER PASSES")
        print(f"{'':38s}    counterfactual dict = {d['counterfactuals']}")
    except AssertionError as e:
        print(f"{name:38s} -> ASSERT FIRED: {e}")
    tc.generation_spectrum = orig
