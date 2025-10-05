
import unittest
from simple_calculator import SimpleCalculator
class SimpleCalculator(unittest.TestCase):
     def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        
def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(4, 3), 1)
        self.assertEqual(self.calc.subtract(5, 1), 4)
  
def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()
        
def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 1), -1)    

def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

def test_division(self):
        """Test the addition method."""
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(4, 2), 2)    
               
# Division by zero should return None
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

        # Division with floats
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

if __name__ == "__main__":
    unittest.main()        
