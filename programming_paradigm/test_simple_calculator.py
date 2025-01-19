import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def test_add(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.add(5, 3), 8)

    def test_subtract(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.subtract(5, 3), 2)

    def test_multiply(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.multiply(5, 3), 15)

    def test_divide(self):
        calculator = SimpleCalculator()
        self.assertEqual(calculator.divide(9, 3), 3)
        
    def test_divide_by_zero_returns_none(self):
        calculator = SimpleCalculator()
        result = calculator.divide(10, 0)
        self.assertIsNone(result)    

if __name__ == '__main__':
    unittest.main()