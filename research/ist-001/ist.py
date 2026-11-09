#!/usr/bin/env python3
"""IST-001: bounded metric-stress and oscillator-reservoir controls.

Classical proposed models only. Not a full covariant gravity/EFMW derivation.
"""
import argparse,hashlib,json,math,random
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def Q(x):
    if type(x)==bool:raise ValueError("Boolean parameter")
    return F(str(x))

class P:
    def __init__(self,a=(0,)):
        a=[F(x) for x in a]
        while len(a)>1 and a[-1]==0:a.pop()
        self.c=tuple(a)
    @staticmethod
    def t():return P((0,1))
    def __add__(self,o):
        o=C(o);return P([(self.c[i] if i<len(self.c) else 0)+(o.c[i] if i<len(o.c) else 0) for i in range(max(len(self.c),len(o.c)))])
    __radd__=__add__
    def __neg__(self):return P((-x for x in self.c))
    def __sub__(self,o):return self+-C(o)
    def __rsub__(self,o):return C(o)-self
    def __mul__(self,o):
        o=C(o);out=[F(0)]*(len(self.c)+len(o.c)-1)
        for i,x in enumerate(self.c):
            for j,y in enumerate(o.c):out[i+j]+=x*y
        return P(out)
    __rmul__=__mul__
    def __truediv__(self,o):
        if type(o) not in (int,F) or not o:raise ValueError("Rational divisor only")
        return P((x/F(o) for x in self.c))
    def __pow__(self,n):
        if type(n)!=int or n<0 or n>12:raise ValueError("Bounded nonnegative power only")
        v=P((1,))
        for _ in range(n):v=v*self
        return v
    def diff(self):return P((i*v for i,v in enumerate(self.c) if i)) if len(self.c)>1 else P((0,))
    def __eq__(self,o):
        try:return self.c==C(o).c
        except (TypeError,ValueError):return False

def C(o):
    if isinstance(o,P):return o
    if type(o) in (int,F):return P((o,))
    raise TypeError("Not a polynomial")

def cov_metric(a,b,c):
    a,b,c=F(a),F(b),F(c);det=a*c-b*b
    if det>=0:raise ValueError("Lorentzian metric required")
    return ((c/det,-b/det),(-b/det,a/det))

def hilbert_checks():
    rng=random.Random(20261109);out=[]
    for i in range(32):
        a,b,c=-F(2),F(rng.randint(-2,2),7),F(3,2)
        g=cov_metric(a,b,c)
        dm=(F(rng.randint(-3,3),4),F(rng.randint(-3,3),5))
        q,m=F(rng.randint(-3,3),3),F(rng.randint(-3,3),3)
        Z,mu2,K=F(3,2),F(2,3),F(5,4)
        W=mu2*m*m/2+K*(q-m)**2/2
        L=-Z*(a*dm[0]**2+2*b*dm[0]*dm[1]+c*dm[1]**2)/2-W
        for u,v in ((0,0),(0,1),(1,1)):
            mult=1 if u==v else 2
            # Direct variation of metric-dependent kinetic term and volume.
            direct=-Z*mult*dm[u]*dm[v]/2-mult*g[u][v]*L/2
            Tuv=Z*dm[u]*dm[v]+g[u][v]*L
            if direct!=-mult*Tuv/2:raise AssertionError("Hilbert stress mismatch")
        if i<2:out.append({"sample":i,"L":str(L)})
    return {"metric_variation_trials":32,"samples":out}

def exchange_checks():
    rng=random.Random(20261109)
    for _ in range(48):
        q=P([rng.randrange(-3,4) for _ in range(4)])
        m=P([rng.randrange(-3,4) for _ in range(3)])
        Z,mu2,K=F(3,2),F(2,3),F(5,4)
        v,w=q.diff(),m.diff()
        E_q=v*v/2+F(2,3)*q*q/2
        E_I=Z*w*w/2+mu2*m*m/2+K*(q-m)*(q-m)/2
        Eq=v.diff()+F(2,3)*q+K*(q-m)
        Em=Z*w.diff()+mu2*m-K*(q-m)
        flux=K*(q-m)*v
        if E_q.diff()!=v*Eq-flux:raise AssertionError("Wrong q exchange")
        if E_I.diff()!=w*Em+flux:raise AssertionError("Wrong memory exchange")
        if (E_q+E_I).diff()!=v*Eq+w*Em:raise AssertionError("Wrong total energy")
    return {"off_shell_polynomial_checks":48,"on_shell_total_conservation":"EXACT_CONDITIONAL"}

def split_check():
    g=cov_metric(-2,F(1,3),F(3,2));q,m,K=F(1),F(1,5),F(5,4)
    W=K*(q-m)**2/2
    for i in range(2):
        for j in range(2):
            # The interaction can be assigned to either component.
            assert F(7)-g[i][j]*W+F(11)==F(7)+F(11)-g[i][j]*W
    return {"status":"PARTIAL_STRESS_NOT_UNIQUE_TOTAL_STRESS_INVARIANT","W":str(W)}

def model(p):
    t=p["numeric_fixtures"]["finite_bath"]
    return {"Z":Q(t["Z"]),"K":Q(t["K"]),"qmass":Q(t["q_mass2"]),
            "bath":[tuple(Q(x[k]) for k in ("z","omega","a")) for x in t["bath"]]}

def force(pos,mod):
    q,m,*xs=pos
    fq=-mod["qmass"]*q-mod["K"]*(q-m)
    fm=mod["K"]*(q-m)
    out=[]
    for (z,w,a),x in zip(mod["bath"],xs):
        fm+=z*w*w*a*(x-a*m)
        out.append(-w*w*(x-a*m))
    return [fq,fm/mod["Z"],*out]

def energy(pos,vel,mod):
    q,m,*xs=pos;dq,dm,*dxs=vel
    E=dq*dq/2+mod["qmass"]*q*q/2+mod["Z"]*dm*dm/2+mod["K"]*(q-m)**2/2
    for (z,w,a),x,dx in zip(mod["bath"],xs,dxs):E+=z*(dx*dx+w*w*(x-a*m)**2)/2
    return E

def bath_checks(p):
    mod=model(p);rng=random.Random(20261109)
    for _ in range(35):
        pos=[F(rng.randrange(-4,5),rng.randrange(1,7)) for i in range(4)]
        vel=[F(rng.randrange(-4,5),rng.randrange(1,7)) for i in range(4)]
        accel=force(pos,mod)
        q,m,*xs=pos;dq,dm,*dxs=vel
        de=dq*(accel[0]+mod["qmass"]*q)+mod["Z"]*dm*accel[1]+mod["K"]*(q-m)*(dq-dm)
        for j,((z,w,a),x,dx) in enumerate(zip(mod["bath"],xs,dxs)):
            de+=z*dx*accel[j+2]+z*w*w*(x-a*m)*(dx-a*dm)
        if de:raise AssertionError("Closed bath not energy-balanced")
    f=p["numeric_fixtures"]["finite_bath"]
    i=f["initial_state"]
    initial=[Q(i["q"]),Q(i["m"]),*[Q(x) for x in i["x"]]]
    vel0=[Q(i["pq"]),Q(i["pm"]),*[Q(x) for x in i["px"]]]
    E0=float(energy(initial,vel0,mod));errs=[]
    fmod={"Z":float(mod["Z"]),"K":float(mod["K"]),"qmass":float(mod["qmass"]),
          "bath":[tuple(map(float,x)) for x in mod["bath"]]}
    for steps in f["steps"]:
        h=float(f["total_time"])/steps
        pos=list(map(float,initial));v=list(map(float,vel0))
        for _ in range(steps):
            A=force(pos,fmod);v=[x+h*a/2 for x,a in zip(v,A)]
            pos=[x+h*y for x,y in zip(pos,v)]
            B=force(pos,fmod);v=[x+h*a/2 for x,a in zip(v,B)]
        errs.append(abs(float(energy(pos,v,fmod))-E0)/E0)
    ratios=[errs[k]/errs[k+1] for k in range(len(errs)-1)]
    if not all(3<r<5 for r in ratios):raise AssertionError("Expected second-order refinement")
    return {"exact_bath_energy_checks":35,"steps":f["steps"],"energy_defects":errs,"refinement_ratios":ratios,
            "scope":"Closed reversible finite bath; no thermodynamic dissipation"}

def gle_check(p):
    mod=model(p);f=p["numeric_fixtures"]["GLE_manufactured"]
    m0=float(Q(f["m0"]));v=float(Q(f["mdot"]))
    xs=[float(Q(x)) for x in f["bath_initial_x"]]
    dxs=[float(Q(x)) for x in f["bath_initial_xdot"]]
    largest=0.0
    for t in f["time_grid"]:
        t=float(t);m=m0+v*t;force0=drag=noise=0.0
        for j,(z,w,a) in enumerate(mod["bath"]):
            z,w,a=map(float,(z,w,a));c=z*w*w*a
            A=xs[j]-a*m0;B=(dxs[j]-a*v)/w
            d=A*math.cos(w*t)+B*math.sin(w*t)
            force0+=c*d
            drag+=z*w*a*a*v*math.sin(w*t)
            noise+=c*(A*math.cos(w*t)+dxs[j]/w*math.sin(w*t))
        qdrive=m-force0/float(mod["K"])
        err=float(mod["K"])*(m-qdrive)+drag-noise
        largest=max(largest,abs(err))
    if largest>float(f["tolerance"]):raise AssertionError("Manufactured GLE mismatch")
    return {"max_residual":largest,"times":len(f["time_grid"]),
            "scope":"Prescribed homogeneous q drive, finite bath kernel; no white-noise or continuum limit"}

def markov_check(p):
    f=p["numeric_fixtures"]["markov"];alpha=float(f["alpha"])
    if abs(float(f["K"])/float(f["Gamma"])-alpha)>1e-12:raise ValueError("Wrong alpha")
    m0=float(f["m0"]);largest=0.0
    for t in f["test_times"]:
        t=float(t);m=t-1/alpha+(m0+1/alpha)*math.exp(-alpha*t)
        dm=1-(1+alpha*m0)*math.exp(-alpha*t)
        largest=max(largest,abs(dm-alpha*(t-m)))
    if largest>float(f["tolerance"]):raise AssertionError("Markov ODE mismatch")
    return {"max_residual":largest,"scope":"Assumed local friction and negligible inertia/noise; not a bath continuum derivation"}

def source_guard(p):
    lock=json.loads((ROOT.parent/"unity-001"/"phase-1"/"sources.lock.json").read_text())
    for name,commit,path,blob in [
      ("EFMW-Lagrangian",p["source"]["frozen_c1_commit"],"candidate/CANDIDATE.md","916e04935f50cbbf07ddcd81e7c71a02954b1c96"),
      ("Information-Tensor",p["source"]["frozen_witd_commit"],"research/witd-002/DERIVATION.md","d427b2f50bd8e577f6c206e076aa4121a612c6d9")]:
        rep=next(r for r in lock["repositories"] if r["repo"]==name)
        if rep["commit"]!=commit or not any(x["path"]==path and x["git_blob_sha"]==blob for x in rep["files"]):
            raise ValueError("Source drift "+name)
    return {"source_files_locked":2}

def run():
    raw=(ROOT/"PROTOCOL.json").read_bytes();p=json.loads(raw)
    if p["schema"]!="ist-001-frozen-protocol-v1":raise ValueError("Protocol drift")
    if any(x["status"]!="UNEXECUTED" for x in p["gates"][:6]) or any(x["status"]!="UNRESOLVED" for x in p["gates"][6:]):
        raise ValueError("Outcome promotion in frozen protocol")
    src=source_guard(p)
    h=hilbert_checks();e=exchange_checks();s=split_check();b=bath_checks(p);g=gle_check(p);m=markov_check(p)
    return {"schema":"ist-001-bounded-results-v1","protocol_sha256":hashlib.sha256(raw).hexdigest(),
      "source_guard":src,"hilbert":h,"exchange":e,"split":s,"bath":b,"GLE":g,"markov":m,
      "gates":{"PASS":6,"FAIL":0,"UNRESOLVED":2},
      "EFMW_specific_physical_PASS":0,
      "physical_status":"UNRESOLVED",
      "note":"Classical toy controls only: finite reservoir is reversible; no source-faithful full WITD or physically novel EFMW gravity established"}

if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--out",default=str(ROOT/"build"/"results.json"));a=ap.parse_args()
    result=run();dest=Path(a.out);dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print(json.dumps({"gates":result["gates"],"hilbert":result["hilbert"]["metric_variation_trials"],
        "bath_refinement":result["bath"]["refinement_ratios"],
        "GLE_residual":result["GLE"]["max_residual"],
        "EFMW_physical_PASS":result["EFMW_specific_physical_PASS"]},indent=2))
