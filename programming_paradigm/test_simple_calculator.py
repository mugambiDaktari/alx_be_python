import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the test environment by creating an instance of SimpleCalculator."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-2, 4), 2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtraction(self):
        """Test the addition method."""
        self.assertEqual(self.calc.subtract(5, 3), 5)

    def test_multiplication(self):
        """Test the addition method."""
        self.assertEqual(self.calc.multiply(5, 3), 15)    

    def test_divide_by_zero_returns_none(self):
        """Test that division by zero returns None."""
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)  # Check if the result is None

    def test_divide_normal(self):
        """Test normal division."""
        self.assertEqual(self.calc.divide(10, 2), 5)

if __name__ == '__main__':
    unittest.main()