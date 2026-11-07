"""Replay from two checksum-verified Loosen et al. public CSVs. No raw data published."""
import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.signal import lfilter
from sklearn.linear_model import Ridge

HASHES = {"t1": "caacb0c111100ee8b24dbefe265f6bb7992e5599ab0b7ffce6abb227726dc2a9",
          "t2": "fc5ce566ba808850b7706095075139a360a2ca1ae79a83308a9fda0064535a06"}
COLS = ["id", "nTrial", "nBlock", "buckPos", "refLoc", "conf", "hitMiss",
        "behav_d", "bayes_CPP", "bayes_RU", "confOri"]
CONT = ["prev_conf", "conf_history", "prev_err", "older_err", "prev_abs", "older_abs",
        "m", "abs_m", "rms", "cpp", "ru", "age"]
BINARY = ["prev_hit"]
def circular(deg):
    return (deg + 180) % 360 - 180

def get_features(path, key):
    assert hashlib.sha256(path.read_bytes()).hexdigest() == HASHES[key]
    data = pd.read_csv(path, usecols=COLS).sort_values(["id", "nTrial"])
    assert not data.duplicated(["id", "nTrial"]).any()
    assert data[COLS].notna().all().all()
    # At antipodal ties either sign convention is possible; retain the authors' sign.
    delta = circular(data.refLoc - data.buckPos)
    assert np.max(np.abs(circular(delta - np.rad2deg(data.behav_d)))) < 1e-6
    blocks = []
    for (who, block), g in data.groupby(["id", "nBlock"], sort=False):
        assert np.all(np.diff(g.nTrial)==1)
        err = g.behav_d.to_numpy()
        def history(values):
            return np.r_[0., lfilter([.5], [1., -.5], values)[:-1]]
        m, b, q = history(err), history(abs(err)), history(err**2)
        ratio = np.divide(abs(m), b, out=np.zeros_like(b), where=b>0)
        idx = np.arange(len(g))
        ratings = g.conf.to_numpy()
        z = pd.DataFrame(dict(id=who, block=block, trial=g.nTrial.values,
            confidence=ratings, slider=g.confOri.values, adjustment=circular(g.buckPos.diff()),
            prev_conf=g.conf.shift(), conf_history=np.r_[0,ratings.cumsum()[:-1]]/np.maximum(idx,1),
            prev_err=g.behav_d.shift(), older_err=g.behav_d.shift(2),
            prev_abs=g.behav_d.shift().abs(), older_abs=g.behav_d.shift(2).abs(),
            m=m, abs_m=abs(m), rms=np.sqrt(q), B=b, R=ratio,
            cpp=g.bayes_CPP.shift(), ru=g.bayes_RU.shift(), prev_hit=g.hitMiss.shift(),
            age=idx), index=g.index)
        z=z.iloc[5:]
        assert z.notna().all().all() and (z.B>0).all()
        blocks.append(z)
    return pd.concat(blocks, ignore_index=True)

def basis(train, test):
    # Linear splines with training-fold quartile knots allow nonlinear control effects.
    # Standardize on training rows only and regularize with the same fixed penalty.
    cols=[]
    for name in CONT:
        x=train[name].to_numpy(); y=test[name].to_numpy()
        cols.append((x,y))
        for knot in np.unique(np.quantile(x,[.25,.5,.75])):
            cols.append((np.maximum(x-knot,0),np.maximum(y-knot,0)))
    for name in BINARY:
        cols.append((train[name].to_numpy(),test[name].to_numpy()))
    a,b = (np.column_stack(v) for v in zip(*cols))
    mu=a.mean(axis=0); sd=a.std(axis=0); sd[sd<1e-9]=1.
    return (a-mu)/sd,(b-mu)/sd

def summarize(loss):
    scores=loss.groupby("id").mean(numeric_only=True)
    base=scores.base.to_numpy()
    rng=np.random.default_rng(20261106)
    idx=rng.integers(len(base),size=(5000,len(base)))
    out={"participants":len(base),"trials":len(loss),"base_mse":float(base.mean())}
    for name in ["B","R"]:
        gain=base-scores[name].to_numpy()
        out[name]={"mse_gain":float(gain.mean()),"percent_mse_gain":float(100*gain.mean()/base.mean()),
                   "gain_ci":np.quantile(gain[idx].mean(axis=1),[.025,.975]).tolist()}
    return out

def main():
    p=argparse.ArgumentParser()
    p.add_argument("directory",type=Path,help="directory containing t1.csv and t2.csv")
    p.add_argument("output",type=Path)
    args=p.parse_args()
    sessions={k:get_features(args.directory/(k+".csv"),k) for k in HASHES}
    ids=sorted(sessions['t1'].id.unique(),key=lambda i:hashlib.sha256(f"EFMW:{i}".encode()).digest())
    assert set(sessions['t2'].id)<=set(ids)
    folds={who:k%5 for k,who in enumerate(ids)}
    outputs={}; slopes={}
    for fold in range(5):
        train=sessions['t1'][sessions['t1'].id.map(folds)!=fold]
        for visit,frame in sessions.items():
            test=frame.loc[frame.id.map(folds)==fold].copy()
            assert set(train.id).isdisjoint(test.id)
            x,y=basis(train,test)
            for target in ["confidence","adjustment"]:
                loss=pd.DataFrame({"id":test.id.to_numpy()})
                for term in ["base","B","R"]:
                    X,Y=x,y
                    if term!="base":
                        mu,sd=train[term].mean(),train[term].std(ddof=0)
                        X=np.column_stack((x,(train[term]-mu)/sd))
                        Y=np.column_stack((y,(test[term]-mu)/sd))
                    model=Ridge(alpha=1.).fit(X,train[target])
                    loss[term]=(test[target].to_numpy()-model.predict(Y))**2
                    if visit=="t1" and term!="base":
                        slopes.setdefault(target+"_"+term,[]).append(float(model.coef_[-1]/sd))
                outputs.setdefault(visit+"_"+target,[]).append(loss)
    reports={k:summarize(pd.concat(v)) for k,v in outputs.items()}
    args.output.write_text(json.dumps({"results":reports,"raw_unit_fold_slopes":slopes},indent=2)+'\n')

if __name__=="__main__":
    main()
