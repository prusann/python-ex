import unittest

from zad3 import is_numeric, is_negative, calculate_savings


class TestDef(unittest.TestCase):

    def test_is_numeric(self):
        self.assertEqual(is_numeric(1), True)
        self.assertEqual(is_numeric("1"), False)

    def test_is_negative(self):        
        self.assertEqual(is_negative(1), False)
        self.assertEqual(is_negative(-1), True)

    def test_calculate_savings(self):
        dane = calculate_savings(100, 12, 20)

        self.assertEqual(dane, 100 + 12 * (12 - 20))
        with self.assertRaisesRegex(ValueError, "All arguments must be positive numbers."):
            calculate_savings(100, 10, -1)
        with self.assertRaisesRegex(ValueError, "All arguments must be numeric."):
            calculate_savings(100, 12, '1')


if __name__ == '__main__':
    unittest.main()
