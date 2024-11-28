#!./venv/bin/python
import unittest
from src.get_fitness_cgi_decode import get_fitness_cgi_decode
from src.evaluate_condition import clear_maps


class TestGetFitnessCgiDecode(unittest.TestCase):

    def tearDown(self) -> None:
        clear_maps()
        return super().tearDown()
    
    def test_case_1(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["%AA"]), 2.357142857142857)

    def test_case_2(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["\%AA"]), 1.8571428571428572)

    def test_case_3(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["\%AU"]), 3.03021978021978)

    def test_case_4(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["\%UU"]), 4.53021978021978)

    def test_case_5(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["Hello+Reader"]), 4.972222222222222)

    def test_case_6(self):
        self.assertAlmostEqual(get_fitness_cgi_decode([""]), 8.5)

    def test_case_7(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["\%"]), 5.357142857142858)

    def test_case_8(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["\%1"]), 5.523809523809524)

    def test_case_9(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["+"]), 6.5)

    def test_case_10(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["+\%1"]), 4.666666666666666)

    def test_case_11(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["\%1+"]), 2.9404761904761907)

    def test_case_12(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["\%1+", "%+1", "a+%AA"]), 0)

    def test_case_13(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["%A"]), 6.023809523809524)

    def test_case_14(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["%"]), 5.857142857142858)

    def test_case_15(self):
        self.assertAlmostEqual(get_fitness_cgi_decode(["%A", "%", "\%1+", "%+1", "a+%AA"]), 0)


        