import unittest
from zad2 import Employee

class TestZad2(unittest.TestCase):
    def setUp(self):
        self.p1 = Employee("Julia", "Sidor", 31,10000)
        self.p2 = Employee("Ola","Olszewska", 17, 8000)
    def test_introduce_self(self):
        self.assertEqual(self.p1.introduce_self(), f'My name is Julia Sidor and I am 31 years old')
        self.assertEqual(self.p2.introduce_self(), f'My name is Ola Olszewska and I am 17 years old')
    def test_raise_salary(self):
        ratio = 2
        self.assertEqual(self.p1.salary * ratio, 10000 * 2)
        self.assertEqual(self.p2.salary * ratio, 8000 * 2)
    def test_check_age(self):
        self.assertEqual(self.p1.check_age(), "Adult employee")
        self.assertEqual(self.p2.check_age(), "Underage employee")
    def test_get_email(self):
        self.assertEqual(self.p1.get_email(), "JuliaSidor@company.com")
        self.assertEqual(self.p2.get_email(), "OlaOlszewska@company.com")

if __name__ == '__main__':
    unittest.main()