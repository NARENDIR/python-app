import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        result = self.calculator.add(3, 7)
        self.assertEqual(result, 10)

    def test_subtract(self):
        result = self.calculator.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiply(self):
        result = self.calculator.multiply(4, 6)
        self.assertEqual(result, 24)

    def test_divide(self):
        result = self.calculator.divide(8, 4)
        self.assertEqual(result, 2)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.divide(10, 0)

if __name__ == '__main__':
    unittest.main()

