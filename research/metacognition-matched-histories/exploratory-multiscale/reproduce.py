"""Reproduce this extension into a NEW directory; never overwrite published files."""
import argparse
import datetime
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shlex
import subprocess
import sys
import time

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--data', type=Path, required=True, help='Directory containing checksum-verified t1.csv and t2.csv')
    p.add_argument('--out', type=Path, required=True, help='New output directory; must not exist')
    a = p.parse_args()
    data, out = a.data.resolve(), a.out.resolve()
    if out.exists():
        p.error('--out must not already exist; choose a new path')
    out.mkdir(parents=True)
    logs = out/'execution'; logs.mkdir()
    results = out/'results'; results.mkdir()
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1')
    versions = {k: importlib.metadata.version(k) for k in ['numpy', 'pandas', 'scipy', 'scikit-learn']}
    expected = dict(line.strip().split('==') for line in (PARENT/'requirements.txt').read_text().splitlines() if line.strip())
    if versions != expected:
        print('WARNING: dependency versions differ from the published pins:', versions, flush=True)
    inputs = {'base_commit': '65f50f6710efa6801169429e5a5ad567f4d567d8',
              'python': platform.python_version(), 'versions': versions,
              'source_sha256': {str(f.relative_to(HERE)): hashlib.sha256(f.read_bytes()).hexdigest()
                                for f in sorted(HERE.glob('*.py'))},
              'plan_sha256': hashlib.sha256((HERE/'PLAN.md').read_bytes()).hexdigest(),
              'data': {k: {'bytes': (data/(k+'.csv')).stat().st_size,
                           'sha256': hashlib.sha256((data/(k+'.csv')).read_bytes()).hexdigest()} for k in ['t1', 't2']}}
    (out/'inputs.json').write_text(json.dumps(inputs, indent=2)+'\n')
    def run(name, args, cwd=HERE):
        cmd = [sys.executable]+list(map(str, args))
        started = datetime.datetime.now(datetime.timezone.utc).isoformat(); t = time.monotonic()
        print('$', shlex.join(cmd), flush=True)
        process = subprocess.run(cmd, cwd=cwd, env=env, text=True, capture_output=True)
        (logs/(name+'.stdout.txt')).write_text(process.stdout)
        (logs/(name+'.stderr.txt')).write_text(process.stderr)
        record = {'name': name, 'started_utc': started, 'cwd': str(cwd), 'argv': cmd,
                  'exit_code': process.returncode, 'elapsed_seconds': time.monotonic()-t,
                  'environment': {k: env[k] for k in ['OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS']},
                  'stdout': name+'.stdout.txt', 'stderr': name+'.stderr.txt'}
        with (logs/'commands.jsonl').open('a') as f:
            f.write(json.dumps(record)+'\n')
        print(process.stdout, end='', flush=True)
        print(process.stderr, end='', file=sys.stderr, flush=True)
        if process.returncode:
            raise SystemExit(process.returncode)
    run('signal-tests', ['-m', 'unittest', '-v', 'test_multiscale.py'])
    run('original-analysis', ['analyze.py', data, logs/'replayed-results.json'], PARENT)
    run('original-sensitivity', ['sensitivity.py', data, logs/'replayed-sensitivity.json'], PARENT)
    run('original-pairs', ['matched.py', logs/'replayed-pairs.csv'], PARENT)
    run('multiscale-pairs', ['multiscale.py', 'pairs', '--out', results])
    run('multiscale-behavior', ['multiscale.py', 'behavior', '--data', data, '--out', results, '--controls', '20'])
    run('verify', ['verify.py', '--execution', logs, '--new-results', results, '--out', out/'verification.json'])
    manifest = {str(f.relative_to(out)): hashlib.sha256(f.read_bytes()).hexdigest()
                for f in sorted(out.rglob('*')) if f.is_file()}
    (out/'output_sha256.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print('PASS: full replay completed without changing original files.', flush=True)


if __name__ == '__main__':
    main()
