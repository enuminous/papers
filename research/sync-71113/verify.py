#!/usr/bin/env python3
"""Exact finite checks for SYNC-71113-001; Python >=3.9, standard library only.

Run from any directory:
    python research/sync-71113/verify.py --check
To regenerate the deterministic published tables:
    python research/sync-71113/verify.py --write
This checks finite arithmetic, not empirical synchronization performance.
"""

import argparse
import csv
import hashlib
import io
import itertools
import json
import math
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent
BARKER = {
    7: (1, 1, 1, -1, -1, 1, -1),
    11: (1, 1, 1, -1, -1, -1, 1, -1, -1, 1, -1),
    13: (1, 1, 1, 1, 1, -1, -1, 1, 1, -1, 1, -1, 1),
}
N = 1001


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def aperiodic(sequence):
    n = len(sequence)
    return [sum(sequence[i] * sequence[i + k] for i in range(n - k))
            for k in range(n)]


def periodic(sequence):
    n = len(sequence)
    return [sum(sequence[i] * sequence[(i + k) % n] for i in range(n))
            for k in range(n)]


def kron(left, right):
    return tuple(a * b for a in left for b in right)


def kronecker_by_index(order):
    """Separate mixed-radix implementation used to check the construction."""
    p, q, r = order
    return tuple(BARKER[p][n // (q * r)] *
                 BARKER[q][(n // r) % q] *
                 BARKER[r][n % r] for n in range(p * q * r))


def summary(correlation):
    peak = correlation[0]
    sidelobe = max(abs(x) for x in correlation[1:])
    common = math.gcd(peak, sidelobe)
    return {
        "length": peak,
        "main_peak": peak,
        "peak_absolute_sidelobe": sidelobe,
        "peak_positive_lags": [k for k, x in enumerate(correlation)
                               if k and abs(x) == sidelobe],
        "sidelobe_to_main_ratio": f"{sidelobe // common}/{peak // common}",
        "sidelobe_to_main_dB": round(20 * math.log10(sidelobe / peak), 6),
    }


def triples(budget):
    """All unordered positive-integer triples with sum <= budget, exactly once."""
    return [(a, b, c)
            for a in range(1, budget // 3 + 1)
            for b in range(a, (budget - a) // 2 + 1)
            for c in range(b, budget - a - b + 1)]


def optimum(budget):
    candidates = triples(budget)
    best = max(math.lcm(*x) for x in candidates)
    return {
        "sum_budget": budget,
        "unordered_triple_count": len(candidates),
        "maximum_lcm": best,
        "maximizers": [list(x) for x in candidates if math.lcm(*x) == best],
    }


def csv_text(header, rows):
    buf = io.StringIO(newline="")
    writer = csv.writer(buf, lineterminator="\n")
    writer.writerow(header)
    writer.writerows(rows)
    return buf.getvalue()


def generate():
    # CRT bijection and the exact joint orbit, including non-prime comparators.
    phases = {(n % 7, n % 11, n % 13) for n in range(N)}
    require(len(phases) == N, "CRT orbit does not contain 1001 distinct phases")
    require(next(n for n in range(1, N + 1)
                 if all(n % p == 0 for p in BARKER)) == N,
            "Unexpected joint return time")
    base_ac = {p: aperiodic(s) for p, s in BARKER.items()}
    base_pc = {p: periodic(s) for p, s in BARKER.items()}
    for p, ac in base_ac.items():
        require(ac[0] == p and max(map(abs, ac[1:])) == 1,
                f"Invalid Barker sequence of length {p}")
        require(all(ac[k] == 0 for k in range(1, p, 2)),
                f"Odd-lag aperiodic correlation is not zero for {p}")
        expected = -1 if p % 4 == 3 else 1
        require(all(x == expected for x in base_pc[p][1:]),
                f"Unexpected periodic correlation for {p}")

    sequences, correlations = {}, {}
    nested_rows = []
    for order in itertools.permutations(BARKER):
        s = (1,)
        for p in order:
            s = kron(s, BARKER[p])
        require(s == kronecker_by_index(order), "Kronecker indexing mismatch")
        key = "nested_" + "_".join(map(str, order))
        ac = aperiodic(s)
        require(len(s) == N and max(map(abs, ac[1:])) == 143,
                f"Nested sidelobe check failed for {order}")
        require(all(ac[k] == 0 for k in range(1, N, 2)),
                "Nested odd-shift cancellation failed")
        sequences[key] = s
        correlations[key + "_aperiodic"] = ac
        nested_rows.append({"order": list(order), **summary(ac)})
    require(correlations["nested_7_11_13_aperiodic"][286] == -143,
            "Block-shift identity failed")

    # A different ordering: sample the tensor along a CRT diagonal.
    crt = tuple(math.prod(BARKER[p][n % p] for p in BARKER)
                for n in range(N))
    crt_ac = aperiodic(crt)
    crt_pc = periodic(crt)
    factorized = [math.prod(base_pc[p][k % p] for p in BARKER)
                  for k in range(N)]
    require(crt_pc == factorized, "Periodic CRT factorization failed")
    require(max(map(abs, crt_ac[1:])) == 122, "CRT aperiodic result changed")
    require(max(map(abs, crt_pc[1:])) == 143, "CRT periodic result changed")
    require(all(abs(x) < N for x in crt_pc[1:]),
            "CRT signal has a smaller exact period")
    expected_distribution = {
        -143: 6, -91: 10, -11: 72, -7: 120,
        1: 720, 13: 60, 77: 12, 1001: 1,
    }
    require(Counter(crt_pc) == expected_distribution,
            "CRT correlation multiplicities changed")
    sequences["crt_product"] = crt
    correlations["crt_product_aperiodic"] = crt_ac
    correlations["crt_product_periodic"] = crt_pc

    # Independent enumeration protects against omissions in the compact loops.
    check_triples = [t for t in itertools.combinations_with_replacement(range(1, 30), 3)
                    if sum(t) <= 31]
    require(triples(31) == check_triples, "Enumeration implementations disagree")
    require(len(check_triples) == 865, "Unexpected triple count")
    opts = [optimum(b) for b in range(29, 34)]
    require(opts[2]["maximum_lcm"] == 1001 and
            opts[2]["maximizers"] == [[7, 11, 13]],
            "31-position optimum failed")
    require(opts[1]["maximum_lcm"] == 990 and opts[1]["maximizers"] == [[9, 10, 11]],
            "30-position control failed")
    require(opts[3]["maximum_lcm"] == 1170 and opts[3]["maximizers"] == [[9, 10, 13]],
            "32-position control failed")
    reduced_cases = {}
    for a in (7, 8, 9, 10):
        candidates = [t for t in check_triples if t[0] == a and
                      all(math.gcd(x, y) == 1 for x, y in itertools.combinations(t, 2))]
        best = max((math.prod(t) for t in candidates), default=None)
        reduced_cases[str(a)] = {
            "max_product": best,
            "maximizers": [list(t) for t in candidates if math.prod(t) == best],
        }

    results = {
        "schema_version": 1,
        "study": "SYNC-71113-001",
        "version": "1.0.0",
        "analysis_date": "2026-10-25",
        "status": "Exact finite calculations; exploratory choice of triple and budget; no physical experiment",
        "arithmetic": {"sum": 31, "product": 1001, "joint_period_ticks": 1001,
                       "distinct_CRT_phases": len(phases),
                       "decimal_identity": "7*11*13 = 10**3+1"},
        "base_sequences": {str(p): list(s) for p, s in BARKER.items()},
        "base_aperiodic": {str(p): summary(base_ac[p]) for p in BARKER},
        "nested_aperiodic": nested_rows,
        "crt_product_aperiodic": summary(crt_ac),
        "crt_product_periodic": summary(crt_pc),
        "crt_periodic_value_counts": {str(k): v for k, v in sorted(expected_distribution.items())},
        "three_counter_optima": opts,
        "analytic_proof_reduced_cases": reduced_cases,
        "excluded_claims": ["Empirical synchronization advantage", "Physical law",
                            "EFMW-specific derivation", "Independent replication",
                            "Formal proof-assistant verification", "Novelty priority"],
    }
    seq_keys = list(sequences)
    corr_keys = list(correlations)
    files = {
        "results.json": json.dumps(results, indent=2, ensure_ascii=False) + "\n",
        "sequences.csv": csv_text(["index"] + seq_keys,
                                 ([n] + [sequences[k][n] for k in seq_keys] for n in range(N))),
        "correlations.csv": csv_text(["lag"] + corr_keys,
                                    ([n] + [correlations[k][n] for k in corr_keys] for n in range(N))),
        "triples_budget31.csv": csv_text(
            ["a", "b", "c", "sum", "lcm", "pairwise_coprime"],
            ([*t, sum(t), math.lcm(*t),
              int(all(math.gcd(x, y) == 1 for x, y in itertools.combinations(t, 2)))]
             for t in check_triples)),
    }
    hashes = {name: hashlib.sha256(body.encode("utf-8")).hexdigest()
              for name, body in files.items()}
    hashes["verify.py"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    files["checksums.json"] = json.dumps(
        {"algorithm": "SHA-256", "scope": "Verifier and deterministic numerical outputs",
         "files": hashes}, indent=2) + "\n"
    return results, files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="Regenerate published tables")
    mode.add_argument("--check", action="store_true", help="Recompute and compare all published tables (default)")
    args = parser.parse_args()
    results, files = generate()
    if args.write:
        for name, text in files.items():
            (ROOT / name).write_bytes(text.encode("utf-8"))
    else:
        for name, text in files.items():
            path = ROOT / name
            require(path.exists(), f"Missing {name}; run --write")
            require(path.read_bytes() == text.encode("utf-8"), f"Published output differs: {name}")
    print(json.dumps({
        "result": "PASS",
        "mode": "write" if args.write else "check",
        "files": list(files),
        "joint_period": N,
        "nested_peak_sidelobe": 143,
        "crt_aperiodic_peak_sidelobe": 122,
        "crt_periodic_peak_sidelobe": 143,
        "budget31_triples": 865,
        "unique_budget31_maximizer": [7, 11, 13],
    }, indent=2))


if __name__ == "__main__":
    main()
