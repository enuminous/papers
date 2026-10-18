#!/usr/bin/env python3
"""Rerun the recovered 2026 toy ensemble, keeping its original file unchanged."""
import ast
import hashlib
import json
import platform
import sys
from pathlib import Path
import numpy as np

root = Path(__file__).resolve().parent
source = root / "recovered/recursion_run3.py"
tree = ast.parse(source.read_text(), filename=str(source))
# Retain every computation, omit only the final absolute-path write and print.
assert isinstance(tree.body[-2], ast.Expr) and isinstance(tree.body[-1], ast.Expr)
assert "write_text" in ast.unparse(tree.body[-2]) and ast.unparse(tree.body[-1]).startswith("print(")
tree.body = tree.body[:-2]
namespace = {}
exec(compile(tree, str(source), "exec"), namespace)
actual = namespace["out"]
expected = json.loads((root / "recovered/recursion_run3_results.json").read_text())
maximum = 0.0

def compare(a, b, path=""):
    global maximum
    if isinstance(a, dict):
        assert a.keys() == b.keys(), path
        for key in a:
            compare(a[key], b[key], path + "." + key)
    elif isinstance(a, list):
        assert len(a) == len(b), path
        for index, (x, y) in enumerate(zip(a, b)):
            compare(x, y, path + f"[{index}]")
    elif isinstance(a, (int, float)):
        difference = abs(a - b)
        maximum = max(maximum, difference)
        assert difference <= 1e-12 + 1e-10 * abs(b), (path, a, b)
    else:
        assert a == b, path

compare(actual, expected)
report = {"status": "PASS", "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
          "scope": "Recovered October 18 Universe 003; not the January 2025 historical claim.",
          "adaptation": "Omitted final two I/O statements via AST; all numerical statements unchanged.",
          "null_runs": 128, "biased_control_runs": 32, "objects_per_run": 100000,
          "maximum_absolute_difference_from_saved_json": maximum,
          "versions": {"python": platform.python_version(), "numpy": np.__version__}}
if len(sys.argv) > 1:
    Path(sys.argv[1]).write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
