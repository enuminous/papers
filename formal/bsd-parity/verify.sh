#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p verification
python3 verify_arithmetic.py | tee verification/arithmetic-check.log
lake build 2>&1 | tee verification/build.log
lake env lean AxiomAudit.lean 2>&1 | tee verification/axioms.log
python3 verify_axioms.py
