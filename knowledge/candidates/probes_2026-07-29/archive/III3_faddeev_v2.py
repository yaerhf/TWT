"""III-3 probe, step 2 (v2): FADDEEV-SKYRME hopfion, Hopf charge H, matched normalization.

    E(c2,c4) = c2 * INT sum_i |d_i n|^2  +  c4 * INT sum_{i<j} |d_i n x d_j n|^2
             = sqrt(c2 c4) * Etil ,      Etil = the c2 = c4 = 1 value.

The soliton size scales as sqrt(c4/c2), so we run at c2 = 1, c4 = K with K chosen to
put the core at ~10-12 lattice cells (v1 at K = 1 put it at 2.6 cells and the lattice
un-threaded it), then report Etil = E_min / sqrt(K).

Seed: Hopf projection of the degree-1 conformal map R^3 -> S^3 at scale s, pre-rescaled
to its own Derrick optimum.  Relaxation: Adam on v with n = v/|v| (exact unit norm),
autograd of the SAME discrete energy that is reported. Hopf charge monitored via the
Coulomb-gauge FFT formula H = (1/16 pi^2) INT A.B.
"""
import math
import sys
import torch

dev = "cuda" if torch.cuda.is_available() else "cpu"
DT = torch.float32


def _shift(n, dim):
    vac = torch.zeros_like(n.narrow(dim, 0, 1))
    vac[2] = 1.0
    return torch.cat([n.narrow(dim, 1, n.shape[dim] - 1), vac], dim=dim)


def parts(n, h):
    d = [(_shift(n, k) - n) / h for k in (1, 2, 3)]
    E2 = sum((di ** 2).sum() for di in d) * h ** 3
    E4 = 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            E4 = E4 + (torch.cross(d[i], d[j], dim=0) ** 2).sum()
    return E2, E4 * h ** 3


def hopf(n, h):
    n = n.double()
    d = [(_shift(n, k) - n) / h for k in (1, 2, 3)]
    F12 = (n * torch.cross(d[0], d[1], dim=0)).sum(0)
    F13 = (n * torch.cross(d[0], d[2], dim=0)).sum(0)
    F23 = (n * torch.cross(d[1], d[2], dim=0)).sum(0)
    B = torch.stack([F23, -F13, F12], dim=0)
    N = n.shape[1]
    k1 = 2 * math.pi * torch.fft.fftfreq(N, d=h).to(n.device).double()
    K = torch.stack([k1.view(-1, 1, 1).expand(N, N, N),
                     k1.view(1, -1, 1).expand(N, N, N),
                     k1.view(1, 1, -1).expand(N, N, N)], dim=0)
    K2 = (K ** 2).sum(0)
    K2 = torch.where(K2 == 0, torch.ones_like(K2), K2)
    Bh = torch.fft.fftn(B, dim=(1, 2, 3))
    cr = torch.stack([K[1] * Bh[2] - K[2] * Bh[1],
                      K[2] * Bh[0] - K[0] * Bh[2],
                      K[0] * Bh[1] - K[1] * Bh[0]], dim=0)
    A = torch.fft.ifftn(-1j * cr / K2, dim=(1, 2, 3)).real
    return float((A * B).sum() * h ** 3 / (16 * math.pi ** 2))


def seed(X, Y, Z, s, m=1):
    r2 = X ** 2 + Y ** 2 + Z ** 2
    den = s ** 2 + r2
    p0 = (s ** 2 - r2) / den
    p1, p2, p3 = 2 * s * X / den, 2 * s * Y / den, 2 * s * Z / den
    n = torch.stack([2 * (p0 * p2 + p1 * p3),
                     2 * (p0 * p1 - p2 * p3),
                     p0 ** 2 + p3 ** 2 - p1 ** 2 - p2 ** 2], dim=0)
    if m != 1:
        phi = torch.atan2(Y, X)
        u = (n[0] + 1j * n[1]).to(torch.complex64) / (1 - n[2] + 1e-7)
        u = u * torch.exp(1j * (m - 1) * phi.to(torch.complex64))
        a = u.abs() ** 2
        n = torch.stack([2 * u.real / (1 + a), 2 * u.imag / (1 + a), (a - 1) / (1 + a)], dim=0)
    return n / n.norm(dim=0, keepdim=True)


def run(N, L, K, m=1, iters=20000, lr=2e-2, tag=""):
    h = 2 * L / N
    ax = torch.linspace(-L + h / 2, L - h / 2, N, device=dev, dtype=DT)
    X = ax.view(-1, 1, 1).expand(N, N, N)
    Y = ax.view(1, -1, 1).expand(N, N, N)
    Z = ax.view(1, 1, -1).expand(N, N, N)
    s = 0.646 * math.sqrt(K) * (1.0 if m == 1 else 1.3)
    n0 = seed(X, Y, Z, s, m)
    with torch.no_grad():
        E2, E4 = parts(n0, h)
        E2, E4 = float(E2), float(E4) * K
        print(f"[{tag}] seed s={s:.3f} h={h:.4f} core/h={s/h:.1f} L/core={L/s:.1f}: "
              f"E={E2+E4:.2f} (E2={E2:.2f} c4E4={E4:.2f} ratio={E4/E2:.3f}) "
              f"H={hopf(n0, h):+.4f}   [Derrick-opt of this shape: {2*math.sqrt(E2*E4):.2f}]",
              flush=True)

    v = n0.clone().requires_grad_(True)
    opt = torch.optim.Adam([v], lr=lr)
    sch = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=iters, eta_min=lr / 200)
    best = None
    for it in range(iters):
        opt.zero_grad(set_to_none=True)
        n = v / v.norm(dim=0, keepdim=True)
        E2, E4 = parts(n, h)
        E = E2 + K * E4
        E.backward()
        opt.step(); sch.step()
        if (it + 1) % 2000 == 0 or it == iters - 1:
            with torch.no_grad():
                nn = v / v.norm(dim=0, keepdim=True)
                e2, e4 = parts(nn, h)
                e2, e4 = float(e2), float(e4) * K
                Hq = hopf(nn, h)
                print(f"[{tag}]  it {it+1:6d}: E={e2+e4:9.3f}  Etil={(e2+e4)/math.sqrt(K):9.3f}  "
                      f"virial c4E4/E2={e4/e2:.4f}  H={Hq:+.4f}", flush=True)
                best = (e2 + e4, e2, e4, Hq)
    return dict(N=N, L=L, h=h, K=K, m=m, E=best[0], Etil=best[0] / math.sqrt(K),
                E2=best[1], c4E4=best[2], H=best[3])


if __name__ == "__main__":
    m = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    out = []
    for N, L, K in ((128, 12.0, 9.0), (160, 15.0, 9.0), (192, 15.0, 9.0)):
        out.append(run(N, L, K, m=m, tag=f"m{m} N{N} L{L}"))
    print("\n=== summary (Faddeev-Skyrme, matched c2=c4=1 units) ===", flush=True)
    for d in out:
        print(f"  N={d['N']:4d} L={d['L']:5.1f} h={d['h']:.4f} core/h~{0.646*math.sqrt(d['K'])/d['h']:.1f}  "
              f"Etil={d['Etil']:9.3f}  virial={d['c4E4']/d['E2']:.4f}  H={d['H']:+.4f}")
    print(f"  Ward/VK bound scale 32 pi^2 sqrt(2)      = {32*math.pi**2*math.sqrt(2):.2f}")
    print(f"  Skyrme hedgehog B=1 in the SAME units    = 4 x 36.47 = {4*36.47:.2f}")
