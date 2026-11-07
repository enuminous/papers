"""Scientific correctness and leakage controls, not model-success tests."""
import unittest
import numpy as np
from fractions import Fraction as F
import multiscale as m


class SignalChecks(unittest.TestCase):
    def test_direct_rational_reference(self):
        rng = np.random.default_rng(101)
        for n in [6, 7, 20, 41]:
            for _ in range(15):
                e = rng.integers(-3, 4, size=n)
                result = m.before_trial(np.r_[e, 0]).iloc[-1]
                exact = m.exact_features(e)
                for k, v in exact.items():
                    self.assertAlmostEqual(result[k], float(v), places=13)

    def test_constant_signal(self):
        n = 8
        f = m.exact_features([2]*n)
        self.assertEqual(f['local'], 0)
        self.assertEqual(f['haar4'], 0)
        # Zero initialization gives a finite-start transient; do not assert false DC invariance.
        self.assertEqual(f['fast'], 2*(F(1, 2)**n-F(1, 4)**n))
        self.assertEqual(f['slow'], 2*(F(3, 4)**n-F(1, 2)**n))
        for v in m.exact_features([0]*n).values():
            self.assertEqual(v, 0)

    def test_self_mirror_and_local_match(self):
        a, b = (3, 0, -1, 2, 1, 0), (-1, 2, 3, 0, 1, 0)
        f, g = m.exact_features(a), m.exact_features(b)
        self.assertEqual(f, m.exact_features(a))
        for name in ['m', 'Q', 'local', 'local_sq']:
            self.assertEqual(f[name], g[name])
        mirror = m.exact_features([-v for v in a])
        for name in ['m', 'local', 'fast', 'slow', 'haar4']:
            self.assertEqual(mirror[name], -f[name])
        for name in ['Q', 'B', 'local_sq', 'fast_sq', 'slow_sq', 'haar4_sq']+m.A_NAMES:
            self.assertEqual(mirror[name], f[name])

    def test_no_current_or_future_error_leakage(self):
        e = np.linspace(-2, 2, 40)
        a = m.before_trial(e)
        e[17:] = 999
        b = m.before_trial(e)
        np.testing.assert_array_equal(a.iloc[:18], b.iloc[:18])
        self.assertFalse(np.array_equal(a.iloc[18:], b.iloc[18:]))

    def test_block_reset(self):
        a = m.before_trial(np.arange(12.))
        b = m.before_trial(np.arange(12.))
        np.testing.assert_array_equal(a, b)
        np.testing.assert_array_equal(a.iloc[0], 0)
        contaminated = m.before_trial(np.r_[100*np.ones(10), np.arange(12.)]).iloc[10:]
        self.assertFalse(np.array_equal(a.to_numpy(), contaminated.to_numpy()))

    def test_standardization_is_training_only(self):
        import pandas as pd
        tr = pd.DataFrame({'x': [1., 3.]}); te = pd.DataFrame({'x': [5., 101.]})
        x, y = m.augment(np.zeros((2, 1)), np.zeros((2, 1)), tr, te, ['x'])
        np.testing.assert_array_equal(x[:, -1], [-1, 1])
        np.testing.assert_array_equal(y[:, -1], [3, 99])

    def test_haar_normalization(self):
        weights = np.array([-.5, -.5, .5, .5])
        self.assertEqual(float(weights@weights), 1.)
        self.assertEqual(float(weights.sum()), 0.)
        self.assertEqual(m.exact_features([1, 0, 0, 0])['haar4'], F(-1, 2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
