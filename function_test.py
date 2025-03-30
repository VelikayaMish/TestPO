import unittest
from function import quadratic_function
import cmath

class TestSolve(unittest.TestCase):
    
    def test_standard_cases(self):
        self.assertEqual(solve_quadratic(1, -3, 2), (2, 1))
        self.assertEqual(solve_quadratic(1, 2, 1), (-1, -1))
        self.assertEqual(solve_quadratic(1, 0, -4), (2, -2))

    def test_complex_roots(self):
        self.assertEqual(solve_quadratic(1, 2, 5), (-1 + 2j, -1 - 2j))

    def test_zero_coefficient_a(self):
        with self.assertRaises(ValueError):
            solve_quadratic(0, 2, 1)

    def test_negative_discriminant(self):
        self.assertEqual(solve_quadratic(1, 0, 1), (0 + 1j, 0 - 1j))

if __name__ == '__main__':
    unittest.main()
