#!./venv/bin/python
import unittest
from src.evaluate_condition import evaluate_condition


class TestEvaluateCondition(unittest.TestCase):

    # Operadores

    def test_eq(self):
        self.assertTrue(evaluate_condition(1, 'Eq', 10, 10))
    
    def test_neq(self):
        self.assertTrue(evaluate_condition(2, 'Ne', 'a', 'b'))

    def test_gt(self):
        self.assertTrue(evaluate_condition(3, 'Gt', 'b', 'a'))

    def test_ge(self):
        self.assertTrue(evaluate_condition(4, 'Ge', 'b', 'a'))

    def test_lt(self):
        self.assertTrue(evaluate_condition(5, 'Lt', 'a', 'b'))

    def test_le(self):
        self.assertTrue(evaluate_condition(6, 'Le', 'a', 'b'))

    def test_in(self):
        self.assertTrue(evaluate_condition(7, 'In', "k", {"k": 1, "j": 2}))

    # Caracteres

    def test_eq_char(self):
        self.assertTrue(evaluate_condition(8, 'Eq', 'a', 'a'))

    def test_in_char(self):
        self.assertTrue(evaluate_condition(9, 'In', 'a', {'a': 1, 'b': 2}))

    
    # Lista vacía

    def test_eq_empty_list(self):
        self.assertFalse(evaluate_condition(10, 'In', 'a', {}))

    def test_invalid_operation(self):
        self.assertFalse(evaluate_condition(10, 'In', 'a', {}))

        with self.assertRaises(ValueError):
            evaluate_condition(1, "In", 5, { "5": "b" })

        with self.assertRaises(ValueError):
            evaluate_condition(1, "Eqq", 5, 5)
