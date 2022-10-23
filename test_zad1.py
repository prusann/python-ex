import unittest
from zad1 import add,subtract, multiply, divide, is_numberic

class TestZad1(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(12,2),14)
        self.assertEqual(add(12,-2),10)
        self.assertEqual(add(-12,-2),-14)
    def test_subtract(self):
        self.assertEqual(subtract(12,2),10)
        self.assertEqual(subtract(12,-2),14)
        self.assertEqual(subtract(-12,-2),-10)
    def test_multiply(self):
        self.assertEqual(multiply(12,2),24)
        self.assertEqual(multiply(12,-2),-24)
        self.assertEqual(multiply(-12,-2),24)
    def test_divide(self):
        self.assertEqual(divide(12,2),6)
        self.assertEqual(divide(12,-2),-6)
        self.assertEqual(divide(-12,-2),6)
        with self.assertRaises(ValueError):
            divide(7, 0)
    def test_is_numeric(self):
        with self.assertRaisesRegex(ValueError, "Bad type of arguments"):
            is_numberic(10, "5")

                
if __name__ == '__main__':
    unittest.main()