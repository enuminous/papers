"""Execute the frozen EFMW-BIO-001 protocol. No hyperparameters depend on outer tests."""
from pathlib import Path
import json,hashlib,datetime,itertools,csv,platform
import numpy as np
import scipy

ROOT=Path(__file__).resolve().parent
ALPHAS=[.1,1,10,100,1000]
CONVENTIONAL=['snapshot','time_average','summary_ablation','multiscale_ema','temporal_bins','production_decay']

def balanced_weights(rep,well,normalize_n=False):
    weights=np.zeros(len(rep))
    groups=np.unique(rep)
    for g in groups:
        ws=np.unique(well[rep==g])
        for w in ws:
            m=(rep==g)&(well==w)
            weights[m]=1/(len(groups)*len(ws)*m.sum())
    if normalize_n:weights*=len(weights)
    return weights

def fit_path_predict(x,y,rep,well,xt,alphas=ALPHAS):
    w=balanced_weights(rep,well,normalize_n=True)
    ym=np.average(y,weights=w)
    if x.shape[1]==0:return [np.full(len(xt),ym) for _ in alphas]
    mu=np.average(x,axis=0,weights=w)
    sd=np.sqrt(np.average((x-mu)**2,axis=0,weights=w));sd[sd==0]=1
    z=(x-mu)/sd;zt=(xt-mu)/sd
    gram=z.T@(w[:,None]*z)
    rhs=z.T@(w*(y-ym))
    eye=np.eye(x.shape[1])
    return [zt@np.linalg.solve(gram+a*eye,rhs)+ym for a in alphas]

def metrics(y,p,rep,well):
    w=balanced_weights(rep,well)
    mse=float(np.sum(w*(y-p)**2));mae=float(np.sum(w*np.abs(y-p)))
    den=float(np.sum(w*(y-np.sum(w*y))**2))
    return dict(mse=mse,mae=mae,r2=1-mse/den if den>0 else None)

def signflip(d):
    d=np.array(d);obs=abs(d.mean())
    values=[abs(np.mean(d*np.array(s))) for s in itertools.product([-1,1],repeat=len(d))]
    return float(np.mean(np.array(values)>=obs-1e-15))

def main():
    freeze=json.loads((ROOT/'protocol_freeze.json').read_text())
    assert hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest()==freeze['protocol_sha256']
    started=datetime.datetime.now(datetime.timezone.utc).isoformat()
    d=np.load(ROOT/'data/analysis_data.npz',allow_pickle=False)
    model_names=[k[len('features_'):] for k in d.files if k.startswith('features_')]
    target_names=list(d['target_names']);all_rep=d['replicate'];all_well=d['well']
    rows=[];tuning=[];predictions={};target_results={}
    for j,target in enumerate(target_names):
        valid=np.isfinite(d['Y'][:,j])&(d['Y'][:,j]>0)
        yy=np.log10(d['Y'][valid,j]);rr=all_rep[valid];ww=all_well[valid]
        feats={name:d['features_'+name][valid] for name in model_names}
        pp={name:np.full(len(yy),np.nan) for name in model_names+['selected_conventional']}
        selections=[]
        for held in np.unique(rr):
            train=rr!=held;test=rr==held
            dev_groups=np.unique(rr[train]);best={};inner_score={}
            for name in model_names:
                inner=[]
                for val_group in dev_groups:
                    itrain=train&(rr!=val_group);ival=train&(rr==val_group)
                    preds=fit_path_predict(feats[name][itrain],yy[itrain],rr[itrain],ww[itrain],feats[name][ival])
                    inner.append([metrics(yy[ival],p,rr[ival],ww[ival])['mse'] for p in preds])
                scores=np.mean(inner,axis=0);chosen=int(np.argmin(scores))
                best[name]=ALPHAS[chosen];inner_score[name]=float(scores[chosen])
                tuning.append(dict(target=target,held_out_replicate=int(held),model=name,
                                   alpha=best[name],inner_macro_mse=inner_score[name],all_alpha_scores=list(scores)))
                pred=fit_path_predict(feats[name][train],yy[train],rr[train],ww[train],feats[name][test],[best[name]])[0]
                pp[name][test]=pred
                rows.append(dict(target=target,held_out_replicate=int(held),model=name,alpha=best[name],
                                 n_train=int(train.sum()),n_test=int(test.sum()),n_test_wells=len(np.unique(ww[test])),
                                 n_features=feats[name].shape[1],**metrics(yy[test],pred,rr[test],ww[test])))
            chosen=min(CONVENTIONAL,key=lambda name:inner_score[name])
            pp['selected_conventional'][test]=pp[chosen][test]
            selections.append(dict(held_out_replicate=int(held),model=chosen,alpha=best[chosen],inner_macro_mse=inner_score[chosen]))
            rows.append(dict(target=target,held_out_replicate=int(held),model='selected_conventional',alpha=best[chosen],
                             n_train=int(train.sum()),n_test=int(test.sum()),n_test_wells=len(np.unique(ww[test])),
                             n_features=feats[chosen].shape[1],**metrics(yy[test],pp[chosen][test],rr[test],ww[test])))
        for name in pp:assert np.isfinite(pp[name]).all()
        equality=float(np.max(np.abs(pp['efmw_memory']-pp['matched_ewma'])))
        np.testing.assert_allclose(pp['efmw_memory'],pp['matched_ewma'],rtol=1e-9,atol=1e-10)
        aggregate={name:{k:float(np.mean([row[k] for row in rows if row['target']==target and row['model']==name]))
                         for k in ['mse','mae','r2']} for name in pp}
        def foldm(name):return np.array([row['mse'] for row in rows if row['target']==target and row['model']==name])
        em=foldm('efmw_memory');cm=foldm('selected_conventional');am=foldm('summary_ablation')
        improvement=float(1-em.mean()/cm.mean());ablation_gain=float(1-em.mean()/am.mean())
        rng=np.random.default_rng(20261025)
        idx=rng.integers(0,len(em),size=(20000,len(em)))
        boot=1-em[idx].mean(axis=1)/cm[idx].mean(axis=1)
        target_results[target]=dict(n_cells=int(valid.sum()),aggregate=aggregate,comparator_selection=selections,
            relative_mse_improvement_vs_selected=improvement,relative_mse_improvement_vs_ablation=ablation_gain,
            candidate_better_all_replicates=bool(np.all(em<cm)),ablation_better_all_replicates=bool(np.all(em<am)),
            practical_screen_pass=bool(improvement>=.05 and np.all(em<cm) and np.all(em<am)),
            paired_replicate_signflip_p=signflip(cm-em),
            descriptive_replicate_bootstrap_95pct=list(np.quantile(boot,[.025,.975])),
            ewma_prediction_max_abs_difference=equality)
        predictions[target+'_source_excel_row']=d['source_excel_row'][valid]
        predictions[target+'_replicate']=rr;predictions[target+'_well']=ww
        predictions[target+'_observed_log10']=yy
        for name,p in pp.items():predictions[target+'_'+name]=p
        print(target,'n',valid.sum(),'gain_vs_selected',round(100*improvement,3),'percent',
              'screen_pass',target_results[target]['practical_screen_pass'],flush=True)
    with (ROOT/'results/fold_metrics.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    (ROOT/'results/inner_tuning.json').write_text(json.dumps(tuning,indent=2)+'\n')
    np.savez_compressed(ROOT/'results/held_out_predictions.npz',**predictions)
    result=dict(study='EFMW-BIO-001',protocol_sha256=freeze['protocol_sha256'],started_at_utc=started,
                completed_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                primary_target='FRA1_nuc',results=target_results,
                limitations=['Author preprocessing aligns outcomes across all replicates.',
                             'Only three independent replicates; cellular counts do not increase experiment count.',
                             'The transferred recurrence is mathematically conventional EWMA.',
                             'One cell line, processed microscopy data, no independent lab replication.',
                             'Full nonlinear published ODE and CNN not reproduced; comparisons are to listed models.',
                             'Downloadable row count differs from paper Figure 2 count; reason not reconciled.'],
                environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__))
    (ROOT/'results/benchmark.json').write_text(json.dumps(result,indent=2)+'\n')
    print('Complete',json.dumps(target_results['FRA1_nuc'],indent=2),flush=True)

if __name__=='__main__':main()
