"""PROBE 3: robustness of h_tk != 0 on the mass-carrying B=1 Q-orbit baryon."""
import sys, os, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import numpy as np
import twt
from twt import MV, e, I4, SCALAR
from texture_h_full16_baryon import (Hmat, PROFILES, Qhat, g0, h, grid_points,
                                     rand_SO3, rand_rotor, rotor_hedgehog,
                                     uhat_of, LBL)

rng = random.Random(20260729)

# ---------------------------------------------------------------- (1) x4 slices
print("=== (1) dependence on the meta-time slice x4 (case A, co-rotating I4*Qhat) ===")
prof = PROFILES["pi*exp(-r)"]
x = [0.7, -0.4, 1.1]
r = np.linalg.norm(x)
for x4 in (0.0, 0.3, 0.9, 1.7, 3.0, -1.1):
    H, _ = Hmat(x + [x4], prof, "A_I4Qhat", 0.83)
    print(f"  x4={x4:+5.2f}  h_tt={H[0,0]:+.3e}  h_t=({H[0,1]:+.6f},{H[0,2]:+.6f},{H[0,3]:+.6f})"
          f"  max|h_kl|={np.max(np.abs(H[1:,1:])):.3e}")

# ---------------------------------------------------------------- (2) FD delta convergence
print("\n=== (2) finite-difference step independence ===")
for d in (1e-3, 1e-4, 1e-5, 1e-6, 1e-7):
    H, _ = Hmat(x + [0.0], prof, "A_I4Qhat", 0.83, delta=d)
    print(f"  delta={d:.0e}  h_t1={H[0,1]:.10f}  max|h_kl|={np.max(np.abs(H[1:,1:])):.3e}"
          f"  h_tt={H[0,0]:.3e}")

# ---------------------------------------------------------------- (3) grid refinement
print("\n=== (3) grid refinement, case A, profile pi*exp(-r), k4=0.83 ===")
for n in (5, 7, 9, 11, 13):
    pts = grid_points(n, box=3.0)
    mtt = mkl = mtk = 0.0
    for p in pts:
        H, _ = Hmat(p + [0.0], prof, "A_I4Qhat", 0.83)
        mtt = max(mtt, abs(H[0, 0])); mkl = max(mkl, np.max(np.abs(H[1:, 1:])))
        mtk = max(mtk, np.max(np.abs(H[0, 1:])))
    print(f"  n={n:2d} ({len(pts):5d} pts): max|h_tt|={mtt:.3e} max|h_kl|={mkl:.3e} max|h_tk|={mtk:.3e}")
print("  + 4000 random points in the box:")
mtt = mkl = mtk = 0.0
for _ in range(4000):
    p = [rng.uniform(-3, 3) for _ in range(3)]
    if np.linalg.norm(p) < 0.05: continue
    H, _ = Hmat(p + [0.0], prof, "A_I4Qhat", 0.83)
    mtt = max(mtt, abs(H[0, 0])); mkl = max(mkl, np.max(np.abs(H[1:, 1:])))
    mtk = max(mtk, np.max(np.abs(H[0, 1:])))
print(f"      max|h_tt|={mtt:.3e} max|h_kl|={mkl:.3e} max|h_tk|={mtk:.3e}")

# ------------------------------------------------- (4) orientation freedom
print("\n=== (4) orientation freedom: 200 independent trials ===")
print("  each trial: random SO(3) rotation of the hedgehog field, random constant")
print("  right-multiplying rotor A0, random profile, random k4, random point, random x4")
names = list(PROFILES)
survive = 0; tot = 0
mn_tk = 1e30; mx_tk = 0.0; mx_tt = 0.0; mx_kl = 0.0
for t in range(200):
    O = rand_SO3(rng); A0 = rand_rotor(rng)
    pn = names[rng.randrange(len(names))]
    k4 = rng.uniform(0.2, 2.0)
    p = [rng.uniform(-2.5, 2.5) for _ in range(3)]
    if np.linalg.norm(p) < 0.2: continue
    x4 = rng.uniform(-2, 2)
    H, _ = Hmat(p + [x4], PROFILES[pn], "A_I4Qhat", k4, Ospat=O, Aright=A0)
    tk = np.max(np.abs(H[0, 1:]))
    tot += 1
    if tk > 1e-6: survive += 1
    mn_tk = min(mn_tk, tk); mx_tk = max(mx_tk, tk)
    mx_tt = max(mx_tt, abs(H[0, 0])); mx_kl = max(mx_kl, np.max(np.abs(H[1:, 1:])))
print(f"  trials={tot}  h_tk nonzero in {survive}/{tot}")
print(f"  |h_tk| range [{mn_tk:.3e}, {mx_tk:.3e}]   max|h_tt|={mx_tt:.3e}  max|h_kl|={mx_kl:.3e}")

# ------------------------------------------------- (5) left- vs right-multiplied phase
print("\n=== (5) left- vs right-multiplied mass phase (case A) ===")
def rotor_left(x4v, prof, k4):
    x3 = x4v[:3]
    Rh = rotor_hedgehog(x3, prof)
    u = uhat_of("A_I4Qhat", x3, prof)
    th = k4 * x4v[3]
    q = math.cos(th/2)*SCALAR + math.sin(th/2)*u
    return q * Rh
def Hleft(x4v, prof, k4, delta=1e-5):
    R = rotor_left(x4v, prof, k4); Rr = R.reverse(); Om=[]
    for mu in (3,0,1,2):
        xp=list(x4v); xm=list(x4v); xp[mu]+=delta; xm[mu]-=delta
        dR=(1/(2*delta))*(rotor_left(xp,prof,k4)-rotor_left(xm,prof,k4))
        Om.append(Rr*dR)
    return np.array([[h(Om[a],Om[b]) for b in range(4)] for a in range(4)])
for p in ([0.7,-0.4,1.1], [1.3,0.2,-0.6]):
    HR,_ = Hmat(p+[0.0], prof, "A_I4Qhat", 0.83)
    HL   = Hleft(p+[0.0], prof, 0.83)
    print(f"  p={p}  max|H_right - H_left| = {np.max(np.abs(HR-HL)):.3e}")

# ------------------------------------------------- (6) what makes h_tt nonzero
print("\n=== (6) h_tt = (k4/2)^2 * <u I4 u>_0 : which axes give h_tt != 0 ===")
SD1=(1/math.sqrt(2))*(e(1,2)-e(3,4)); ASD1=(1/math.sqrt(2))*(e(1,2)+e(3,4))
for nm,u in [("e12 (L)",e(1,2)),("e23 (L)",e(2,3)),("e14 (Q)",e(1,4)),("e34 (Q)",e(3,4)),
             ("I4*Qhat(z)=-e12",I4*e(3,4)),("SD1",SD1),("ASD1",ASD1)]:
    print(f"  u={nm:>18}: <u I4 u>_0 = {g0(u*I4*u):+.6f}   -> h_tt = {g0(u*I4*u)/4:+.6f} * k4^2")

# ------------------------------------------------- (7) B=2 / other profiles sanity
print("\n=== (7) higher winding f(0)=2pi (B=2 hedgehog) and f(0)=3pi ===")
for mult,nm in [(2,"2pi*exp(-r)"),(3,"3pi*exp(-r)")]:
    pf = (lambda m: (lambda r: m*math.pi*math.exp(-r)))(mult)
    mtt=mkl=mtk=0.0
    for p in grid_points(9, box=3.0):
        H,_ = Hmat(p+[0.0], pf, "A_I4Qhat", 0.83)
        mtt=max(mtt,abs(H[0,0])); mkl=max(mkl,np.max(np.abs(H[1:,1:]))); mtk=max(mtk,np.max(np.abs(H[0,1:])))
    print(f"  {nm}: max|h_tt|={mtt:.3e} max|h_kl|={mkl:.3e} max|h_tk|={mtk:.3e}")
