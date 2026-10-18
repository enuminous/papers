import numpy as np,json
rng=np.random.default_rng(20261018)
N=100000
m=rng.lognormal(mean=0.,sigma=.35,size=N)
unit=rng.normal(size=(N,3));unit/=np.linalg.norm(unit,axis=1)[:,None]
chi=rng.uniform(.05,.85,N)
J=unit*(chi*m*m)[:,None]
M0=float(m.sum()); J0=J.sum(axis=0); E_rad=0.; J_rad=np.zeros(3)
stages=[]; step=0
while len(m)>5:
    n=len(m); perm=rng.permutation(n); nm=n//2; a,b=perm[:2*nm:2],perm[1:2*nm:2]; rem=perm[2*nm:]
    pairmass=m[a]+m[b]
    # stochastic radiation fraction of available rest energy (toy, not binary waveform)
    f=rng.uniform(.005,.025,size=nm)
    mr=pairmass*f; E_rad+=float(mr.sum())
    jpair=J[a]+J[b]
    g=rng.uniform(.03,.15,size=nm)
    jloss=jpair*g[:,None]
    J_rad+=jloss.sum(axis=0)
    m=np.concatenate([pairmass-mr,m[rem]])
    J=np.concatenate([jpair-jloss,J[rem]],axis=0)
    step+=1
    if n>=10000 or n<=100 or step in (5,10,14):
        stages.append({'round':step,'objects':int(len(m)),'mass_remaining':float(m.sum()),'radiated_energy_mass_units':float(E_rad),'net_J_remnant':float(np.linalg.norm(J.sum(axis=0))),'angular_momentum_residual':float(np.linalg.norm(J.sum(axis=0)+J_rad-J0))})
Jpre=J.sum(axis=0); Mpre=float(m.sum())
# hypothetical transformation conserving separate ledgers, not derived from GR or EFMW
rebound_fraction=.65
J_after=rebound_fraction*Jpre; J_boundary=(1-rebound_fraction)*Jpre
mass_after=.98*Mpre; E_boundary=.02*Mpre
result={'seed':20261018,'initial_count':N,'initial_mass':M0,'initial_J_vector':J0.tolist(),'initial_J_norm':float(np.linalg.norm(J0)),'final_remnants':int(len(m)),'final_mass':Mpre,'mass_radiated':E_rad,'mass_conservation_error':float(Mpre+E_rad-M0),'final_J_vector':Jpre.tolist(),'final_J_norm':float(np.linalg.norm(Jpre)),'radiated_J_vector':J_rad.tolist(),'J_conservation_error_norm':float(np.linalg.norm(Jpre+J_rad-J0)),'rebound_assumed_J_inheritance_fraction':rebound_fraction,'post_rebound_J_vector':J_after.tolist(),'boundary_export_J_vector':J_boundary.tolist(),'rebound_J_balance_error':float(np.linalg.norm(J_after+J_boundary-Jpre)),'post_rebound_mass':mass_after,'boundary_energy_export':E_boundary,'post_rebound_mass_balance_error':float(mass_after+E_boundary-Mpre),'stages':stages}
with open('/mnt/data/recursion_run2_results.json','w') as f:json.dump(result,f,indent=2)
print(json.dumps(result,indent=2))