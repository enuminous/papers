#!/usr/bin/env python3
"""Bounded algebra checks for the supplied parallel-qudit-sheet posters.

PASS validates a statement in the referee report, not physical time travel.
No third-party dependencies, network calls, randomness, or file writes.
"""
from fractions import Fraction as Q
from pathlib import Path
import hashlib
import json


def matmul(a, b):
    assert len(a[0]) == len(b)
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def identity(n):
    return [[Q(int(i == j)) for j in range(n)] for i in range(n)]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def quadratic(a, v):
    return sum((v[i] * a[i][j] * v[j]
                for i in range(len(v)) for j in range(len(v))), Q(0))


def matrix_strings(a):
    return [[str(x) for x in row] for row in a]


def main():
    checks = []

    def record(name, condition, details):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "status": "PASS", "details": details})

    # A counterexample to "inverse of lower triangular becomes upper triangular".
    m = [[Q(1), Q(0)], [Q(3), Q(1)]]
    inv = [[Q(1), Q(0)], [Q(-3), Q(1)]]
    record(
        "lower_triangular_inverse_counterexample",
        matmul(m, inv) == identity(2) and matmul(inv, m) == identity(2)
        and inv[0][1] == 0 and inv[1][0] != 0,
        {"matrix": matrix_strings(m), "inverse": matrix_strings(inv),
         "scope": "Exact 2x2 counterexample; report supplies the general proof."},
    )

    # Both signs give the same interval for the frozen exact example.
    dx, c, dt = Q(7, 3), Q(5, 2), Q(11, 7)
    forward = dx**2 - c**2 * dt**2
    reversed_interval = dx**2 - c**2 * (-dt)**2
    record(
        "time_sign_invariance_of_squared_interval",
        forward == reversed_interval,
        {"forward": str(forward), "reversed": str(reversed_interval),
         "scope": "Exact example of the algebraic identity (-dt)^2 = dt^2."},
    )

    pa, pb = [[Q(1), Q(0)], [Q(0), Q(0)]], [[Q(0), Q(0)], [Q(0), Q(1)]]
    u_decoupled = [[Q(1), Q(0)], [Q(0), Q(-1)]]
    cross = matmul(matmul(pb, u_decoupled), pa)
    record(
        "block_diagonal_unitary_has_zero_cross_sector_block",
        matmul(transpose(u_decoupled), u_decoupled) == identity(2)
        and cross == [[0, 0], [0, 0]],
        {"cross_sector_block": matrix_strings(cross),
         "scope": "Example; P_beta (U_alpha direct-sum U_beta) P_alpha = 0 generally."},
    )

    # Real orthogonal matrices are also unitary. This is an ordinary sector swap.
    swap = [[Q(0), Q(1)], [Q(1), Q(0)]]
    swapped = matmul(matmul(swap, pa), transpose(swap))
    record(
        "coupled_unitary_can_transfer_sector_population",
        matmul(transpose(swap), swap) == identity(2)
        and swapped == pb and matmul(matmul(pb, swap), pa) != [[0, 0], [0, 0]],
        {"initial_density": matrix_strings(pa), "final_density": matrix_strings(swapped),
         "scope": "State transfer under a non-block-diagonal unitary; no temporal interpretation."},
    )

    g = [[Q(-1), Q(0)], [Q(0), Q(1)]]
    changed_one_sign = identity(2)
    v = [Q(1), Q(1)]
    record(
        "flipping_only_negative_diagonal_entry_removes_lorentzian_signature",
        quadratic(g, v) == 0 and quadratic(changed_one_sign, v) == 2
        and changed_one_sign == identity(2),
        {"before_diagonal": ["-1", "1"], "after_diagonal": ["1", "1"],
         "scope": "Identity form is positive definite; report explains the general diagonal case."},
    )

    neg_g = [[-x for x in row] for row in g]
    record(
        "overall_metric_sign_preserves_nullness",
        quadratic(g, v) == quadratic(neg_g, v) == 0
        and all(quadratic(neg_g, w) == -quadratic(g, w)
                for w in ([Q(2), Q(1)], [Q(1), Q(3)])),
        {"null_vector": ["1", "1"],
         "scope": "Exact examples; g(v,v)=0 iff -g(v,v)=0 algebraically."},
    )

    # |+><+| tensor |0><0|, using the basis 00,01,10,11.
    initial_joint = [[Q(1, 2) if i in (0, 2) and j in (0, 2) else Q(0)
                      for j in range(4)] for i in range(4)]
    cnot = [[Q(1), Q(0), Q(0), Q(0)],
            [Q(0), Q(1), Q(0), Q(0)],
            [Q(0), Q(0), Q(0), Q(1)],
            [Q(0), Q(0), Q(1), Q(0)]]
    final_joint = matmul(matmul(cnot, initial_joint), transpose(cnot))
    reduced = [[sum((final_joint[2*i + e][2*j + e] for e in range(2)), Q(0))
                for j in range(2)] for i in range(2)]
    joint_purity = trace(matmul(final_joint, final_joint))
    reduced_purity = trace(matmul(reduced, reduced))
    record(
        "global_unitarity_does_not_preserve_subsystem_purity",
        matmul(transpose(cnot), cnot) == identity(4)
        and joint_purity == 1 and reduced_purity == Q(1, 2)
        and reduced == [[Q(1, 2), Q(0)], [Q(0), Q(1, 2)]],
        {"joint_purity": str(joint_purity), "reduced_purity": str(reduced_purity),
         "reduced_density": matrix_strings(reduced),
         "scope": "Entanglement with an environment; not a claim of fundamental collapse."},
    )

    expected = {
        "poster-a.jpeg": "26814565f155ab9fe8a592cc0202e150329430095f7ec86e8e055945dd57bfa6",
        "poster-b.jpeg": "47d3e4e77108376720577063a0d937bc5ce361903b72168e39a06d2d4808e526",
    }
    exhibits = []
    for name, digest in expected.items():
        path = Path(__file__).resolve().parent / name
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != digest:
            raise AssertionError("Exhibit hash mismatch: " + name)
        exhibits.append({"file": name, "sha256": actual, "status": "PASS"})

    output = {
        "review": "Bloke parallel qudit sheets, supplied artifacts, 2026-11-01",
        "arithmetic": "Python standard-library Fraction; exact rational",
        "interpretation": "PASS means the referee-report check reproduced, not time travel.",
        "algebra_checks_passed": len(checks),
        "algebra_checks_total": 7,
        "checks": checks,
        "exhibit_checks": exhibits,
        "limitations": [
            "No physical experiment or operational test of temporal access.",
            "No Lean proof, full quantum-field model, or exhaustive novelty search.",
            "No inference about author identity, intentions, or unpublished work.",
        ],
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

