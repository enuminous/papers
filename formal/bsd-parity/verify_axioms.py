#!/usr/bin/env python3
"""Reject unproved admissions and any non-foundational theorem dependency."""
from pathlib import Path
import json
import re

root = Path(__file__).resolve().parent
names = []
for source in sorted((root/'BSDImprovements').glob('*.lean')):
    names += ['BSDImprovements.'+name for name in re.findall(r'^theorem\s+(\w+)',source.read_text(),re.M)]
log = (root/'verification/axioms.log').read_text()
allowed = {'propext','Classical.choice','Quot.sound'}
results = []
for name in names:
    pattern = re.escape("'"+name+"'") + r'\s+(?:depends on axioms: \[([^\]]*)\]|does not depend on any axioms)'
    match = re.search(pattern,log)
    if not match:
        raise SystemExit('Missing axiom audit result: '+name)
    axioms = sorted({s.strip() for s in (match.group(1) or '').split(',') if s.strip()})
    if set(axioms) - allowed:
        raise SystemExit('Unexpected axiom dependency: '+name+' '+str(axioms))
    results.append(dict(theorem=name, axioms=axioms))
report = dict(theorem_count=len(results), all_pass=True,
              allowed_axioms=sorted(allowed), theorems=results)
(root/'verification/axiom-audit.json').write_text(json.dumps(report,indent=2)+'\n')
print(f'PASS: {len(results)} named theorems, only standard foundational axioms.')
