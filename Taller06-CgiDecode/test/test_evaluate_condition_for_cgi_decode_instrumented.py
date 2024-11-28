#!./venv/bin/python
import unittest
from src.cgi_decode import cgi_decode
from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import clear_maps, get_true_distance, get_false_distance


class TestEvaluateConditionForCgiDecodeInstrumented(unittest.TestCase):

    def test_example(self):
        clear_maps()
        result = cgi_decode_instrumented("Hello+World")

        self.assertEqual(get_true_distance(1), 0)
        self.assertEqual(get_true_distance(2), 0)
        self.assertEqual(get_true_distance(3), 35)

        self.assertEqual(get_false_distance(1), 0)
        self.assertEqual(get_false_distance(2), 0)
        self.assertEqual(get_false_distance(3), 0)

        self.assertEqual(result, "Hello World")

    def test_not_c1(self):
        clear_maps()
        result = cgi_decode_instrumented("")

        self.assertEqual(get_true_distance(1), 1)
        self.assertEqual(get_false_distance(1), 0)

        self.assertEqual(result, "")

    def test_not_eq(self):
        clear_maps()
        result = cgi_decode_instrumented("a")

        self.assertEqual(get_true_distance(2), 54)
        self.assertEqual(get_false_distance(2), 0)

        self.assertEqual(result, "a")

    def test_eq(self):
        clear_maps()
        result = cgi_decode_instrumented("+")

        self.assertEqual(get_true_distance(2), 0)
        self.assertEqual(get_false_distance(2), 1)

        self.assertEqual(result, " ")

    def test_in(self):
        clear_maps()
        result = cgi_decode_instrumented("%41")

        self.assertEqual(get_true_distance(3), 0)
        self.assertEqual(get_false_distance(3), 1)

        self.assertEqual(result, "A")

    def test_not_in(self):
        clear_maps()
        with self.assertRaises(ValueError):
            cgi_decode_instrumented("%4x")

        self.assertEqual(get_true_distance(4), 0)
        self.assertEqual(get_false_distance(4), 0)



        