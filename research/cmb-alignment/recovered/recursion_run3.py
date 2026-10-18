"""Universe 003: isotropic-null ensemble and explicit non-blind control.
A statistical audit of a toy merger bookkeeping algorithm, NOT a GR simulation.
"""
import json
import numpy as np
from pathlib import Path

N=100_000
REPS=128
SEED=20261018

def experiment(seed, injected_axis_bias=0.0):
    rng=np.random.default_rng(seed)
    m=rng.lognormal(0,.35,N)
    v=rng.normal(size=(N,3))
    # Optional injected z-axis preference is a positive control, NOT a physical prediction.
    v[:,2]+=injected_axis_bias
    v/=np.linalg.norm(v,axis=1)[:,None]
    chi=rng.uniform(.05,.85,N)
    j=v*(chi*m*m)[:,None]
    m0=float(m.sum()); j0=j.sum(axis=0)
    er=0.; jr=np.zeros(3); count=0
    while len(m)>4:
        n=len(m); p=rng.permutation(n); k=n//2
        a,b=p[:2*k:2],p[1:2*k:2]; rem=p[2*k:]
        pair=m[a]+m[b]
        f=rng.uniform(.005,.025,k)
        loss=pair*f
        er+=float(loss.sum())
        jp=j[a]+j[b]
        g=rng.uniform(.03,.15,k)
        lost_j=jp*g[:,None]
        jr+=lost_j.sum(axis=0)
        m=np.concatenate((pair-loss,m[rem])); j=np.concatenate((jp-lost_j,j[rem])); count+=1
    jf=j.sum(axis=0)
    return {'rounds':count,'final_count':len(m),'mass_fraction':float(m.sum()/m0),
            'initial_J_norm':float(np.linalg.norm(j0)), 'final_J_norm':float(np.linalg.norm(jf)),
            'cos_to_z':float(jf[2]/np.linalg.norm(jf)),
            'mass_relative_error':float(abs(m.sum()+er-m0)/m0),
            'J_relative_error':float(np.linalg.norm(jf+jr-j0)/max(np.linalg.norm(j0),1)),
            'spin_scale':float(np.linalg.norm(jf)/np.sqrt(N))}

null=[experiment(SEED+i) for i in range(REPS)]
# Two fixed positive-control runs assess detection sensitivity, not astrophysical truth.
pos=[experiment(SEED+100000+i,.2) for i in range(32)]
a=np.array([x['cos_to_z'] for x in null]); b=np.array([x['cos_to_z'] for x in pos])
# Preregistered two-sided statistic: abs(cos to z). For isotropic vectors cos(theta) is uniform [-1,1].
# An exact one-draw p-value is p=1-|cos|, NOT a multiple-comparison corrected discovery.
t0=abs(a[0]); rank_p=(1+np.count_nonzero(abs(a[1:])>=t0))/REPS
out={'description':'Toy merging population; no spatial dynamics or GR, and bounce excluded from statistical test',
     'n_per_run':N,'null_realizations':REPS,'positive_controls':32,'seed':SEED,
     'first_null':null[0], 'null_cos_mean':float(a.mean()),'null_abs_cos_mean':float(np.abs(a).mean()),
     'null_signed_cos_sd':float(a.std(ddof=1)), 'null_fraction_cos_positive':float(np.mean(a>0)),
     'null_mass_fraction_mean':float(np.mean([x['mass_fraction'] for x in null])),
     'null_max_relative_mass_error':max(x['mass_relative_error'] for x in null),
     'null_max_relative_J_error':max(x['J_relative_error'] for x in null),
     'first_run_exact_fixed_axis_p':float(1-t0),'first_run_empirical_rank_p':float(rank_p),
     'positive_control_cos_mean':float(b.mean()), 'positive_control_fraction_positive':float(np.mean(b>0)),
     'positive_control_all_cos':b.tolist(),
     'null_all_cos':a.tolist(),
     'interpretation':'Bias control is seeded deliberately. No physically derived axis, data comparison, or 6-sigma claim.'}
Path('/mnt/data/recursion_run3_results.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if not k.endswith('all_cos') and k!='positive_control_all_cos'},indent=2))