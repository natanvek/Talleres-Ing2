#!./venv/bin/python
import unittest
from src.evaluate_condition import evaluate_condition


class TestEvaluateCondition(unittest.TestCase):

    # Evaluamos la rama True y la rama False de cada operador programado en evaluate_conditions.py
    def test_eq(self):
        self.assertTrue(evaluate_condition(1, 'Eq', 10, 10))
        self.assertFalse(evaluate_condition(1, 'Eq', 3, 10))

    
    def test_neq(self):
        self.assertTrue(evaluate_condition(2, 'Ne', 'a', 'b'))
        self.assertFalse(evaluate_condition(2, 'Ne', 'a', 'a'))

    def test_gt(self):
        self.assertTrue(evaluate_condition(3, 'Gt', 'b', 'a'))
        self.assertFalse(evaluate_condition(3, 'Gt', 'b', 'c'))

    def test_ge(self):
        self.assertTrue(evaluate_condition(4, 'Ge', 'b', 'a'))
        self.assertFalse(evaluate_condition(4, 'Ge', 'b', 'c'))

    def test_lt(self):
        self.assertTrue(evaluate_condition(5, 'Lt', 'a', 'b'))
        self.assertFalse(evaluate_condition(5, 'Lt', 'c', 'b'))

    def test_le(self):
        self.assertTrue(evaluate_condition(6, 'Le', 'a', 'b'))
        self.assertFalse(evaluate_condition(6, 'Le', 'c', 'b'))

    def test_in(self):
        self.assertTrue(evaluate_condition(7, 'In', "k", {"k": 1, "j": 2}))

    def test_in_char(self):
        self.assertTrue(evaluate_condition(9, 'In', 'a', {'a': 1, 'b': 2}))


    def test_eq_empty_list(self):
        self.assertFalse(evaluate_condition(10, 'In', 'a', {}))

    def test_invalid_operation(self):
        self.assertFalse(evaluate_condition(10, 'In', 'a', {}))

        with self.assertRaises(ValueError):
            evaluate_condition(1, "In", 5, { "5": "b" })

        with self.assertRaises(ValueError):
            evaluate_condition(1, "Eqq", 5, 5)
