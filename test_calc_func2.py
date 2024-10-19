import unittest
from Calc_file2 import CalcClass

class TestCalc2(unittest.TestCase):
    def setUp(self):
        self.calc_instance = CalcClass()
    def test_calc_func2(self):

        a = 5
        b = 3
        c = 8
        self.assertEqual(self.calc_instance.calc_func(a,b),c)

