"""Run unchanged frozen model code in a local staging folder, verify, then copy atomically.

This wrapper prevents a partially-written NPZ from becoming the visible result on
synchronized filesystems. It makes no change to analysis or model selection.
"""
from pathlib import Path
import tempfile,shutil,subprocess,sys,os,zipfile
ROOT=Path(__file__).resolve().parent
with tempfile.TemporaryDirectory(prefix='efmw-bio001-reproduce-') as folder:
    stage=Path(folder);(stage/'data').mkdir();(stage/'results').mkdir()
    for name in ['run_benchmark.py','prepare_data.py','verify_results.py','PROTOCOL.md','protocol_freeze.json','code_freeze.json']:
        shutil.copy2(ROOT/name,stage/name)
    for name in ['analysis_data.npz','df_erk_MCF10A.xlsx']:
        source=ROOT/'data'/name
        if source.exists():
            try:os.link(source,stage/'data'/name)
            except OSError:shutil.copy2(source,stage/'data'/name)
    env=dict(os.environ,OPENBLAS_NUM_THREADS='2',OMP_NUM_THREADS='2')
    subprocess.run([sys.executable,str(stage/'run_benchmark.py')],check=True,env=env)
    with zipfile.ZipFile(stage/'results/held_out_predictions.npz') as z:assert z.testzip() is None
    subprocess.run([sys.executable,str(stage/'verify_results.py')],check=True,env=env)
    for source in (stage/'results').iterdir():
        pending=ROOT/'results'/(source.name+'.pending')
        shutil.copy2(source,pending);os.replace(pending,ROOT/'results'/source.name)
print('Frozen benchmark reproduced and independently checked.')
