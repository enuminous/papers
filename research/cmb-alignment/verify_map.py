#!/usr/bin/env python3
"""Compare a fresh FITS extraction to the archived numerical measurement."""
import json
import sys
from pathlib import Path
import numpy as np

root = Path(__file__).resolve().parent
old = json.loads((root / "raw-map-results.json").read_text())
new = json.loads(Path(sys.argv[1]).read_text())
assert new["input_sha256"] == old["input_sha256"]
assert new["plan_id"] == old["plan_id"]
max_a = 0.0
max_axis = 0.0
for iteration in ("0", "3", "5"):
    for treatment in ("uncorrected", "DQ_corrected"):
        a = old["runs_by_iteration"][iteration][treatment]
        b = new["runs_by_iteration"][iteration][treatment]
        max_a = max(max_a, abs(a["A23"] - b["A23"]))
        assert a["max_pair"]["ell_pair"] == b["max_pair"]["ell_pair"]
        for ell in map(str, range(2, 11)):
            x, y = a["all_axes"][ell], b["all_axes"][ell]
            # Headless axes must agree up to a sign.
            max_axis = max(max_axis, abs(1 - abs(float(np.dot(x["axis"], y["axis"])))))
            for part in ("alm_re_m_minus_l_to_l", "alm_im_m_minus_l_to_l"):
                assert np.allclose(x[part], y[part], rtol=1e-9, atol=1e-7), (iteration, treatment, ell, part)
assert max_a < 1e-8 and max_axis < 1e-10
print(json.dumps({"status": "PASS", "max_A23_difference": max_a,
                  "max_antipodal_axis_difference": max_axis, "versions": new["versions"]}, indent=2))
