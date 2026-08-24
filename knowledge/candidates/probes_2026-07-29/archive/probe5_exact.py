"""PROBE 5: exact (sympy, symbolic-in-f) derivation of h_tk on the B=1 Q-orbit
hedgehog with the R-128 mass rotor, + particle/antiparticle sign, + long-range fall-off."""
import sys, os, math, itertools
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import numpy as np, sympy as sp
import twt
from twt import MV, e, I4, SCALAR
from texture_h_full16_baryon import Hmat, PROFILES, Qhat, g0, h, grid_points

# ---------- exact symbolic Clifford Cl(4,0) over sympy -----------------------
BL = [()] + [tuple(c) for k in range(1, 5) for c in itertools.combinations((1, 2, 3, 4), k)]
IDX = {b: i for i, b in enumerate(BL)}

def bmul(a, b):
    s = 1; out = list(a)
    for x in b:
        j = len(out)
        while j > 0 and out[j-1] > x:
            s = -s; j -= 1
        if j > 0 and out[j-1] == x:
            out = out[:j-1] + out[j:]           # e_i^2 = +1 in Cl(4,0)
        else:
            out = out[:j] + [x] + out[j:]
    return s, tuple(out)

def mul(A, B):
    C = [sp.Integer(0)] * 16
    for i, ai in enumerate(A):
        if ai == 0: continue
        for j, bj in enumerate(B):
            if bj == 0: continue
            s, bl = bmul(BL[i], BL[j])
            C[IDX[bl]] += s * ai * bj
    return C

def sc(A): return sp.simplify(A[0])
def blade(b, c=1):
    v = [sp.Integer(0)]*16; v[IDX[b]] = sp.sympify(c); return v
def add(*vs):
    out = [sp.Integer(0)]*16
    for v in vs:
        for i in range(16): out[i] += v[i]
    return out
def smul(s, v): return [sp.simplify(s*x) for x in v]

x1, x2, x3, t = sp.symbols('x1 x2 x3 t', real=True)
k4 = sp.Symbol('k4', positive=True)
r = sp.sqrt(x1**2 + x2**2 + x3**2)
f = sp.Function('f')(r)
rh = [x1/r, x2/r, x3/r]

Qh = add(blade((1,4), rh[0]), blade((2,4), rh[1]), blade((3,4), rh[2]))
Rh = add(blade((), sp.cos(f)), smul(sp.sin(f), Qh))
I4v = blade((1,2,3,4))
u   = mul(I4v, Qh)                        # R-128 lock axis (co-rotating)
th  = k4*t
q   = add(blade((), sp.cos(th/2)), smul(sp.sin(th/2), u))
R   = mul(Rh, q)

def rev(A):
    return [A[i]*(-1)**(len(BL[i])*(len(BL[i])-1)//2) for i in range(16)]

def d(A, v): return [sp.diff(a, v) for a in A]

Rr = rev(R)
coords = [t, x1, x2, x3]
print("building symbolic Omega_mu ... (this takes a moment)")
Om = [mul(Rr, d(R, c)) for c in coords]

def hsym(A, B): return sp.simplify(mul(A, mul(I4v, B))[0])

# evaluate on the t=0 slice with a generic symbolic f
sub0 = {t: 0}
Om0 = [[sp.simplify(a.subs(sub0)) for a in O] for O in Om]

print("\n=== EXACT symbolic h_mn on the t=0 slice (generic f(r)) ===")
H = sp.zeros(4, 4)
for a in range(4):
    for b in range(4):
        H[a, b] = sp.simplify(hsym(Om0[a], Om0[b]))
lbl = ["t", "1", "2", "3"]
for a in range(4):
    for b in range(4):
        val = sp.simplify(sp.trigsimp(H[a, b]))
        print(f"  h_{lbl[a]}{lbl[b]} = {val}")

print("\n  => EXACT, generic f:  h_tt = 0,  h_kl = 0,  h_tk = -(k4/2) f'(r) rhat_k")

# ---------------------------------------------------------------- sign flip
print("\n=== particle/antiparticle (u -> -u) sign flip ===")
prof = PROFILES["pi*exp(-r)"]
p = [0.7, -0.4, 1.1]
Hp, _ = Hmat(p+[0.0], prof, "A_I4Qhat", 0.83)
Hm, _ = Hmat(p+[0.0], prof, "A_minus", 0.83)
print("  h_t(+u) =", Hp[0,1:], "\n  h_t(-u) =", Hm[0,1:],
      "\n  max|H(+)+H(-)| =", np.max(np.abs(Hp+Hm)))

# ---------------------------------------------------------------- fall-off
print("\n=== radial fall-off of h_tr (is there a 1/r Newtonian tail?) ===")
for pn in ["pi*exp(-r)", "2*atan(1/r^2)", "pi/(1+r^2)"]:
    pf = PROFILES[pn]
    print(f"  {pn}:")
    for rr in (0.5, 1, 2, 4, 8, 16):
        H, _ = Hmat([rr, 0, 0, 0.0], pf, "A_I4Qhat", 1.0)
        print(f"     r={rr:5.1f}  h_tr={H[0,1]:+.6e}   r*h_tr={rr*H[0,1]:+.4e}"
              f"   r^2*h_tr={rr*rr*H[0,1]:+.4e}   r^3*h_tr={rr**3*H[0,1]:+.4e}")
