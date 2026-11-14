#!/usr/bin/env python3
"""Check retained artifact integrity and independently recompute simple output relations."""
from pathlib import Path
import csv,hashlib,json,math
ROOT=Path(__file__).resolve().parent
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
lock=json.loads((ROOT/'SCOPE_LOCK.json').read_text())
for path,wanted in lock['files'].items():assert digest(ROOT/path)==wanted,path
p=json.loads((ROOT/'results/provenance.json').read_text())
assert digest(ROOT/'calculate.py')==p['calculation_sha256']
for path,wanted in p['results_sha256'].items():assert digest(ROOT/'results'/path)==wanted,path
ex=json.loads((ROOT/'results/example.json').read_text())
count=ex['incident_photons']*ex['detector_efficiency']*ex['regeneration_probability']
assert math.isclose(count,ex['expected_signal_counts'],rel_tol=1e-14)
assert math.isclose(ex['single_conversion_1']*ex['single_conversion_2'],
                    ex['regeneration_probability'],rel_tol=1e-14)
trans=json.loads((ROOT/'results/existing_bound_translation.json').read_text())
assert trans['C1_c_MW_GeV_inverse']==trans['published_scalar_g_GeV_inverse']/4
with (ROOT/'results/mass_scan.csv').open() as f:scan=list(csv.DictReader(f))
with (ROOT/'results/verification_grid.csv').open() as f:grid=list(csv.DictReader(f))
assert len(scan)==401 and len(grid)==35
assert all(0<=float(r['regeneration_probability'])<=1 for r in scan)
assert all(float(r['qL_relativistic_error'])<.01 for r in scan)
assert all(abs(float(r['matrix_exponential_probability'])-float(r['closed_probability']))<2e-13 for r in grid)
manifest=ROOT/'MANIFEST.sha256'
if manifest.exists():
    for line in manifest.read_text().splitlines():
        wanted,path=line.split('  ',1);assert digest(ROOT/path)==wanted,path
print(json.dumps({'source_scope_and_result_hashes':'verified',
    'matrix_grid_rows':len(grid),'mass_scan_rows':len(scan),
    'count_and_coupling_mapping':'verified',
    'maximum_accumulated_phase_approximation_error':max(float(r['qL_relativistic_error']) for r in scan),
    'scope':'Integrity and arithmetic check, not an independent experiment'},indent=2))

