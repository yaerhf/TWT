"""III-3 probe, step 2: the FADDEEV-SKYRME hopfion energy at Hopf charge H, computed
in the SAME matched normalization used for the Skyrme hedgehog (c2 = c4 = 1):

    E = INT d^3x [ sum_i |d_i n|^2  +  sum_{i<j} |d_i n x d_j n|^2 ]
      = INT d^3x [ (d_i n)^2 + (1/2) F_ij F_ij ],   F_ij = n . (d_i n x d_j n)

(the second form is the standard Faddeev-Skyrme / Battye-Sutcliffe normalization:
 (1/2) sum_{i,j} F_ij^2 = sum_{i<j} F_ij^2 and |F_ij| = |d_i n x d_j n| because
 d_i n _|_ n.)

Seed: n = Hopf-project( degree-1 conformal map R^3 -> S^3 ), scale s.  Hopf invariant of
(Hopf o deg-d) = d, so the seed has H = 1 exactly in the continuum.
For H = 2 we use the toroidal ansatz with doubled azimuthal winding.

Relaxation: unconstrained v in R^3 with n = v/|v| (exact unit constraint), Adam warm-up
then LBFGS, autograd on the SAME discrete energy that is reported.
Hopf charge monitored by the FFT/Coulomb-gauge formula H = (1/(16 pi^2)) INT A.B,
B_i = (1/2) eps_ijk F_jk, A = curl^{-1} B in Coulomb gauge.
"""
import math
import sys
import torch

torch.set_default_dtype(torch.float64)
dev = "cuda" if torch.cuda.is_available() else "cpu"


# ---------------------------------------------------------------- discretisation
def _shift(n, dim):
    """forward neighbour, vacuum (z-hat) beyond the boundary"""
    vac = torch.zeros_like(n.narrow(dim, 0, 1))
    vac[2] = 1.0
    return torch.cat([n.narrow(dim, 1, n.shape[dim] - 1), vac], dim=dim)


def energy_parts(n, h):
    d = [(_shift(n, k) - n) / h for k in (1, 2, 3)]
    E2 = sum((di ** 2).sum() for di in d) * h ** 3
    E4 = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            cr = torch.cross(d[i], d[j], dim=0)
            E4 = E4 + (cr ** 2).sum()
    E4 = E4 * h ** 3
    return E2, E4


# ---------------------------------------------------------------- Hopf charge
def hopf_charge(n, h):
    d = [(_shift(n, k) - n) / h for k in (1, 2, 3)]
    F12 = (n * torch.cross(d[0], d[1], dim=0)).sum(0)
    F13 = (n * torch.cross(d[0], d[2], dim=0)).sum(0)
    F23 = (n * torch.cross(d[1], d[2], dim=0)).sum(0)
    B = torch.stack([F23, -F13, F12], dim=0)          # B_i = (1/2) eps_ijk F_jk
    N = n.shape[1]
    k1 = 2 * math.pi * torch.fft.fftfreq(N, d=h).to(n.device)
    KX = k1.view(-1, 1, 1).expand(N, N, N)
    KY = k1.view(1, -1, 1).expand(N, N, N)
    KZ = k1.view(1, 1, -1).expand(N, N, N)
    K = torch.stack([KX, KY, KZ], dim=0)
    K2 = (K ** 2).sum(0)
    K2 = torch.where(K2 == 0, torch.ones_like(K2), K2)
    Bh = torch.fft.fftn(B, dim=(1, 2, 3))
    # A = curl^{-1} B (Coulomb gauge):  A_hat = -i k x B_hat / k^2
    cross = torch.stack([K[1] * Bh[2] - K[2] * Bh[1],
                         K[2] * Bh[0] - K[0] * Bh[2],
                         K[0] * Bh[1] - K[1] * Bh[0]], dim=0)
    Ah = -1j * cross / K2
    A = torch.fft.ifftn(Ah, dim=(1, 2, 3)).real
    return float((A * B).sum() * h ** 3 / (16 * math.pi ** 2))


# ---------------------------------------------------------------- seeds
def seed_H1(X, Y, Z, s):
    r2 = X ** 2 + Y ** 2 + Z ** 2
    den = s ** 2 + r2
    p0 = (s ** 2 - r2) / den
    p1, p2, p3 = 2 * s * X / den, 2 * s * Y / den, 2 * s * Z / den
    n1 = 2 * (p0 * p2 + p1 * p3)
    n2 = 2 * (p0 * p1 - p2 * p3)
    n3 = p0 ** 2 + p3 ** 2 - p1 ** 2 - p2 ** 2
    return torch.stack([n1, n2, n3], dim=0)


def seed_Hm(X, Y, Z, s, m):
    """toroidal ansatz with azimuthal winding m: H = m (m=1 reduces to the above class).
    Take the H=1 field's complex Riemann coordinate u = (n1 + i n2)/(1 - n3) and raise
    the azimuthal phase: u -> |u| e^{i(arg u + (m-1) phi)}."""
    n = seed_H1(X, Y, Z, s)
    if m == 1:
        return n
    phi = torch.atan2(Y, X)
    u = (n[0] + 1j * n[1]) / (1 - n[2] + 1e-14)
    u = u * torch.exp(1j * (m - 1) * phi)
    a = u.abs() ** 2
    n1 = 2 * u.real / (1 + a)
    n2 = 2 * u.imag / (1 + a)
    n3 = (a - 1) / (1 + a)
    return torch.stack([n1, n2, n3], dim=0)


# ---------------------------------------------------------------- driver
def run(N=96, L=8.0, s=1.5, m=1, adam_iters=3000, lbfgs_cycles=8, lr=3e-3, tag=""):
    h = 2 * L / N
    ax = torch.linspace(-L + h / 2, L - h / 2, N, device=dev)
    X = ax.view(-1, 1, 1).expand(N, N, N)
    Y = ax.view(1, -1, 1).expand(N, N, N)
    Z = ax.view(1, 1, -1).expand(N, N, N)
    n0 = seed_Hm(X, Y, Z, s, m)
    n0 = n0 / n0.norm(dim=0, keepdim=True)

    with torch.no_grad():
        E2, E4 = energy_parts(n0, h)
        print(f"[{tag}] seed  N={N} L={L} h={h:.4f} s={s} m={m}: "
              f"E={float(E2+E4):.3f} (E2={float(E2):.3f}, E4={float(E4):.3f}) "
              f"H={hopf_charge(n0, h):+.4f}")

    v = n0.clone().requires_grad_(True)

    def E_of_v():
        n = v / v.norm(dim=0, keepdim=True)
        E2, E4 = energy_parts(n, h)
        return E2 + E4

    opt = torch.optim.Adam([v], lr=lr)
    for it in range(adam_iters):
        opt.zero_grad(); E = E_of_v(); E.backward(); opt.step()
        if (it + 1) % 1000 == 0:
            with torch.no_grad():
                nn = v / v.norm(dim=0, keepdim=True)
                E2, E4 = energy_parts(nn, h)
                print(f"[{tag}]  adam {it+1:5d}: E={float(E2+E4):9.3f} "
                      f"E2={float(E2):8.3f} E4={float(E4):8.3f} "
                      f"E4/E2={float(E4/E2):.4f} H={hopf_charge(nn, h):+.4f}")

    lb = torch.optim.LBFGS([v], max_iter=500, history_size=60,
                           tolerance_grad=1e-12, tolerance_change=1e-16,
                           line_search_fn="strong_wolfe")
    for c in range(lbfgs_cycles):
        def closure():
            lb.zero_grad(); E = E_of_v(); E.backward(); return E
        lb.step(closure)
        with torch.no_grad():
            nn = v / v.norm(dim=0, keepdim=True)
            E2, E4 = energy_parts(nn, h)
            print(f"[{tag}]  lbfgs {c}: E={float(E2+E4):9.4f} "
                  f"E2={float(E2):8.3f} E4={float(E4):8.3f} "
                  f"E4/E2={float(E4/E2):.5f} H={hopf_charge(nn, h):+.5f}")

    with torch.no_grad():
        nn = v / v.norm(dim=0, keepdim=True)
        E2, E4 = energy_parts(nn, h)
        return dict(N=N, L=L, h=h, m=m, E=float(E2 + E4), E2=float(E2),
                    E4=float(E4), H=hopf_charge(nn, h))


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "h1"
    out = []
    if mode == "h1":
        for N, L in ((64, 8.0), (96, 8.0), (128, 8.0), (128, 10.0)):
            out.append(run(N=N, L=L, s=1.5, m=1, tag=f"H1 N{N} L{L}"))
    elif mode == "h2":
        for N, L in ((96, 8.0), (128, 8.0)):
            out.append(run(N=N, L=L, s=1.8, m=2, tag=f"H2 N{N} L{L}"))
    print("\n=== summary ===")
    for d in out:
        print(f"  N={d['N']:4d} L={d['L']:4.1f} h={d['h']:.4f} m={d['m']}  "
              f"E={d['E']:9.3f}  E4/E2={d['E4']/d['E2']:.4f}  H={d['H']:+.4f}")
    print(f"  reference: 32 pi^2 sqrt(2) = {32*math.pi**2*math.sqrt(2):.2f} "
          f"(Vakulenko-Kapitanski / Ward class lower-bound scale)")
    print(f"  Skyrme B=1 in the SAME units = 4 * 36.47 = {4*36.47:.2f}")
