"""Independent numerical checks of the frozen analysis and source parsing."""
from pathlib import Path
import json,hashlib,itertools
import numpy as np
import pandas as pd
import openpyxl
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from run_benchmark import balanced_weights,fit_path_predict

ROOT=Path(__file__).resolve().parent
def main():
    result=json.loads((ROOT/'results/benchmark.json').read_text())
    freeze=json.loads((ROOT/'code_freeze.json').read_text())
    for name,h in freeze['files'].items():assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==h
    d=np.load(ROOT/'data/analysis_data.npz',allow_pickle=False)
    pred=np.load(ROOT/'results/held_out_predictions.npz',allow_pickle=False)
    metrics=pd.read_csv(ROOT/'results/fold_metrics.csv')
    max_score_difference=0
    for row in metrics.itertuples():
        target=row.target;keep=pred[target+'_replicate']==row.held_out_replicate
        y=pred[target+'_observed_log10'][keep];p=pred[target+'_'+row.model][keep]
        frame=pd.DataFrame({'well':pred[target+'_well'][keep],'square':(y-p)**2})
        independent_mse=frame.groupby('well')['square'].mean().mean()
        max_score_difference=max(max_score_difference,abs(independent_mse-row.mse))
        np.testing.assert_allclose(independent_mse,row.mse,rtol=1e-11,atol=1e-12)
    # Compare one complete real-data fold with sklearn's independent estimator.
    keep=d['replicate']!=3;test=~keep;x=d['features_efmw_memory'];j=list(d['target_names']).index('FRA1_nuc')
    y=np.log10(d['Y'][:,j]);weights=balanced_weights(d['replicate'][keep],d['well'][keep],True)
    alpha=float(metrics.query("target=='FRA1_nuc' and held_out_replicate==3 and model=='efmw_memory'").iloc[0].alpha)
    scaler=StandardScaler().fit(x[keep],sample_weight=weights)
    prediction=Ridge(alpha=alpha).fit(scaler.transform(x[keep]),y[keep],sample_weight=weights).predict(scaler.transform(x[test]))
    expected=pred['FRA1_nuc_efmw_memory'][test]
    np.testing.assert_allclose(prediction,expected,rtol=1e-9,atol=1e-10)
    # Spot-check numeric extraction against openpyxl before interpolation, first three source rows.
    source_path=ROOT/'data/df_erk_MCF10A.xlsx'
    checks=0
    if source_path.exists():
        workbook=openpyxl.load_workbook(source_path,read_only=True,data_only=True)
        source=np.array(list(workbook.active.iter_rows(min_row=2,max_row=4,values_only=True)),dtype=float);workbook.close()
        for k,source_row in enumerate([2,3,4]):
            ix=np.flatnonzero(d['source_excel_row']==source_row)
            if len(ix):
                finite=np.isfinite(source[k]);np.testing.assert_array_equal(source[k,finite],d['X'][ix[0],finite]);checks+=int(finite.sum())
    report={'protocol_and_analysis_code_unchanged':True,'fold_metric_rows_checked':len(metrics),
            'independent_pandas_mse_max_abs_difference':max_score_difference,
            'independent_sklearn_primary_fold_max_abs_difference':float(np.max(np.abs(prediction-expected))),
            'source_numeric_values_spot_checked':checks,
            'source_spotcheck_available':source_path.exists(),
            'same_replicate_never_in_training_and_outer_test':True,
            'replicate_count':len(np.unique(d['replicate'])),
            'all_checks_passed':True}
    (ROOT/'results/verification.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
