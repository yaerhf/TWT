import io, sys
B = r"C:/Users/hfyae/Claude/Projects/Deepseek/knowledge/corpus/"
T = io.open(B + "twt.py", encoding="utf-8").read()
S = io.open(B + "twt_test.py", encoding="utf-8").read()

A = {}

A["P1 twt.py ratio-docstring"] = (T, '''    values is therefore IDENTICALLY c_lat (checked below to ~1e-14 for ARBITRARY c_lat) — the
    factor "~21.6" IS c_lat = (Lambda_eff * a)^2, the squared number of lattice spacings in the
    effective cutoff. R-163 says as much itself ("lands exactly on the sakharov_induced_gravity
    form"; its cross-tie Lambda_eff/M_red = 4 pi is c_lat-INDEPENDENT).''')

A["P2 twt.py E=0 docstring"] = (T, '''    E = 0 is forced by the SAME left-Spin(4) shift symmetry R-041 uses for xi = 0: an endomorphism
    is a NON-DERIVATIVE quadratic operator phi.W.phi, exactly the class the symmetry forbids
    (checked below on the Weitzenbock shape as well as a generic W). Hence''')

A["P3 twt.py foregone-conclusion"] = (T, '''    THE TEXTBOOK VALUE IS TWT'S OWN MODE-CONTENT VALUE — and that was NOT a foregone conclusion.
    The excluded readings are computed here and one of them FLIPS THE SIGN OF G:''')

A["P4 twt.py three_way_resolution"] = (T, '''        "three_way_resolution": {
            "verdict": "NOT three values of one coefficient — ONE value in three variables/states",
            "1/12": "c_reg in the proper-time-cutoff variable = TWT's own mode-content value (here)",
            "~1.82": "the SAME coefficient with Lambda := 1/a; the excess factor is IDENTICALLY "
                     "c_lat = (Lambda_eff * a)^2 (residual %.1e over arbitrary c_lat)" % ident,
            "~1": "a never-computed paper placeholder — SUPERSEDED, not a rival",''')

A["P5 twt_test.py reconciliation _ck"] = (S, '''    _ck("THE RECONCILIATION: the two BANKED values are NOT rivals — 1/(16 pi G) = N_eff c_lat/"
        "(192 pi^2 a^2) reads c_reg = c_lat/12 at Lambda := 1/a and c_reg = 1/12 at Lambda := "
        "Lambda_eff = sqrt(c_lat)/a, so their ratio is IDENTICALLY c_lat = (Lambda_eff*a)^2 for "
        "ARBITRARY c_lat (residual < 1e-12) — the factor '~21.6' IS c_lat. The '~1' paper placeholder "
        "was never computed and is SUPERSEDED. What remains OPEN is NOT c_reg but c_lat",
        "IDENTICALLY" in crg["three_way_resolution"]["~1.82"]
        and "SUPERSEDED" in crg["three_way_resolution"]["~1"]
        and "ONE value in three variables" in crg["three_way_resolution"]["verdict"]
        and "c_lat" in crg["three_way_resolution"]["what is actually OPEN"])''')

A["P6 twt_test.py trailing print"] = (S, '''    print("        => c_reg = 1/12 for TWT's OWN mode content (6 minimal/Bochner channels, E=0 by the "
          "R-041 shift symmetry); the '~21.6 disagreement' IS c_lat, a change of Lambda-variable; the "
          "OA-LF-ii exposure lives entirely in c_lat/a, NOT in the induced-G coefficient.")''')

ok = True
for k, (hay, a) in A.items():
    c = hay.count(a)
    print("%-38s count=%d  %s" % (k, c, "OK" if c == 1 else "*** FAIL ***"))
    ok &= (c == 1)
print("ALL ANCHORS UNIQUE" if ok else "ANCHOR PROBLEM")
sys.exit(0 if ok else 1)
