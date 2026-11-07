"""Post hoc conventional comparator using only the signed and squared memories."""
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from analyze import HASHES, basis, get_features, summarize

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("directory",type=Path)
    parser.add_argument("output",type=Path)
    args=parser.parse_args()
    sessions={k:get_features(args.directory/(k+".csv"),k) for k in HASHES}
    ids=sorted(sessions['t1'].id.unique(),key=lambda i:hashlib.sha256(f"EFMW:{i}".encode()).digest())
    folds={who:i%5 for i,who in enumerate(ids)}
    for df in sessions.values():
        df["conventional"]=df.abs_m/df.rms
    outputs={}
    for fold in range(5):
        tr=sessions["t1"][sessions["t1"].id.map(folds)!=fold]
        for visit,frame in sessions.items():
            te=frame[frame.id.map(folds)==fold]
            x,y=basis(tr,te)
            scale=lambda s:(tr[s].mean(),tr[s].std(ddof=0))
            def augment(x,y,s):
                mu,sd=scale(s)
                return np.column_stack([x,(tr[s]-mu)/sd]),np.column_stack([y,(te[s]-mu)/sd])
            x,y=augment(x,y,"conventional")
            for comparison in ["moments", "moments_and_rating_cues"]:
                if comparison=="moments_and_rating_cues":
                    # Both the slider start and the participant's current placement
                    # are observable by the time they rate confidence.
                    tr=tr.assign(move_size=tr.adjustment.abs())
                    te=te.assign(move_size=te.adjustment.abs())
                    x,y=augment(x,y,"slider")
                    x,y=augment(x,y,"move_size")
                loss=pd.DataFrame({"id":te.id.to_numpy()})
                for term in ["base","B","R"]:
                    a,b=(x,y) if term=="base" else augment(x,y,term)
                    model=Ridge(alpha=1.).fit(a,tr.confidence)
                    loss[term]=(te.confidence.to_numpy()-model.predict(b))**2
                outputs.setdefault(visit+"_"+comparison,[]).append(loss)
    args.output.write_text(json.dumps({k:summarize(pd.concat(v)) for k,v in outputs.items()},indent=2)+'\n')
if __name__=="__main__":
    main()
