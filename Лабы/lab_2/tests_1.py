import unittest
import numpy as np
from task_1 import f, simpsons_rule, runge_error


class TestFunctions(unittest.TestCase):

    def test_f_valid_range(self):
        self.assertAlmostEqual(f(0), 0, places=5)
        self.assertAlmostEqual(f(1), np.sin(2) / (0.4 + np.cos(1)), places=5)
        self.assertAlmostEqual(f(-1), np.sin(0) / (0.4 + np.cos(1)), places=5)

    def test_f_out_of_range(self):
        with self.assertRaises(AssertionError):
            f(2)
        with self.assertRaises(AssertionError):
            f(-2)

    def test_simpsons_rule(self):
        def quadratic(x):
            return x ** 2

        expected_value = 1 / 3
        result = simpsons_rule(quadratic, 0, 1, 10)
        self.assertAlmostEqual(result, expected_value, places=5)

    def test_simpsons_rule_invalid_n(self):
        def test_func(x):
            return x ** 2

        with self.assertRaises(ZeroDivisionError):
            simpsons_rule(test_func, 0, 1, 0)

    def test_runge_error(self):
        In = 1.0
        I2n = 1.1
        expected_error = abs(1.1 - 1.0) / (2 ** 4 - 1)
        result = runge_error(I2n, In)
        self.assertAlmostEqual(result, expected_error, places=5)

    def test_runge_error_zero_difference(self):
        In = 1.0
        I2n = 1.0
        result = runge_error(I2n, In)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()


