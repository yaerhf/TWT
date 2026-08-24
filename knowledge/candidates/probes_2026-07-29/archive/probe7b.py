import sys, os, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "corpus"))
import numpy as np, twt
from twt import e, I4, SCALAR
from texture_h_full16_baryon import PROFILES, Qhat, g0, h, rotor_hedgehog
from probe7_conj import rot_conj
prof=PROFILES["pi*exp(-r)"]; n=[0.3,-0.5,0.81]; n=list(np.array(n)/np.linalg.norm(n))
p=[0.7,-0.4,1.1]; k4=0.83; d=1e-5
for x4 in (0.0,0.6):
    v=p+[x4]; R=rot_conj(v,prof,n,k4); Rr=R.reverse()
    for mu,lab in [(3,'t'),(0,'1')]:
        xp=list(v);xm=list(v);xp[mu]+=d;xm[mu]-=d
        Om=Rr*((1/(2*d))*(rot_conj(xp,prof,n,k4)-rot_conj(xm,prof,n,k4)))
        print(f" x4={x4}  Omega_{lab} =", Om)
    Om_t=Rr*((1/(2*d))*(rot_conj([p[0],p[1],p[2],x4+d],prof,n,k4)-rot_conj([p[0],p[1],p[2],x4-d],prof,n,k4)))
    print("   <Om_t I4 Om_t>_0 =", g0(Om_t*I4*Om_t))
    # SD/ASD balance of Om_t
    SD=[(1/math.sqrt(2))*(e(1,2)-e(3,4)),(1/math.sqrt(2))*(e(1,3)+e(2,4)),(1/math.sqrt(2))*(e(1,4)-e(2,3))]
    AS=[(1/math.sqrt(2))*(e(1,2)+e(3,4)),(1/math.sqrt(2))*(e(1,3)-e(2,4)),(1/math.sqrt(2))*(e(1,4)+e(2,3))]
    nsd=sum(g0(Om_t*b.reverse())**2 for b in SD); nas=sum(g0(Om_t*b.reverse())**2 for b in AS)
    print(f"   |SD|^2={nsd:.6f}  |ASD|^2={nas:.6f}  (h_tt ∝ difference)")
