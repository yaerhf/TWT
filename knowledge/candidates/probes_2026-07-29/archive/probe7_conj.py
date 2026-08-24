"""PROBE 7: third reading -- mass phase as a CONJUGATING (grand-isorotation-type)
rotation R(x,t) = A(t) R_h(x) A(t)^-1, A = exp(u*k4*t/2), u = I4*Qhat(n)."""
import sys, os, math, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import numpy as np
import twt
from twt import e, I4, SCALAR
from texture_h_full16_baryon import PROFILES, Qhat, g0, h, grid_points, rotor_hedgehog

rng = random.Random(99)
def rot_conj(x4v, prof, nhat, k4):
    Rh = rotor_hedgehog(x4v[:3], prof)
    u = I4*Qhat(np.asarray(nhat,dtype=float))
    th = k4*x4v[3]
    A  = math.cos(th/2)*SCALAR + math.sin(th/2)*u
    Ai = math.cos(th/2)*SCALAR - math.sin(th/2)*u
    return A*Rh*Ai
def Hc(x4v, prof, nhat, k4, delta=1e-5):
    R = rot_conj(x4v,prof,nhat,k4); Rr=R.reverse(); Om=[]
    for mu in (3,0,1,2):
        xp=list(x4v); xm=list(x4v); xp[mu]+=delta; xm[mu]-=delta
        Om.append(Rr*((1/(2*delta))*(rot_conj(xp,prof,nhat,k4)-rot_conj(xm,prof,nhat,k4))))
    return np.array([[h(Om[a],Om[b]) for b in range(4)] for a in range(4)])
prof=PROFILES["pi*exp(-r)"]; nz=[0,0,1.0]
M=np.zeros((4,4))
for p in grid_points(9,box=3.0):
    M=np.maximum(M,np.abs(Hc(p+[0.0],prof,nz,0.83)))
print("CONJUGATING reading, max|h_mn| over 9^3 grid:")
print(M)
print("\n h_tt max =",M[0,0]," h_tk max =",np.max(M[0,1:])," h_kl max =",np.max(M[1:,1:]))
# and with a random n / profile / point
tot=surv=0
for _ in range(120):
    pn=list(PROFILES)[rng.randrange(len(PROFILES))]
    p=[rng.uniform(-2.5,2.5) for _ in range(3)]
    if np.linalg.norm(p)<0.2: continue
    n=np.array([rng.gauss(0,1) for _ in range(3)]); n/=np.linalg.norm(n)
    H=Hc(p+[rng.uniform(-2,2)],PROFILES[pn],n,rng.uniform(.2,2.))
    tot+=1
    if np.max(np.abs(H))>1e-6: surv+=1
print(f"\n nonzero h in {surv}/{tot} random trials")
