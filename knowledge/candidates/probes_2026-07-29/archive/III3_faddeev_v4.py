"""III-3 probe, step 2 (v4): FADDEEV-SKYRME hopfion, matched normalisation, FREE (Neumann)
boundaries + projected gradient flow with backtracking.

Two defects of v1-v3 fixed here:
  * v1/v2 used Adam on n = v/|v| -> the texture un-threaded ('Adam unwinds', project memory).
  * v3 padded the box with the vacuum z-hat, which puts a spurious ~1/h-divergent surface
    energy on the boundary shell (measured: seed E2 = 1311/1710/2107 at h = .375/.25/.188,
    i.e. E2 ~ 512 + 299/h) and drives an artificial inward squeeze.  v4 uses replicate
    (Neumann) padding: the forward difference vanishes on the last plane, so the only
    boundary error is the omitted tail, which shrinks as L grows and is checked by an
    L-sequence.

Normalisation: E = c2*E2 + c4*E4, c2 = 1, c4 = K; Etil = E/sqrt(K) is the c2 = c4 = 1
number directly comparable with the Skyrme hedgehog's 4 x 36.47 = 145.88.
"""
import math
import sys
import torch

dev = "cuda" if torch.cuda.is_available() else "cpu"
torch.set_default_dtype(torch.float64)


def _shift(n, dim):
    """forward neighbour with REPLICATE (free) boundary"""
    last = n.narrow(dim, n.shape[dim] - 1, 1)
    return torch.cat([n.narrow(dim, 1, n.shape[dim] - 1), last], dim=dim)


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


def seed(X, Y, Z, s):
    r2 = X ** 2 + Y ** 2 + Z ** 2; den = s ** 2 + r2
    p0 = (s ** 2 - r2) / den
    p1, p2, p3 = 2 * s * X / den, 2 * s * Y / den, 2 * s * Z / den
    n = torch.stack([2 * (p0 * p2 + p1 * p3),
                     2 * (p0 * p1 - p2 * p3),
                     p0 ** 2 + p3 ** 2 - p1 ** 2 - p2 ** 2], dim=0)
    return n / n.norm(dim=0, keepdim=True)


def run(N, L, K, iters=20000, tau_fac=1 / 300.0, log=1000, tag="", n_init=None):
    h = 2 * L / N
    ax = torch.linspace(-L + h / 2, L - h / 2, N, device=dev)
    X = ax.view(-1, 1, 1).expand(N, N, N)
    Y = ax.view(1, -1, 1).expand(N, N, N)
    Z = ax.view(1, 1, -1).expand(N, N, N)
    s = 1.09 * math.sqrt(K)   # Derrick-optimal scale of THIS seed shape (measured)
    n = seed(X, Y, Z, s) if n_init is None else n_init.clone()
    tau = tau_fac * h ** 2

    def Eval(x):
        with torch.no_grad():
            a, b = parts(x, h)
            return float(a) + K * float(b)

    with torch.no_grad():
        e2, e4 = parts(n, h); e2, e4 = float(e2), float(e4) * K
    print(f"[{tag}] N={N} L={L} K={K} h={h:.4f} core/h={s/h:.1f} L/core={L/s:.1f}\n"
          f"        seed: E={e2+e4:.2f} Etil={(e2+e4)/math.sqrt(K):.2f} "
          f"virial={e4/e2:.3f} H={hopf(n,h):+.4f}", flush=True)

    Ecur = e2 + e4
    nrej = 0
    for it in range(iters):
        w = n.detach().requires_grad_(True)
        E2, E4 = parts(w, h)
        (g,) = torch.autograd.grad(E2 + K * E4, w)
        with torch.no_grad():
            g = g / h ** 3
            g = g - (g * w).sum(0, keepdim=True) * w
            for _ in range(40):
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
    for N, L, K in ((96, 12.0, 9.0), (128, 12.0, 9.0), (160, 15.0, 9.0), (192, 15.0, 9.0)):
        out.append(run(N, L, K, iters=it, tag=f"N{N}L{int(L)}"))
    print("\n=== Faddeev-Skyrme H=1, matched c2=c4=1 units ===", flush=True)
    for d in out:
        print(f"  N={d['N']:4d} L={d['L']:5.1f} h={d['h']:.4f} core/h~{1.09*math.sqrt(d['K'])/d['h']:.1f} "
              f" Etil={d['Etil']:9.3f}  virial={d['c4E4']/d['E2']:.4f}  H={d['H']:+.4f}")
    print(f"  Ward/VK bound scale 32 pi^2 sqrt(2)   = {32*math.pi**2*math.sqrt(2):.2f}")
    print(f"  Skyrme hedgehog B=1 in the SAME units = 4 x 36.47 = {4*36.47:.2f}")
