"""Verify original-source preservation and replay agreement without rewriting it."""
import argparse
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent


def compare(a, b, path='root', deltas=None):
    if deltas is None:
        deltas = []
    if isinstance(a, dict):
        assert a.keys() == b.keys(), path
        for k in a:
            compare(a[k], b[k], path+'.'+k, deltas)
    elif isinstance(a, list):
        assert len(a) == len(b), path
        for i, (x, y) in enumerate(zip(a, b)):
            compare(x, y, path+f'[{i}]', deltas)
    elif isinstance(a, (int, float)):
        assert math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9), (path, a, b)
        deltas.append(abs(a-b))
    else:
        assert a == b, (path, a, b)
    return deltas


def verify(execution, new_results):
    snapshot = json.loads((HERE/'source_snapshot.json').read_text())
    records = []
    for item in snapshot['source_files']:
        p = PARENT/Path(item['path']).name
        data = p.read_bytes()
        sha = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
        assert sha == item['git_blob_sha'], str(p)
        records.append({'name': p.name, 'bytes': len(data), 'git_blob_sha': sha,
                        'sha256': hashlib.sha256(data).hexdigest()})
    report = {'original_files_unchanged': True, 'original_source_files': records, 'replay': {}}
    assert (execution/'replayed-pairs.csv').read_bytes() == (PARENT/'pairs.csv').read_bytes()
    report['replay']['pairs_byte_identical'] = True
    for name in ['results', 'sensitivity']:
        a = json.loads((PARENT/(name+'.json')).read_text())
        b = json.loads((execution/('replayed-'+name+'.json')).read_text())
        delta = compare(a, b)
        report['replay'][name] = {'numeric_leaves': len(delta), 'max_absolute_difference': max(delta),
                                  'tolerance_rtol': 1e-9, 'tolerance_atol': 1e-9}
    if new_results is not None:
        new = json.loads((new_results/'behavior-results.json').read_text())['results']
        old = json.loads((PARENT/'results.json').read_text())['results']
        comparisons = {}
        for key, val in old.items():
            new_val = new['original'][key]
            delta = compare(val['base_mse'], new_val['mse']['base'])
            delta += compare(val['B']['mse_gain'], new_val['comparisons']['base__to__B']['mse_gain'])
            delta += compare(val['B']['gain_ci'], new_val['comparisons']['base__to__B']['conditional_participant_bootstrap_95ci'])
            assert val['trials'] == new_val['trials'] and val['participants'] == new_val['participants']
            comparisons[key] = max(delta)
        sensitivity = json.loads((PARENT/'sensitivity.json').read_text())
        for s in ['t1', 't2']:
            val = sensitivity[s+'_moments_and_rating_cues']
            new_val = new['rating_cues'][s+'_confidence']
            delta = compare(val['base_mse'], new_val['mse']['base'])
            delta += compare(val['B']['mse_gain'], new_val['comparisons']['base__to__B']['mse_gain'])
            delta += compare(val['B']['gain_ci'], new_val['comparisons']['base__to__B']['conditional_participant_bootstrap_95ci'])
            comparisons[s+'_rating_cues'] = max(delta)
        report['new_pipeline_matches_original_baselines_max_abs_difference'] = comparisons
    return report


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('--execution', required=True, type=Path)
    p.add_argument('--new-results', type=Path)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    result = verify(a.execution, a.new_results)
    a.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
