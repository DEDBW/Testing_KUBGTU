import unittest
from task_2 import factorial, sum_of_factorials, INT32_MAX


class TestFactorialFunctions(unittest.TestCase):

    def test_factorial_base_cases(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_recursive_cases(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_sum_of_factorials_small_limit(self):
        self.assertEqual(sum_of_factorials(1), 1)
        self.assertEqual(sum_of_factorials(2), 3)
        self.assertEqual(sum_of_factorials(3), 9)

    def test_sum_of_factorials_large(self):
        result = sum_of_factorials(10)
        self.assertTrue(result < INT32_MAX)

    def test_sum_of_factorials_overflow(self):
        result = sum_of_factorials(20)
        self.assertIsInstance(result, AssertionError)

    def test_sum_of_factorials_zero(self):
        self.assertEqual(sum_of_factorials(0), 0)


if __name__ == '__main__':
    unittest.main()
