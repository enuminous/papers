"""Private exploratory extension. Does not modify original sources or results.

All filtering is causal and block-local. See PLAN.md for frozen definitions.
"""
from __future__ import annotations

import argparse
import csv
from fractions import Fraction as F
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
import sys

import numpy as np
import pandas as pd
from scipy.signal import lfilter
from sklearn.linear_model import Ridge

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
sys.path.insert(0, str(PARENT))
import analyze as original

C_NAMES = ['local', 'local_sq', 'fast', 'fast_sq', 'slow', 'slow_sq', 'haar4', 'haar4_sq']
A_NAMES = ['mag_fast', 'mag_slow']
MODELS = {'base': [], 'B': ['B'], 'C': C_NAMES, 'C_B': C_NAMES+['B'],
          'A': A_NAMES, 'A_B': A_NAMES+['B'], 'C_A': C_NAMES+A_NAMES,
          'C_A_B': C_NAMES+A_NAMES+['B']}
COMPARISONS = [('base', 'B'), ('base', 'C'), ('base', 'A'), ('base', 'C_A'),
               ('C', 'C_B'), ('A', 'A_B'), ('C_A', 'C_A_B'),
               ('B', 'C'), ('B', 'A'), ('B', 'C_A'), ('B', 'C_B')]
SEED = 20261106


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')


def exact_features(history):
    """Reference implementation on one oldest-first history, using rationals."""
    # NumPy integer numerators otherwise retain fixed-width arithmetic inside Fraction.
    e = tuple(F(v.item() if isinstance(v, np.generic) else v) for v in history)
    if len(e) < 4:
        raise ValueError('At least four observations required')
    def ew(r, fn=lambda x: x):
        return (1-r)*sum((r**k)*fn(v) for k, v in enumerate(reversed(e)))
    m = ew(F(1, 2)); q = ew(F(1, 2), lambda x: x*x); b = ew(F(1, 2), abs)
    d = e[-1]-e[-2]
    fast = ew(F(1, 4))-m
    slow = m-ew(F(3, 4))
    haar = (e[-1]+e[-2]-e[-3]-e[-4])/2
    return dict(m=m, Q=q, B=b, local=d, local_sq=d*d,
                fast=fast, fast_sq=fast*fast, slow=slow, slow_sq=slow*slow,
                haar4=haar, haar4_sq=haar*haar,
                mag_fast=ew(F(1, 4), abs), mag_slow=ew(F(3, 4), abs))


def before_trial(errors):
    """Float features at t depend only on errors with index < t; zero state."""
    e = np.asarray(errors, dtype=float)
    def lag(k):
        out = np.zeros(len(e))
        if k < len(e):
            out[k:] = e[:-k]
        return out
    def ew(r, x):
        return np.r_[0., lfilter([1-r], [1., -r], x)[:-1]]
    m = ew(.5, e)
    vals = dict(m=m, Q=ew(.5, e*e), B=ew(.5, abs(e)),
                local=lag(1)-lag(2), fast=ew(.25, e)-m,
                slow=m-ew(.75, e),
                haar4=(lag(1)+lag(2)-lag(3)-lag(4))/2,
                mag_fast=ew(.25, abs(e)), mag_slow=ew(.75, abs(e)))
    for n in ['local', 'fast', 'slow', 'haar4']:
        vals[n+'_sq'] = vals[n]**2
    return pd.DataFrame(vals)


def pair_analysis(pairs_path, out):
    rows = list(csv.DictReader(pairs_path.open()))
    counts = {k: 0 for k in C_NAMES+A_NAMES}
    bank_counts = {'C': 0, 'A': 0, 'C_A': 0}
    detail, canonical = [], set()
    min_delta, max_delta = {}, {}
    for i, row in enumerate(rows):
        a = tuple(map(int, row['A_oldest_first'].split()))
        b = tuple(map(int, row['B_oldest_first'].split()))
        fa, fb = exact_features(a), exact_features(b)
        assert sorted(a) == sorted(b) and a[-2:] == b[-2:]
        assert fa['m'] == fb['m'] == F(row['common_m'])
        assert fa['Q'] == fb['Q'] == F(row['common_Q'])
        assert fa['B'] == F(row['abs_A']) > fb['B'] == F(row['abs_B'])
        assert abs(fa['m'])/fa['B'] == F(row['R_A'])
        assert abs(fb['m'])/fb['B'] == F(row['R_B'])
        canonical.add(min((a, b), (tuple(-x for x in a), tuple(-x for x in b))))
        r = {'row': i, 'history_A': row['A_oldest_first'], 'history_B': row['B_oldest_first']}
        for k in ['m', 'Q', 'B']+C_NAMES+A_NAMES:
            delta = fa[k]-fb[k]
            r[k+'_A'], r[k+'_B'], r['delta_'+k] = map(str, (fa[k], fb[k], delta))
            if k in counts:
                counts[k] += int(delta != 0)
                if delta != 0:
                    min_delta[k] = min(min_delta.get(k, abs(delta)), abs(delta))
                    max_delta[k] = max(max_delta.get(k, abs(delta)), abs(delta))
        for bank, keys in [('C', C_NAMES), ('A', A_NAMES), ('C_A', C_NAMES+A_NAMES)]:
            bank_counts[bank] += int(any(fa[k] != fb[k] for k in keys))
        detail.append(r)
    with (out/'pair-features.csv').open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=detail[0].keys(), lineterminator='\n')
        w.writeheader(); w.writerows(detail)
    example_a, example_b = (3, 0, -1, 2, 1, 0), (-1, 2, 3, 0, 1, 0)
    example = {'history_A': example_a, 'history_B': example_b,
               'features_A': {k: str(v) for k, v in exact_features(example_a).items()},
               'features_B': {k: str(v) for k, v in exact_features(example_b).items()}}
    report = {'rows_including_mirrors': len(rows), 'pairs_modulo_global_sign': len(canonical),
              'all_original_match_checks': 'PASS', 'different_by_feature': counts,
              'different_by_bank': bank_counts,
              'minimum_nonzero_absolute_difference': {k: str(v) for k, v in min_delta.items()},
              'maximum_absolute_difference': {k: str(v) for k, v in max_delta.items()},
              'fixed_original_example_with_appended_zero': example,
              'interpretation': 'Selected constructed bank, not human observations; counts are descriptive.'}
    write_json(out/'pair-results.json', report)
    print(json.dumps(report, indent=2), flush=True)


def load_session(path, key):
    frame = original.get_features(path, key)
    raw = pd.read_csv(path, usecols=['id', 'nBlock', 'nTrial', 'behav_d']).sort_values(['id', 'nTrial'])
    blocks = []
    for (who, block), g in raw.groupby(['id', 'nBlock'], sort=False):
        z = before_trial(g.behav_d.to_numpy())
        z['id'], z['block'], z['trial'] = who, block, g.nTrial.to_numpy()
        blocks.append(z.iloc[5:])
    extra = pd.concat(blocks, ignore_index=True)
    keys = ['id', 'block', 'trial']
    assert frame[keys].equals(extra[keys])
    np.testing.assert_allclose(frame.m, extra.m, atol=1e-14, rtol=1e-14)
    np.testing.assert_allclose(frame.B, extra.B, atol=1e-14, rtol=1e-14)
    np.testing.assert_allclose(frame.rms**2, extra.Q, atol=1e-14, rtol=1e-14)
    for k in C_NAMES+A_NAMES:
        frame[k] = extra[k].to_numpy()
    assert np.isfinite(frame[C_NAMES+A_NAMES].to_numpy()).all()
    frame['moment_ratio'] = frame.abs_m/frame.rms
    frame['move_size'] = frame.adjustment.abs()
    return frame


def fold_map(frame):
    ids = sorted(frame.id.unique(), key=lambda i: hashlib.sha256(f'EFMW:{i}'.encode()).digest())
    return {who: k % 5 for k, who in enumerate(ids)}


def augment(x, y, train, test, names):
    if not names:
        return x, y
    a, b = train[names].to_numpy(), test[names].to_numpy()
    mu, sd = a.mean(axis=0), a.std(axis=0)
    sd[sd < 1e-9] = 1.
    return np.column_stack((x, (a-mu)/sd)), np.column_stack((y, (b-mu)/sd))


def base_basis(train, test, baseline):
    x, y = original.basis(train, test)
    if baseline == 'rating_cues':
        x, y = augment(x, y, train, test, ['moment_ratio', 'slider', 'move_size'])
    return x, y


def summarize(loss):
    scores = loss.groupby('id').mean(numeric_only=True)
    rng = np.random.default_rng(SEED)
    idx = rng.integers(len(scores), size=(5000, len(scores)))
    result = {'participants': len(scores), 'trials': len(loss),
              'mse': {k: float(scores[k].mean()) for k in MODELS}, 'comparisons': {}}
    for base, alt in COMPARISONS:
        gain = (scores[base]-scores[alt]).to_numpy()
        result['comparisons'][base+'__to__'+alt] = {
            'mse_gain': float(gain.mean()),
            'percent_mse_gain': float(100*gain.mean()/scores[base].mean()),
            'conditional_participant_bootstrap_95ci': np.quantile(gain[idx].mean(axis=1), [.025, .975]).tolist(),
            'participants_with_positive_gain': int((gain > 0).sum())}
    return result


def circular_shift(frame, names, rng):
    """Keep columns aligned; independently shift each participant-block."""
    shifted = frame[names].copy()
    offsets = []
    for _, positions in frame.groupby(['id', 'block'], sort=False).indices.items():
        n = len(positions)
        assert n >= 11
        shift = int(rng.integers(5, n-4))
        shifted.iloc[positions] = np.roll(frame.iloc[positions][names].to_numpy(), shift, axis=0)
        offsets.append(shift)
    # Do not archive participant-linked rows. Digest plus seed makes the alignment reproducible.
    digest = hashlib.sha256(np.asarray(offsets, dtype='<i8').tobytes()).hexdigest()
    return shifted, {'blocks': len(offsets), 'minimum': min(offsets), 'maximum': max(offsets),
                     'offsets_sha256_little_endian_int64': digest}


def fit_behavior(data_dir, out, controls=20):
    sessions = {k: load_session(data_dir/(k+'.csv'), k) for k in original.HASHES}
    folds = fold_map(sessions['t1'])
    assert set(sessions['t2'].id) <= set(folds)
    reports, fold_rows = {}, []
    null_base_losses = {s: [] for s in sessions}
    for baseline in ['original', 'rating_cues']:
        targets = ['confidence', 'adjustment'] if baseline == 'original' else ['confidence']
        losses = {}
        for fold in range(5):
            tr = sessions['t1'].loc[sessions['t1'].id.map(folds) != fold]
            for visit, frame in sessions.items():
                te = frame.loc[frame.id.map(folds) == fold]
                assert set(tr.id).isdisjoint(te.id)
                x, y = base_basis(tr, te, baseline)
                for target in targets:
                    loss = pd.DataFrame({'id': te.id.to_numpy()})
                    for model_name, names in MODELS.items():
                        xx, yy = augment(x, y, tr, te, names)
                        model = Ridge(alpha=1.).fit(xx, tr[target])
                        loss[model_name] = (te[target].to_numpy()-model.predict(yy))**2
                        fold_rows.append({'baseline': baseline, 'target': target, 'session': visit,
                                          'fold': fold, 'model': model_name, 'test_participants': te.id.nunique(),
                                          'test_trials': len(te), 'columns': xx.shape[1],
                                          'participant_mse': float(loss.groupby('id')[model_name].mean().mean())})
                    losses.setdefault(visit+'_'+target, []).append(loss)
                    if baseline == 'original' and target == 'confidence':
                        null_base_losses[visit].append(loss[['id', 'base']])
            print(f'Completed {baseline} fold {fold}', flush=True)
        reports[baseline] = {k: summarize(pd.concat(v)) for k, v in losses.items()}
    metadata = {'base_commit': '65f50f6710efa6801169429e5a5ad567f4d567d8',
                'plan_sha256': hashlib.sha256((HERE/'PLAN.md').read_bytes()).hexdigest(),
                'data_sha256': {k: hashlib.sha256((data_dir/(k+'.csv')).read_bytes()).hexdigest() for k in sessions},
                'python': platform.python_version(),
                'versions': {k: importlib.metadata.version(k) for k in ['numpy', 'pandas', 'scipy', 'scikit-learn']},
                'models': MODELS, 'ridge_alpha': 1., 'bootstrap_replicates': 5000, 'bootstrap_seed': SEED,
                'sessions': {k: {'participants': int(v.id.nunique()), 'trials': len(v)} for k, v in sessions.items()}}
    write_json(out/'behavior-results.json', {'metadata': metadata, 'results': reports})
    pd.DataFrame(fold_rows).to_csv(out/'fold-results.csv', index=False)
    # Alignment diagnostics use original confidence baseline only. No outcome refitting choices.
    null_base = {s: pd.concat(v).groupby('id').base.mean() for s, v in null_base_losses.items()}
    null_rows = []
    for seed in range(20261107, 20261107+controls):
        for bank, names in [('B', ['B']), ('C', C_NAMES), ('A', A_NAMES)]:
            rng = np.random.default_rng(seed)
            shifted, manifests = {}, {}
            for visit, frame in sessions.items():
                shifted[visit], manifests[visit] = circular_shift(frame, names, rng)
            losses = {s: [] for s in sessions}
            for fold in range(5):
                train_mask = sessions['t1'].id.map(folds) != fold
                tr = sessions['t1'].loc[train_mask]
                for visit, frame in sessions.items():
                    test_mask = frame.id.map(folds) == fold
                    te = frame.loc[test_mask]
                    x, y = base_basis(tr, te, 'original')
                    xx, yy = augment(x, y, shifted['t1'].loc[train_mask], shifted[visit].loc[test_mask], names)
                    model = Ridge(alpha=1.).fit(xx, tr.confidence)
                    losses[visit].append(pd.DataFrame({'id': te.id.to_numpy(),
                        'loss': (te.confidence.to_numpy()-model.predict(yy))**2}))
            for visit in sessions:
                scores = pd.concat(losses[visit]).groupby('id').loss.mean()
                gain = null_base[visit]-scores
                null_rows.append({'seed': seed, 'bank': bank, 'session': visit,
                                  'mse_gain': float(gain.mean()),
                                  'percent_mse_gain': float(100*gain.mean()/null_base[visit].mean()),
                                  **manifests[visit]})
        print(f'Completed circular-shift diagnostic seed {seed}', flush=True)
    if null_rows:
        pd.DataFrame(null_rows).to_csv(out/'shift-controls.csv', index=False)
        summary = {'replicates': controls, 'kind': 'Alignment diagnostic, not a conditional randomization p-value', 'results': {}}
        for s in sessions:
            for bank in ['B', 'C', 'A']:
                gains = [r['mse_gain'] for r in null_rows if r['session'] == s and r['bank'] == bank]
                observed = reports['original'][s+'_confidence']['comparisons']['base__to__'+bank]['mse_gain']
                summary['results'][s+'_'+bank] = {'observed_mse_gain': observed, 'shifted_mean_mse_gain': float(np.mean(gains)),
                    'shifted_min_mse_gain': min(gains), 'shifted_max_mse_gain': max(gains),
                    'shifts_at_least_observed': sum(v >= observed for v in gains)}
        write_json(out/'shift-control-results.json', summary)
    print('Behavior and diagnostic outputs written:', out, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('pairs'); p.add_argument('--pairs', type=Path, default=PARENT/'pairs.csv')
    p.add_argument('--out', type=Path, required=True)
    p = sub.add_parser('behavior'); p.add_argument('--data', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True); p.add_argument('--controls', type=int, default=20)
    args = parser.parse_args(); args.out.mkdir(parents=True, exist_ok=True)
    if args.command == 'pairs':
        pair_analysis(args.pairs, args.out)
    else:
        fit_behavior(args.data, args.out, args.controls)


if __name__ == '__main__':
    main()
