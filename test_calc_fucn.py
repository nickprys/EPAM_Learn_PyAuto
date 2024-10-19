import unittest
from Calc_file import calc_func

class TestFunc(unittest.TestCase):
    def test_calc_func(self):
        a = 2
        b = 3
        c = 5
        self.assertEqual(calc_func(a, b), c)