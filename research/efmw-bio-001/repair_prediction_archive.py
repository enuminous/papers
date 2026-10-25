"""Recover a truncated output archive using archived fit choices, without retuning.
All re-fitted fold scores must match the already-written benchmark scores.
"""
from pathlib import Path
import tempfile,shutil,os,json,zipfile
import numpy as np
import pandas as pd
from run_benchmark import fit_path_predict,metrics
ROOT=Path(__file__).resolve().parent
d=np.load(ROOT/'data/analysis_data.npz',allow_pickle=False)
score=pd.read_csv(ROOT/'results/fold_metrics.csv')
result=json.loads((ROOT/'results/benchmark.json').read_text())
out={};maxdiff=0
for j,target in enumerate(d['target_names']):
    good=np.isfinite(d['Y'][:,j])&(d['Y'][:,j]>0)
    r=d['replicate'][good];w=d['well'][good];y=np.log10(d['Y'][good,j])
    out[target+'_source_excel_row']=d['source_excel_row'][good]
    out[target+'_replicate']=r;out[target+'_well']=w;out[target+'_observed_log10']=y
    for name in [k[9:] for k in d.files if k.startswith('features_')]:
        x=d['features_'+name][good];p=np.full(len(y),np.nan)
        for held in np.unique(r):
            tr=r!=held;te=~tr
            row=score.query('target==@target and model==@name and held_out_replicate==@held').iloc[0]
            p[te]=fit_path_predict(x[tr],y[tr],r[tr],w[tr],x[te],[float(row.alpha)])[0]
            diff=abs(metrics(y[te],p[te],r[te],w[te])['mse']-row.mse)
            assert diff<1e-12;maxdiff=max(maxdiff,diff)
        out[target+'_'+name]=p
    p=np.empty(len(y))
    for choice in result['results'][target]['comparator_selection']:
        te=r==choice['held_out_replicate'];p[te]=out[target+'_'+choice['model']][te]
    out[target+'_selected_conventional']=p
with tempfile.TemporaryDirectory(prefix='efmw-bio001-archive-') as folder:
    tmp=Path(folder)/'held_out_predictions.npz'
    np.savez_compressed(tmp,**out)
    with zipfile.ZipFile(tmp) as z:
        assert z.testzip() is None and len(z.namelist())==len(out)
    staged=ROOT/'results/held_out_predictions.complete.npz'
    shutil.copyfile(tmp,staged)
    with zipfile.ZipFile(staged) as z:assert z.testzip() is None
    os.replace(staged,ROOT/'results/held_out_predictions.npz')
log={'reason':'Initial output NPZ lacked central directory and final 16 entries; 96 complete entries passed CRC checks.',
     'recovery':'Refit archived alpha choices with unchanged frozen model and data. No new selection or tuning.',
     'refit_metric_max_abs_difference':maxdiff,'complete_arrays':len(out),'archive_crc_verified':True,
     'protocol_or_models_changed':False}
(ROOT/'results/archive_recovery.json').write_text(json.dumps(log,indent=2)+'\n')
print(json.dumps(log,indent=2))
