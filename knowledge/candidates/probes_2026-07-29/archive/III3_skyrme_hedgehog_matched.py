"""III-3 probe, step 1: the ANW hedgehog BVP recomputed in the MATCHED (c2=c4=1)
normalization, to fix the unit dictionary between the Skyrme and Faddeev-Skyrme models.

Matched normalization (derived, not assumed):
    Skyrme   E = c2 * INT sum_i |a_i|^2  +  c4 * INT sum_{i<j} |a_i x a_j|^2 ,  a_i = su(2) current
    Faddeev  E = c2 * INT sum_i |d_i n|^2 +  c4 * INT sum_{i<j} |d_i n x d_j n|^2

with (ANW conventions) c2 = f_pi^2/8, c4 = 1/(2 e^2).  Check: substituting the hedgehog
and x = e f_pi r reproduces the engine's own radial density
    u = x^2 F'^2/8 + sin^2F/4 + sin^2F F'^2 + sin^4F/(2 x^2),  M = 4 pi (f_pi/e) INT u dx
(twt.skyrmion_rotational_band_nucleon_delta docstring).  Hence sqrt(c2 c4) = f_pi/(4e),
so a dimensionless energy Etil (couplings set to 1) maps to  E = Etil * f_pi/(4e),
i.e. Etil(B=1) must equal 4 * 36.47 = 145.88.
"""
import math
import torch

torch.set_default_dtype(torch.float64)

R, M = 60.0, 6000
r = torch.linspace(R / M, R, M)
dr = float(r[1] - r[0])
rr = torch.cat([torch.zeros(1), r, torch.tensor([R + dr])])
rm = 0.5 * (rr[1:] + rr[:-1])
drs = rr[1:] - rr[:-1]

Fint = (math.pi * torch.exp(-r / 1.5)).clone().requires_grad_(True)


def parts(Fint):
    F = torch.cat([torch.tensor([math.pi]), Fint, torch.zeros(1)])
    Fp = (F[1:] - F[:-1]) / drs
    Fm = 0.5 * (F[1:] + F[:-1])
    s2 = torch.sin(Fm) ** 2
    w = 4 * math.pi * rm ** 2 * drs
    E2 = (w * (Fp ** 2 + 2 * s2 / rm ** 2)).sum()
    E4 = (w * (s2 / rm ** 2) * (2 * Fp ** 2 + s2 / rm ** 2)).sum()
    return E2, E4


opt = torch.optim.LBFGS([Fint], max_iter=4000, tolerance_grad=1e-14,
                        tolerance_change=1e-18, history_size=100,
                        line_search_fn="strong_wolfe")
for cycle in range(6):
    def closure():
        opt.zero_grad()
        E2, E4 = parts(Fint)
        E = E2 + E4
        E.backward()
        return E
    opt.step(closure)
    with torch.no_grad():
        E2, E4 = parts(Fint)
    print(f"  cycle {cycle}: Etil = {float(E2+E4):.4f}")

with torch.no_grad():
    E2, E4 = parts(Fint)
Etil = float(E2 + E4)
print("\nSkyrme hedgehog B=1, matched units (c2=c4=1)")
print(f"  Etil               = {Etil:.3f}")
print(f"  Etil/4             = {Etil/4:.4f}      <- must reproduce the banked 36.47")
print(f"  4 * 36.47          = {4*36.47:.3f}")
print(f"  rel. deviation     = {abs(Etil - 4*36.47)/(4*36.47)*100:.3f} %")
print(f"  E2 = {float(E2):.3f}  E4 = {float(E4):.3f}  E4/E2 = {float(E4/E2):.5f} (Derrick: 1)")
