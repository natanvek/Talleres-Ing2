#!./venv/bin/python
import unittest

from random import seed
from src.genetic_algorithm import GeneticAlgorithm
from src.cgi_decode_instrumented import cgi_decode_instrumented
from src.evaluate_condition import clear_maps, get_false_distance, get_true_distance

def branch_coverage(best_individual):
    clear_maps()

    for test in best_individual:
        try:
            cgi_decode_instrumented(test)
        except Exception as _:
            pass

    branches_covered = 0
    for c_num in range(1, 6):
        branches_covered += (get_true_distance(c_num) == 0) + (get_false_distance(c_num) == 0)

    return branches_covered / 10


class TestGeneticAlgorithm(unittest.TestCase):
    def test1(self):
        seed(1)
        ga = GeneticAlgorithm()
        result = ga.run()

        # Cantidad de generaciones realizada
        self.assertEqual(ga.get_generation(), 3)
        self.assertAlmostEqual(branch_coverage(result), 1.0)

        # El branch coverage logrado al final del algoritmo por el mejor individuo

        


    def test2(self):
        seed(2)
        ga = GeneticAlgorithm()
        result = ga.run()

        # Cantidad de generaciones realizada
        self.assertEqual(ga.get_generation(), 4)
        self.assertAlmostEqual(branch_coverage(result), 1.0)

        
        # El branch coverage logrado al final del algoritmo por el mejor individuo
        # self.assertAlmostEqual(result, 1.0)

    def test3(self):
        seed(3)
        ga = GeneticAlgorithm()
        result = ga.run()

        # Cantidad de generaciones realizada
        self.assertEqual(ga.get_generation(), 3)
        self.assertAlmostEqual(branch_coverage(result), 1.0)

        # El branch coverage logrado al final del algoritmo por el mejor individuo
        # self.assertAlmostEqual(result, 1.0)




