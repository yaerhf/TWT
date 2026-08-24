"""III-3 probe, step 2 (v5): FADDEEV-SKYRME hopfion, matched normalisation.

Failure modes fixed, in order (each measured, each on the record):
  v1/v2  Adam on n = v/|v| -> un-threads ('Adam unwinds', project memory).
  v3     vacuum-padded box + a slowly-decaying seed -> spurious ~1/h surface energy
         (seed E2 = 1311/1710/2107 at h = .375/.25/.188, i.e. ~512 + 299/h) driving an
         artificial inward squeeze.
  v4     replicate (Neumann) padding removes the surface term but lets the texture
         SPREAD OUT OF THE BOX for free (energy outside is simply not counted), so the
         flow lowers E by leaking: E2 up 892 -> 1103, c4E4 down 846 -> 299.
  v5     compactly-supported seed (polar angle multiplied by a smooth radial cutoff, so
         n == z-hat well inside the boundary) PLUS vacuum (Dirichlet) padding: no surface
         jump AND no escape.  Projected gradient flow with backtracking (monotone E).

Normalisation: E = c2*E2 + c4*E4 with c2 = 1, c4 = K.  Etil = E/sqrt(K) is the
c2 = c4 = 1 number, directly comparable with the Skyrme hedgehog's 4 x 36.47 = 145.88.
"""
import math
import sys
import torch

dev = "cuda" if torch.cuda.is_available() else "cpu"
torch.set_default_dtype(torch.float64)


def _shift(n, dim):
    """forward neighbour, vacuum (z-hat) beyond the boundary (Dirichlet)"""
    vac = torch.zeros_like(n.narrow(dim, 0, 1)); vac[2] = 1.0
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
    d = [(_shift(n, k) - n) / h for k in (1, 2, 3)]
    F12 = (n * torch.cross(d[0], d[1], dim=0)).sum(0)
    F13 = (n * torch.cross(d[0], d[2], dim=0)).sum(0)
    F23 = (n * torch.cross(d[1], d[2], dim=0)).sum(0)
    B = torch.stack([F23, -F13, F12], dim=0)
    N = n.shape[1]
    k1 = 2 * math.pi * torch.fft.fftfreq(N, d=h).to(n.device)
    K = torch.stack([k1.view(-1, 1, 1).expand(N, N, N),
                     k1.view(1, -1, 1).expand(N, N, N),
                     k1.view(1, 1, -1).expand(N, N, N)], dim=0)
    K2 = (K ** 2).sum(0); K2 = torch.where(K2 == 0, torch.ones_like(K2), K2)
    Bh = torch.fft.fftn(B, dim=(1, 2, 3))
    cr = torch.stack([K[1] * Bh[2] - K[2] * Bh[1],
                      K[2] * Bh[0] - K[0] * Bh[2],
                      K[0] * Bh[1] - K[1] * Bh[0]], dim=0)
    A = torch.fft.ifftn(-1j * cr / K2, dim=(1, 2, 3)).real
    return float((A * B).sum() * h ** 3 / (16 * math.pi ** 2))


def seed(X, Y, Z, s, R1, R2):
    r2 = X ** 2 + Y ** 2 + Z ** 2; den = s ** 2 + r2
    p0 = (s ** 2 - r2) / den
    p1, p2, p3 = 2 * s * X / den, 2 * s * Y / den, 2 * s * Z / den
    n = torch.stack([2 * (p0 * p2 + p1 * p3),
                     2 * (p0 * p1 - p2 * p3),
                     p0 ** 2 + p3 ** 2 - p1 ** 2 - p2 ** 2], dim=0)
    n = n / n.norm(dim=0, keepdim=True)
    # compact support: theta -> chi(r) * theta  (chi = 1 inside R1, 0 outside R2)
    r = torch.sqrt(r2)
    t = ((r - R1) / (R2 - R1)).clamp(0.0, 1.0)
    chi = 1.0 - t * t * (3.0 - 2.0 * t)                   # smoothstep 1 -> 0
    n3 = n[2].clamp(-1.0, 1.0)
    th = torch.acos(n3)
    st = torch.sqrt((1.0 - n3 ** 2).clamp_min(1e-30))
    th2 = chi * th
    f = torch.sin(th2) / st
    out = torch.stack([n[0] * f, n[1] * f, torch.cos(th2)], dim=0)
    return out / out.norm(dim=0, keepdim=True)


def run(N, L, K, iters=20000, tau_fac=1 / 300.0, log=1000, tag="", scale=1.09,
        r1f=0.55, r2f=0.85, n_init=None):
    h = 2 * L / N
    ax = torch.linspace(-L + h / 2, L - h / 2, N, device=dev)
    X = ax.view(-1, 1, 1).expand(N, N, N)
    Y = ax.view(1, -1, 1).expand(N, N, N)
    Z = ax.view(1, 1, -1).expand(N, N, N)
    s = scale * math.sqrt(K)
    n = seed(X, Y, Z, s, r1f * L, r2f * L) if n_init is None else n_init.clone()
    tau = tau_fac * h ** 2

    def Eval(x):
        with torch.no_grad():
            a, b = parts(x, h)
            return float(a) + K * float(b)

    with torch.no_grad():
        e2, e4 = parts(n, h); e2, e4 = float(e2), float(e4) * K
    print(f"[{tag}] N={N} L={L} K={K} h={h:.4f} core={s:.2f} core/h={s/h:.1f} L/core={L/s:.1f}\n"
          f"        seed: E={e2+e4:.2f} Etil={(e2+e4)/math.sqrt(K):.2f} "
          f"virial={e4/e2:.3f} H={hopf(n,h):+.4f}", flush=True)

    Ecur = e2 + e4
    nrej = 0
    for it in range(iters):
        w = n.detach().requires_grad_(True)
        E2, E4 = parts(w, h)
        (g,) = torch.autograd.grad(E2 + K * E4, w)
        with torch.no_grad():
            g = (g / h ** 3)
            g = g - (g * w).sum(0, keepdim=True) * w
            for _ in range(50):
                cand = w - tau * g
                cand = cand / cand.norm(dim=0, keepdim=True)
                Enew = Eval(cand)
                if Enew <= Ecur:
                    break
                tau *= 0.5; nrej += 1
            n, Ecur = cand, Enew
            tau *= 1.02
        if (it + 1) % log == 0 or it == iters - 1:
            with torch.no_grad():
                e2, e4 = parts(n, h); e2, e4 = float(e2), float(e4) * K
            Hq = hopf(n, h)
            print(f"[{tag}]  it {it+1:6d}: E={e2+e4:9.3f} Etil={(e2+e4)/math.sqrt(K):9.3f} "
                  f"virial={e4/e2:.4f} H={Hq:+.4f} tau={tau:.2e} rej={nrej}", flush=True)
            if abs(Hq) < 0.4:
                print(f"[{tag}]  *** un-threaded ***", flush=True); break
    with torch.no_grad():
        e2, e4 = parts(n, h); e2, e4 = float(e2), float(e4) * K
    return dict(N=N, L=L, K=K, h=h, E=e2 + e4, Etil=(e2 + e4) / math.sqrt(K),
                E2=e2, c4E4=e4, H=hopf(n, h), n=n.detach())


if __name__ == "__main__":
    it = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    out = []
    for N, L, K in ((128, 26.0, 9.0), (160, 26.0, 9.0), (192, 26.0, 9.0), (192, 34.0, 16.0)):
        out.append(run(N, L, K, iters=it, log=2000, tag=f"N{N}L{int(L)}K{int(K)}"))
    print("\n=== Faddeev-Skyrme H=1, matched c2=c4=1 units ===", flush=True)
    for d in out:
        print(f"  N={d['N']:4d} L={d['L']:5.1f} h={d['h']:.4f}  Etil={d['Etil']:9.3f}  "
              f"virial={d['c4E4']/d['E2']:.4f}  H={d['H']:+.4f}")
    print(f"  Ward/VK bound scale 32 pi^2 sqrt(2)   = {32*math.pi**2*math.sqrt(2):.2f}")
    print(f"  Skyrme hedgehog B=1 in the SAME units = 4 x 36.47 = {4*36.47:.2f}")
