# ONE-FIELD probe, part 2: the moduli-space L^2 metric cross-block  (the tensor product)
# and the two-maximum -> one-maximum individuation bifurcation, done properly.
import sys, math, itertools
sys.path.insert(0, r"C:\Users\hfyae\Claude\Projects\Deepseek\knowledge\corpus")
import numpy as np
from scipy.integrate import solve_ivp

# ---------- banked B=1 profile (R-135's BVP, same shooting) ----------
def make_rhs(Bc, Ic):
    def f_rhs(t, y):
        F, Fp = y
        s2 = math.sin(2*F); sF = math.sin(F)
        num = -(t/2)*Fp - Bc*s2*Fp**2 + Bc*s2/4 + Ic*sF**2*s2/t**2
        den = t**2/4 + 2*Bc*sF**2
        return [Fp, num/den]
    return f_rhs
def solve_profile(Bc, Ic, a_lo, a_hi, xmax=40.0):
    p = (-1+math.sqrt(1+8*Bc))/2; s_dec = (1+math.sqrt(1+8*Bc))/2
    rhs = make_rhs(Bc, Ic); x0 = 1e-3
    def integrate(a):
        return solve_ivp(rhs,(x0,xmax),[math.pi-a*x0**p, -a*p*x0**(p-1)],
                         rtol=1e-11, atol=1e-13, dense_output=True, max_step=0.1)
    w1,w2 = 10.0,16.0
    def flatness(a):
        s = integrate(a)
        if np.any(s.y[0] < -1e-12): return -1e9
        return w2**s_dec*s.sol(w2)[0] - w1**s_dec*s.sol(w1)[0]
    flo = flatness(a_lo); assert flo*flatness(a_hi) < 0
    lo,hi = a_lo,a_hi
    for _ in range(52):
        mid=.5*(lo+hi)
        if flatness(mid)*flo>0: lo=mid
        else: hi=mid
    a=.5*(lo+hi); return integrate(a), a
sol1, a1 = solve_profile(1.0, 1.0, 0.9, 1.2)
XS = np.linspace(1e-6, 40.0, 400001)
FF = sol1.sol(XS)[0]
C_tail = float(np.mean(XS[(XS>10)&(XS<16)]**2 * FF[(XS>10)&(XS<16)]))
print(f"a* = {a1:.10f}   tail C (F ~ C/x^2) = {C_tail:.6f}   (R-135 banked 8.6344)")

def Fint(r):
    return np.interp(r, XS, FF, left=math.pi, right=0.0) + np.where(r>40.0, C_tail/np.maximum(r,1e-9)**2, 0.0)*0.0

def rot(axis, ang):
    axis = np.asarray(axis,dtype=float); axis/=np.linalg.norm(axis)
    K = np.array([[0,-axis[2],axis[1]],[axis[2],0,-axis[0]],[-axis[1],axis[0],0]])
    return np.eye(3)+math.sin(ang)*K+(1-math.cos(ang))*K@K
def qmul(a,b):
    w1,x1,y1,z1=a[...,0],a[...,1],a[...,2],a[...,3]
    w2,x2,y2,z2=b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([w1*w2-x1*x2-y1*y2-z1*z2, w1*x2+x1*w2+y1*z2-z1*y2,
                     w1*y2-x1*z2+y1*w2+z1*x2, w1*z2+x1*y2-y1*x2+z1*w2],axis=-1)

def sigma_pair(Xg, c1, c2, A):
    d1 = Xg - c1; r1 = np.sqrt((d1*d1).sum(-1)); f1 = Fint(r1)
    n1 = d1/np.maximum(r1,1e-12)[...,None]
    q1 = np.concatenate([np.cos(f1)[...,None], np.sin(f1)[...,None]*n1], -1)
    d2 = Xg - c2; r2 = np.sqrt((d2*d2).sum(-1)); f2 = Fint(r2)
    n2 = d2/np.maximum(r2,1e-12)[...,None]
    q2 = np.concatenate([np.cos(f2)[...,None], np.sin(f2)[...,None]*(n2@A.T)], -1)
    return qmul(q1,q2)

# ---------- G. the L^2 (sigma-model) moduli metric: cross-block vs separation ----------
print("\n"+"="*78)
print("G. Moduli-space L^2 metric: does the TRANSLATIONAL block factorise?")
print("   g_ab = Int d^3x  d_a sigma . d_b sigma ;  a,b in {c1_i, c2_j}")
print("="*78)
A_att = rot([1,0,0], math.pi)      # maximally attractive channel (R-139: pi-rot _|_ R)
L, N = 16.0, 129
g = np.linspace(-L, L, N).astype(np.float64); h = g[1]-g[0]
Xg = np.stack(np.meshgrid(g,g,g,indexing='ij'),-1)
delta = 0.02
print(f"   grid {N}^3 on [-{L},{L}]^3, h={h:.4f}, FD delta={delta}")
print(f"   {'d':>6} {'|g11|_F':>10} {'|g22|_F':>10} {'|g12|_F':>10} {'ratio':>10} {'d^3*ratio':>10}")
rows=[]
for d in [4.0,5.0,6.0,7.0,8.0,10.0,12.0]:
    c1 = np.array([0,0,+d/2.]); c2 = np.array([0,0,-d/2.])
    D1=[];D2=[]
    for i in range(3):
        ei = np.zeros(3); ei[i]=1.0
        D1.append(((sigma_pair(Xg,c1+delta*ei,c2,A_att)-sigma_pair(Xg,c1-delta*ei,c2,A_att))/(2*delta)).astype(np.float32))
        D2.append(((sigma_pair(Xg,c1,c2+delta*ei,A_att)-sigma_pair(Xg,c1,c2-delta*ei,A_att))/(2*delta)).astype(np.float32))
    def ip(u,v): return float(np.einsum('ijkl,ijkl->',u,v))*h**3
    g11 = np.array([[ip(D1[i],D1[j]) for j in range(3)] for i in range(3)])
    g22 = np.array([[ip(D2[i],D2[j]) for j in range(3)] for i in range(3)])
    g12 = np.array([[ip(D1[i],D2[j]) for j in range(3)] for i in range(3)])
    n11,n22,n12 = np.linalg.norm(g11),np.linalg.norm(g22),np.linalg.norm(g12)
    ratio = n12/math.sqrt(n11*n22)
    rows.append((d,ratio))
    print(f"   {d:6.2f} {n11:10.3f} {n22:10.3f} {n12:10.5f} {ratio:10.6f} {d**3*ratio:10.4f}")
    del D1,D2
ds = np.array([r[0] for r in rows]); rs = np.array([r[1] for r in rows])
sel = ds>=6.0
p = np.polyfit(np.log(ds[sel]), np.log(rs[sel]), 1)
print(f"   power-law fit on d>=6:  |g12|/sqrt(|g11||g22|) ~ d^({p[0]:.3f})")

# ---------- D'. individuation: local maxima of the baryon density, fine 2D slab ----------
print("\n"+"="*78)
print("D'. Individuation: number of local maxima of the baryon density b(x)")
print("    [MODEL: product ansatz -- valid at large d; indicative only at small d]")
print("="*78)
def bary_slab(c1,c2,A,Lxz=7.0,Nxz=281,hy=0.02):
    gx = np.linspace(-Lxz,Lxz,Nxz); gz = np.linspace(-Lxz,Lxz,Nxz)
    hx = gx[1]-gx[0]
    X,Z = np.meshgrid(gx,gz,indexing='ij')
    def sig_at(dx,dy,dz):
        P = np.stack([X+dx, np.full_like(X,dy), Z+dz],-1)
        return sigma_pair(P,c1,c2,A)
    s0 = sig_at(0,0,0)
    d1 = (sig_at(hx,0,0)-sig_at(-hx,0,0))/(2*hx)
    d2 = (sig_at(0,hy,0)-sig_at(0,-hy,0))/(2*hy)
    d3 = (sig_at(0,0,hx)-sig_at(0,0,-hx))/(2*hx)
    M = np.stack([s0,d1,d2,d3],-2)
    return gx,gz,np.linalg.det(M)/(2*math.pi**2)

print(f"   {'d':>6} {'#max on axis':>13} {'z of maxima':>28}")
for d in [6.0,5.0,4.0,3.5,3.0,2.5,2.0,1.5,1.2,1.0,0.8,0.5]:
    c1=np.array([0,0,+d/2.]); c2=np.array([0,0,-d/2.])
    gx,gz,b = bary_slab(c1,c2,A_att)
    ax = np.abs(b[len(gx)//2,:])          # |b| along the separation axis x=y=0
    loc = [i for i in range(1,len(ax)-1) if ax[i]>ax[i-1] and ax[i]>=ax[i+1] and ax[i]>0.02*ax.max()]
    print(f"   {d:6.2f} {len(loc):13d}   {np.round(gz[loc],3)}")
