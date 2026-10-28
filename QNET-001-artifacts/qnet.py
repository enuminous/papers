#!/usr/bin/env python3
"""QNET-001: exact bounded tests of a postulated dynamical-edge Hamiltonian.

Only Python stdlib and NumPy. See frozen PROTOCOL.md for scope and limitations.
Bit e=0 means absent edge, bit e=1 means present; edges are lexicographic.
"""
from __future__ import annotations

import argparse
from collections import Counter, deque
from datetime import datetime, timezone
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
import platform
import sys

import numpy as np

ROOT = Path(__file__).resolve().parent
MU_GRID = (0, 1, 2, 4)
STATIC_NS = (4, 5, 6)
PROTOCOL_HASH = "fc264efee375c6509fab46a00c8907e0b48856e51843f4330558508939116ec3"


def edge_list(n):
    return list(combinations(range(n), 2))


def graph_features(n, mask):
    """Exact integer graph features, using adjacency bitsets."""
    adjacency = [0] * n
    degrees = [0] * n
    edges = edge_list(n)
    for bit, (i, j) in enumerate(edges):
        if mask & (1 << bit):
            adjacency[i] |= 1 << j
            adjacency[j] |= 1 << i
            degrees[i] += 1
            degrees[j] += 1
    triangle_triple_count = sum(
        (adjacency[i] & adjacency[j]).bit_count()
        for i, j in edges if adjacency[i] & (1 << j)
    )
    assert triangle_triple_count % 3 == 0
    triangles = triangle_triple_count // 3
    return degrees, mask.bit_count(), triangles, adjacency


def component_sizes(adjacency):
    unseen = set(range(len(adjacency)))
    sizes = []
    while unseen:
        root = min(unseen)
        unseen.remove(root)
        stack = [root]
        size = 0
        while stack:
            u = stack.pop()
            size += 1
            neighbours = [v for v in unseen if adjacency[u] & (1 << v)]
            unseen.difference_update(neighbours)
            stack.extend(neighbours)
        sizes.append(size)
    return sorted(sizes, reverse=True)


def static_energy(degrees, edges, triangles, mu, U=1, V=1, J=1):
    return U * sum(d * (d - 1) // 2 for d in degrees) - (mu + J) * edges + V * triangles


def counter_records(counter, field):
    return [{field: list(k) if isinstance(k, tuple) else k, "count": v}
            for k, v in sorted(counter.items())]


def enumerate_static(n, mu):
    minimum = None
    ground_masks = []
    graph_count = 1 << len(edge_list(n))
    for mask in range(graph_count):
        d, m, t, _ = graph_features(n, mask)
        e = static_energy(d, m, t, mu)
        if minimum is None or e < minimum:
            minimum, ground_masks = e, [mask]
        elif e == minimum:
            ground_masks.append(mask)
    degree_hist, component_hist, triangle_hist, joint_hist = (Counter() for _ in range(4))
    connected_count = 0
    for mask in ground_masks:
        d, _, t, a = graph_features(n, mask)
        components = tuple(component_sizes(a))
        degrees = tuple(sorted(d))
        degree_hist[degrees] += 1
        component_hist[components] += 1
        triangle_hist[t] += 1
        joint_hist[(degrees, components, t)] += 1
        connected_count += int(len(components) == 1)
    return {
        "N": n, "mu": mu, "g": 0, "U": 1, "V": 1, "J": 1,
        "labelled_graphs_enumerated": graph_count,
        "minimum_energy": minimum,
        "ground_graph_count": len(ground_masks),
        "connected_ground_graph_count": connected_count,
        "connected_fraction": connected_count / len(ground_masks),
        "connected_fraction_exact": f"{connected_count}/{len(ground_masks)}",
        "degree_sequence_histogram": counter_records(degree_hist, "sorted_degrees"),
        "component_size_histogram": counter_records(component_hist, "component_sizes_descending"),
        "triangle_count_histogram": counter_records(triangle_hist, "triangles"),
        "joint_structure_histogram": [
            {"sorted_degrees": list(d), "component_sizes_descending": list(c),
             "triangles": t, "count": count}
            for (d, c, t), count in sorted(joint_hist.items())
        ],
        "all_ground_graph_masks": ground_masks,
        "mask_encoding": "bit e corresponds to edge list entry e, least-significant bit first",
        "edge_list": edge_list(n),
    }


def edge_operators(n):
    m = len(edge_list(n))
    dim = 1 << m
    ns, xs, ys, zs = [], [], [], []
    for e in range(m):
        ns.append(np.diag([float((state >> e) & 1) for state in range(dim)]))
        x = np.zeros((dim, dim), dtype=complex)
        y = np.zeros_like(x)
        for state in range(dim):
            flipped = state ^ (1 << e)
            x[flipped, state] = 1
            y[flipped, state] = -1j if state & (1 << e) else 1j
        xs.append(x)
        ys.append(y)
        zs.append(np.eye(dim) - 2 * ns[-1])
    return ns, xs, ys, zs


def edge_hamiltonian(n, mu, g, U=1, V=1, J=1):
    dim = 1 << len(edge_list(n))
    diagonal = []
    for state in range(dim):
        d, m, t, _ = graph_features(n, state)
        diagonal.append(static_energy(d, m, t, mu, U, V, J))
    ns, xs, ys, zs = edge_operators(n)
    h = np.diag(diagonal).astype(complex) - g * sum(xs, start=np.zeros((dim, dim), complex))
    return h, ns, xs, ys, zs


def expected(psi, operator):
    value = np.vdot(psi, operator @ psi)
    if abs(value.imag) > 1e-12:
        raise ValueError(f"Unexpected imaginary expectation: {value}")
    return float(value.real)


def run_quantum():
    n, mu, g = 3, 1, 0.25
    h, ns, xs, ys, zs = edge_hamiltonian(n, mu, g)
    values, vectors = np.linalg.eigh(h)
    initial = np.zeros(len(h), complex)
    initial[0] = 1
    coefficients = vectors.conj().T @ initial

    def state_at(t):
        return vectors @ (np.exp(-1j * values * t) * coefficients)

    initial_energy = expected(initial, h)
    max_commutator_error = max(float(np.max(np.abs(1j * (h @ op - op @ h) - g * y)))
                               for op, y in zip(ns, ys))
    rows = []
    for t in np.linspace(0, 4, 9):
        psi = state_at(t)
        derivative = -1j * h @ psi
        occupation_derivatives = [float(2 * np.vdot(derivative, op @ psi).real) for op in ns]
        y_expectations = [expected(psi, y) for y in ys]
        rows.append({
            "time": float(t), "norm_squared": float(np.vdot(psi, psi).real),
            "energy": expected(psi, h),
            "edge_occupancies": [expected(psi, op) for op in ns],
            "edge_Y_expectations": y_expectations,
            "occupation_derivatives_from_state": occupation_derivatives,
            "g_times_Y": [g * y for y in y_expectations],
            "basis_probabilities_masks_0_through_7": [float(p) for p in np.abs(psi) ** 2],
        })
    t, epsilon = 0.7, 1e-5
    finite_differences = [(expected(state_at(t + epsilon), op) - expected(state_at(t - epsilon), op)) /
                          (2 * epsilon) for op in ns]
    rhs = [g * expected(state_at(t), y) for y in ys]
    diagnostics = {
        "max_Hermiticity_error": float(np.max(np.abs(h - h.conj().T))),
        "max_norm_squared_error": max(abs(row["norm_squared"] - 1) for row in rows),
        "max_energy_drift": max(abs(row["energy"] - initial_energy) for row in rows),
        "max_commutator_error": max_commutator_error,
        "max_dndt_identity_error": max(abs(a - b) for row in rows for a, b in
                                       zip(row["occupation_derivatives_from_state"], row["g_times_Y"])),
        "finite_difference_time": t,
        "finite_difference_step": epsilon,
        "finite_difference_dndt": finite_differences,
        "finite_difference_g_times_Y": rhs,
        "max_finite_difference_error": max(abs(a - b) for a, b in zip(finite_differences, rhs)),
    }
    diagnostics["passed"] = all(diagnostics[key] <= 1e-12 for key in (
        "max_Hermiticity_error", "max_norm_squared_error", "max_energy_drift",
        "max_commutator_error", "max_dndt_identity_error")) and diagnostics["max_finite_difference_error"] <= 1e-9
    return {
        "N": n, "edge_hilbert_dimension": len(h), "mu": mu, "g": g, "hbar": 1,
        "U": 1, "V": 1, "J": 1, "initial_edge_state": "empty graph, mask 0",
        "matter_sector": "all factors identical; exactly invariant, not full matter Hilbert simulation",
        "edge_list": edge_list(n), "Hamiltonian_real": h.real.tolist(),
        "energy_eigenvalues": values.tolist(), "rows": rows, "diagnostics": diagnostics,
    }


def adjacency_from_edges(n, edges):
    a = np.zeros((n, n), dtype=np.int64)
    for i, j in edges:
        assert i != j
        a[i, j] = a[j, i] = 1
    return a


def cubic_torus(side=6):
    n = side ** 3
    edges = set()
    index = lambda x, y, z: (x * side + y) * side + z
    for x in range(side):
        for y in range(side):
            for z in range(side):
                i = index(x, y, z)
                for xyz in (((x + 1) % side, y, z), (x, (y + 1) % side, z), (x, y, (z + 1) % side)):
                    edges.add(tuple(sorted((i, index(*xyz)))))
    return adjacency_from_edges(n, edges)


def circulant(n=216, offsets=(1, 3, 5)):
    return adjacency_from_edges(n, {(i, (i + offset) % n) for i in range(n) for offset in offsets})


def disjoint_k66(copies=18):
    edges = [(12 * c + i, 12 * c + j) for c in range(copies) for i in range(6) for j in range(6, 12)]
    return adjacency_from_edges(12 * copies, edges)


def all_distances(adjacency):
    neighbours = [np.flatnonzero(row).tolist() for row in adjacency]
    n = len(adjacency)
    distances = np.full((n, n), -1, dtype=int)
    for root in range(n):
        distances[root, root] = 0
        queue = deque([root])
        while queue:
            u = queue.popleft()
            for v in neighbours[u]:
                if distances[root, v] == -1:
                    distances[root, v] = distances[root, u] + 1
                    queue.append(v)
    return distances


def clustered_spectrum(eigenvalues, tolerance=1e-8):
    groups = []
    for value in eigenvalues:
        clean = 0.0 if abs(value) < tolerance else float(value)
        if groups and abs(clean - groups[-1]["eigenvalue"]) <= tolerance:
            groups[-1]["multiplicity"] += 1
        else:
            groups.append({"eigenvalue": clean, "multiplicity": 1})
    return groups


def graph_diagnostic(name, adjacency):
    n = len(adjacency)
    degrees = adjacency.sum(axis=1)
    edges = int(degrees.sum() // 2)
    triangles = int(np.trace(adjacency @ adjacency @ adjacency) // 6)
    distances = all_distances(adjacency)
    finite_nonzero = distances[distances > 0]
    bit_adjacency = [sum(1 << int(j) for j in np.flatnonzero(row)) for row in adjacency]
    sizes = component_sizes(bit_adjacency)
    laplacian = np.diag(degrees) - adjacency
    eigenvalues = np.linalg.eigvalsh(laplacian.astype(float))
    shell_hist = Counter(int(d) for d in distances[0] if d >= 0)
    shells = [{"radius": radius, "shell_vertices": shell_hist[radius],
               "ball_vertices_including_root": sum(shell_hist[r] for r in range(radius + 1))}
              for radius in range(max(shell_hist) + 1)]
    energies = {str(mu): int(static_energy(degrees.tolist(), edges, triangles, mu)) for mu in MU_GRID}
    return {
        "name": name, "N": n, "edges": edges, "degree_histogram": counter_records(Counter(int(d) for d in degrees), "degree"),
        "triangles": triangles, "components": len(sizes), "component_sizes_descending": sizes,
        "connected": len(sizes) == 1,
        "finite_within_component_diameter": int(distances.max()),
        "whole_graph_diameter": int(distances.max()) if len(sizes) == 1 else None,
        "whole_graph_diameter_note": "null denotes disconnected graph with infinite extended distance",
        "mean_finite_nonself_pair_distance": float(finite_nonzero.mean()),
        "finite_ordered_nonself_pairs": int(len(finite_nonzero)),
        "distance_growth_from_vertex_0": shells,
        "unreachable_from_vertex_0": int(np.sum(distances[0] < 0)),
        "combinatorial_Laplacian_eigenvalues": eigenvalues.tolist(),
        "Laplacian_spectrum_grouped_tolerance_1e_minus_8": clustered_spectrum(eigenvalues),
        "Laplacian_zero_eigenvalue_count_tolerance_1e_minus_8": int(np.sum(np.abs(eigenvalues) <= 1e-8)),
        "algebraic_connectivity": float(eigenvalues[1]) if eigenvalues[1] > 1e-8 else 0.0,
        "static_energies_by_mu": energies,
        "role": "constructed diagnostic reference, NOT emergent output or prescribed simulation initial state",
    }


def run_geometry():
    references = [graph_diagnostic("6x6x6 cubic periodic nearest-neighbour graph", cubic_torus()),
                  graph_diagnostic("circulant C216 offsets +/-1,+/-3,+/-5", circulant()),
                  graph_diagnostic("18 disjoint copies of K6,6", disjoint_k66())]
    assert all(row["N"] == 216 and row["triangles"] == 0 and
               row["degree_histogram"] == [{"degree": 6, "count": 216}] for row in references)
    assert all(row["static_energies_by_mu"] == references[0]["static_energies_by_mu"] for row in references)
    return {"references": references, "same_N_degree_triangle_count_and_energy": True,
            "dimension_estimated": False,
            "conclusion_scope": "The static regular triangle-free energy does not distinguish these geometries. These references are not claimed ground states."}


def run_all(output_directory):
    protocol = (ROOT / "PROTOCOL.md").read_bytes()
    assert sha256(protocol).hexdigest() == PROTOCOL_HASH, "Frozen protocol has changed"
    output_directory.mkdir(parents=True, exist_ok=True)
    results = {
        "static": {"scope": "aligned matter, g=0, exact labelled-graph enumeration", "results": [
            enumerate_static(n, mu) for n in STATIC_NS for mu in MU_GRID]},
        "quantum": run_quantum(),
        "geometry": run_geometry(),
        "q_null": {"q_values": [887, 888, 889], "method": "exact analytic sector restriction, not numerical full-q simulation",
                   "identity": "S_ij |phi>^tensorN = |phi>^tensorN for every q>=1",
                   "reduced_edge_H_independent_of_q": True,
                   "scope": "aligned-matter sector; full-ground-energy theorem is separately proved in README"},
    }
    assert results["quantum"]["diagnostics"]["passed"]
    manifest = {"protocol_sha256": PROTOCOL_HASH, "source_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
                "completed_at_UTC": datetime.now(timezone.utc).isoformat(), "python": sys.version,
                "numpy": np.__version__, "platform": platform.platform(), "files": {}}
    for name, result in results.items():
        path = output_directory / f"{name}.json"
        path.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
        manifest["files"][path.name] = sha256(path.read_bytes()).hexdigest()
    (output_directory / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"output_directory": str(output_directory), "protocol_sha256": PROTOCOL_HASH,
                      "quantum_checks": results["quantum"]["diagnostics"],
                      "static_summary": [{key: row[key] for key in ("N", "mu", "minimum_energy", "ground_graph_count", "connected_ground_graph_count")}
                                         for row in results["static"]["results"]],
                      "geometry_summary": [{key: row[key] for key in ("name", "edges", "triangles", "components", "finite_within_component_diameter", "algebraic_connectivity")}
                                           for row in results["geometry"]["references"]]}, indent=2))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "results")
    args = parser.parse_args()
    run_all(args.output)
