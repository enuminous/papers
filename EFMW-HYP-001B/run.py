import numpy as np
from scipy.stats import t, binomtest
import json
N=400; REPS=2000
# Fresh seed; oracle whitening and estimated AR(1) sensitivity.
def run(seed=2026112501):
 rng=np.random.default_rng(seed); out=[]
 for rho in [.3,.65,.85]:
  for k in [0.,.35]:
   stats={m:[] for m in ['oracle_gls','feasible_gls']}
   for j in range(REPS):
    tt=np.arange(N); c=np.clip(.52+.25*np.sin(2*np.pi*tt/79)+rng.normal(0,.13,N),.02,.98)
    m=np.empty(N);m[0]=.5
    for i in range(1,N):m[i]=m[i-1]+(c[i]-m[i-1])/18
    x=c*m;drift=np.cumsum(rng.normal(0,.012,N))+.0015*tt;cross=.65*c+.3*np.roll(c,2)+rng.normal(0,.12,N)
    thermal=np.zeros(N);noise=np.empty(N);noise[0]=rng.normal(0,.12);innov=rng.normal(0,.12,N)
    for i in range(1,N):thermal[i]=thermal[i-1]+(cross[i]-thermal[i-1])/26;noise[i]=rho*noise[i-1]+innov[i]
    X=np.column_stack([np.ones(N),x,drift,cross,thermal,tt]);y=k*x+.7*drift+.45*cross+.65*thermal+noise
    e=y-X@np.linalg.lstsq(X,y,rcond=None)[0];rh=np.clip(e[1:]@e[:-1]/(e[:-1]@e[:-1]),-.98,.98)
    for method,r in [('oracle_gls',rho),('feasible_gls',rh)]:
     xx=X[1:]-r*X[:-1];yy=y[1:]-r*y[:-1];b=np.linalg.lstsq(xx,yy,rcond=None)[0];res=yy-xx@b;df=len(yy)-X.shape[1];se=np.sqrt((res@res/df)*np.linalg.inv(xx.T@xx)[1,1]);w=t.ppf(.975,df)*se;lo,hi=b[1]-w,b[1]+w
     stats[method].append((not lo<=0<=hi,lo<=k<=hi,b[1],2*w))
   for method,arr in stats.items():
    a=np.array(arr);n=int(a[:,0].sum());ci=binomtest(n,REPS).proportion_ci();out.append(dict(rho=rho,kappa=k,method=method,n=REPS,exclusions=n,rate=n/REPS,rate_ci=[ci.low,ci.high],coverage=float(a[:,1].mean()),mean=float(a[:,2].mean()),width=float(np.median(a[:,3]))))
 return out
if __name__=='__main__':
 out=run();print(json.dumps(out,indent=2));open('summary.json','w').write(json.dumps(out,indent=2))
