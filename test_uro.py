import unittest
from uro import wrap

class TestUro(unittest.TestCase):
    def test_obliczenie(self):
        self.assertEqual(wrap(1,3,1),32)
        self.assertEqual(wrap(13,13,13),124)
        self.assertEqual(wrap(17,32,11),162)
    def test_type(self):
        self.assertEqual(wrap(1,'3',1),TypeError)
     

if __name__ == '__main__':
    unittest.main()
