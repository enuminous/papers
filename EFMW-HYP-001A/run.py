import numpy as np, pandas as pd
from scipy.stats import norm
import statsmodels.api as sm
SEED=20261113; rng=np.random.default_rng(SEED)
N=400; REPS=1000; KTRUE=0.35
# Measurement units are arbitrary standardized force units. The H2 regressor is C*M.
def trial(kappa):
 t=np.arange(N); c=np.clip(0.52+0.25*np.sin(2*np.pi*t/79)+rng.normal(0,.13,N),.02,.98)
 m=np.empty(N); m[0]=.5
 for i in range(1,N):m[i]=m[i-1]+(c[i]-m[i-1])/18
 x=c*m
 # nuisance signals share common slow component with coherence
 drift=np.cumsum(rng.normal(0,.012,N)); drift+=.0015*t
 cross=.65*c+.3*np.roll(c,2)+rng.normal(0,.12,N)
 thermal=np.empty(N);thermal[0]=0
 for i in range(1,N):thermal[i]=thermal[i-1]+(cross[i]-thermal[i-1])/26
 noise=np.empty(N);noise[0]=rng.normal(0,.12)
 for i in range(1,N):noise[i]=.65*noise[i-1]+rng.normal(0,.12)
 y=kappa*x+.7*drift+.45*cross+.65*thermal+noise
 # intentionally misspecified H2-only fit, iid confidence interval
 naive=sm.OLS(y,sm.add_constant(x)).fit()
 # better-specified model: independently measured nuisance proxies, time, and HAC covariance
 X=sm.add_constant(np.column_stack([x,drift,cross,thermal,t]))
 adj=sm.OLS(y,X).fit(cov_type='HAC',cov_kwds={'maxlags':20})
 return [(fit.params[1],fit.bse[1],fit.conf_int()[1,0],fit.conf_int()[1,1]) for fit in (naive,adj)]
rows=[]
for k,label in [(0.,'null'),(KTRUE,'injected')]:
 for i in range(REPS):
  z=trial(k)
  for method,vals in zip(['naive_iid','nuisance_HAC'],z):
   est,se,lo,hi=vals
   rows.append((label,i,method,k,est,se,lo,hi,not(lo<=0<=hi),lo<=k<=hi,hi-lo))
df=pd.DataFrame(rows,columns=['condition','replicate','method','true_kappa','estimate','se','ci_low','ci_high','excludes_zero','covers_truth','ci_width'])
df.to_csv('replicates.csv',index=False)
summary=df.groupby(['condition','method']).agg(replicates=('estimate','size'),mean_estimate=('estimate','mean'),median_estimate=('estimate','median'),sd_estimate=('estimate','std'),zero_exclusion_rate=('excludes_zero','mean'),truth_coverage=('covers_truth','mean'),median_ci_width=('ci_width','median'),mean_ci_width=('ci_width','mean'),p95_ci_width=('ci_width',lambda v:np.quantile(v,.95))).reset_index()
summary.to_csv('summary.csv',index=False)
print(summary.to_string(index=False,float_format=lambda x:f'{x:.4f}'))
