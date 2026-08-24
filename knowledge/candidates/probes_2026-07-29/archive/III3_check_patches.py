import io, sys
sys.stdout.reconfigure(encoding="utf-8")

R4 = ("| R-055 | Electron as Hopf defect on L-orbit; QCP scaling `f_L = f_π · (1 − D/J)^{9/2}` at L1 "
      "| DERIVED-CONDITIONAL | electron_two_windings + electron_QCP_nu + electron_f_L_MeV | C.1 | A-1c, R-007 | — "
      "| The `f_L` SCALING is untouched. The `f_L → m_e` CONVERSION is not: III-3 (2026-07-29) finds the "
      "section's `e_L = √36.47 ≈ 6.04` is (a) not an eigenvalue — `36.47` is the ANW hedgehog BVP eigenvalue "
      "and enters as `M_0 = 36.47 f_π/e`, so `m_e = f_L · e_L` silently SETS the L-sector Skyrme COUPLING to "
      "`√36.47` (an undeclared, uncounted INPUT/FIT with no engine primitive and no derivation in the corpus), "
      "and (b) borrowed from the wrong model for an S²-director Hopf defect. In the matched normalisation "
      "(`c₂ = f_π²/8`, `c₄ = 1/(2e²)`, `√(c₂c₄) = f_π/(4e)`) the Skyrme hedgehog `B = 1` minimum is "
      "`145.85 = 4 × 36.46` while the RIGOROUS Vakulenko–Kapitanski floor for any Faddeev-Skyrme `H = 1` "
      "configuration is `32π²(3/16)^{3/8} = 168.59` — strictly above it, so `36.47` cannot be a hopfion "
      "eigenvalue. Literature hopfion value `552.1` ⇒ analogue coefficient `138.0` (×3.79), which moves the "
      "quoted residuals from 36% / 4.4% to ×2.64 in `f_L` and 13.8% in the exponent. The `f_L → m_e` factor is "
      "therefore an OPEN, uncounted input and the 4.4% figure is model-choice-dependent. L2 mechanism "
      "unidentified (`ν = 3π/2 = 4.712`, CANDIDATE). |")

R5 = ("| `m_e` via L-orbit QCP scaling | DERIVED-CONDITIONAL-plus-OPEN-INPUT | R-055 | `electron_f_L_MeV`, "
      "`electron_QCP_nu` | `f_L` scaling: 36% on `f_L`, 4.4% in exponent. The `f_L → m_e` conversion `e_L = "
      "√36.47` is an UNDECLARED coupling choice borrowed from the wrong (hedgehog, not hopfion) model — III-3, "
      "2026-07-29; on the Faddeev-Skyrme analogue `138.0` the residuals become ×2.64 and 13.8%. L2 mechanism "
      "unidentified. |")

for nm, r, want in (("R4", R4, 9), ("R5", R5, 6)):
    n = r.count("|")
    print(f"{nm}: pipes = {n} (want {want}) {'OK' if n == want else 'MISMATCH'}")
    print("   ", r[:120], "...")
