"""Independent checks of implementation identities and graph construction."""
import hashlib
import json
from pathlib import Path
import unittest

import numpy as np
import qnet


class QnetTests(unittest.TestCase):
    def test_protocol_unchanged(self):
        self.assertEqual(hashlib.sha256((qnet.ROOT / "PROTOCOL.md").read_bytes()).hexdigest(), qnet.PROTOCOL_HASH)

    def test_all_n4_graph_features_against_matrix_evaluator(self):
        n = 4
        for mask in range(1 << len(qnet.edge_list(n))):
            a = qnet.adjacency_from_edges(n, [edge for bit, edge in enumerate(qnet.edge_list(n)) if mask & (1 << bit)])
            d, m, triangles, _ = qnet.graph_features(n, mask)
            self.assertEqual(d, a.sum(axis=1).tolist())
            self.assertEqual(m, int(a.sum() // 2))
            self.assertEqual(triangles, int(np.trace(np.linalg.matrix_power(a, 3)) // 6))
            for mu in qnet.MU_GRID:
                direct = sum(a.sum(axis=1) * (a.sum(axis=1) - 1)) // 2 - (mu + 1) * a.sum() // 2 + np.trace(a @ a @ a) // 6
                self.assertEqual(qnet.static_energy(d, m, triangles, mu), direct)

    def test_n3_energies_manual(self):
        for mu in qnet.MU_GRID:
            h, *_ = qnet.edge_hamiltonian(3, mu, 0)
            a = mu + 1
            np.testing.assert_array_equal(np.diag(h).real, [0, -a, -a, 1 - 2*a, -a, 1 - 2*a, 1 - 2*a, 4 - 3*a])

    def test_pauli_and_commutators(self):
        h, ns, xs, ys, zs = qnet.edge_hamiltonian(3, 1.7, 0.43)
        for n, x, y, z in zip(ns, xs, ys, zs):
            np.testing.assert_allclose(x @ y - y @ x, 2j * z, atol=1e-14)
            np.testing.assert_allclose(1j * (h @ n - n @ h), 0.43 * y, atol=1e-14)
            np.testing.assert_allclose(n @ n, n, atol=1e-14)

    def test_quantum_diagnostics(self):
        result = qnet.run_quantum()
        self.assertTrue(result["diagnostics"]["passed"])
        for row in result["rows"]:
            self.assertAlmostEqual(sum(row["basis_probabilities_masks_0_through_7"]), 1, places=12)
            self.assertLess(max(row["edge_occupancies"]) - min(row["edge_occupancies"]), 1e-12)

    def test_reference_graphs(self):
        for a in (qnet.cubic_torus(), qnet.circulant(), qnet.disjoint_k66()):
            self.assertEqual(a.shape, (216, 216))
            np.testing.assert_array_equal(a, a.T)
            self.assertEqual(int(np.trace(a)), 0)
            np.testing.assert_array_equal(a.sum(axis=1), [6] * 216)
            self.assertEqual(int(np.trace(a @ a @ a)), 0)
        result = qnet.run_geometry()
        self.assertEqual([r["components"] for r in result["references"]], [1, 1, 18])
        self.assertTrue(result["same_N_degree_triangle_count_and_energy"])
        for row in result["references"]:
            self.assertEqual(row["components"], row["Laplacian_zero_eigenvalue_count_tolerance_1e_minus_8"])
            self.assertAlmostEqual(sum(row["combinatorial_Laplacian_eigenvalues"]), 1296, places=9)

    def test_c8_and_two_c4_ground_bound(self):
        # Supplemental analytic deduction, not an added enumeration grid.
        examples = [[(i, (i+1) % 8) for i in range(8)],
                    [(base+i, base+(i+1) % 4) for base in (0, 4) for i in range(4)]]
        for edges in examples:
            a = qnet.adjacency_from_edges(8, edges)
            d = a.sum(axis=1)
            triangles = int(np.trace(a @ a @ a) // 6)
            self.assertEqual(qnet.static_energy(d.tolist(), int(a.sum()//2), triangles, 2), -16)
            self.assertEqual(0.5 * np.sum((d-2)**2) - 16 + triangles, -16)

    def test_static_ground_histograms(self):
        for mu in qnet.MU_GRID:
            result = qnet.enumerate_static(4, mu)
            count = result["ground_graph_count"]
            self.assertEqual(result["labelled_graphs_enumerated"], 64)
            for key in ("degree_sequence_histogram", "component_size_histogram", "triangle_count_histogram", "joint_structure_histogram"):
                self.assertEqual(sum(row["count"] for row in result[key]), count)
            self.assertEqual(len(set(result["all_ground_graph_masks"])), count)


if __name__ == "__main__":
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(QnetTests)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    report = {"tests_run": result.testsRun, "successful": result.wasSuccessful(),
              "failures": [{"test": str(t), "traceback": tb} for t, tb in result.failures],
              "errors": [{"test": str(t), "traceback": tb} for t, tb in result.errors],
              "skipped": [{"test": str(t), "reason": why} for t, why in result.skipped]}
    output = qnet.ROOT / "results"
    output.mkdir(exist_ok=True)
    (output / "tests.json").write_text(json.dumps(report, indent=2) + "\n")
    raise SystemExit(0 if result.wasSuccessful() else 1)
