#!./venv/bin/python
import unittest

from random import seed
from src.genetic_algorithm import GeneticAlgorithm


class TestGeneticAlgorithm(unittest.TestCase):
    def test1(self):
        seed(1)
        ga = GeneticAlgorithm()
        result = ga.run()

        # Cantidad de generaciones realizada
        self.assertEquals(ga.get_generation(), 1000)

        # El branch coverage logrado al final del algoritmo por el mejor individuo
        self.assertAlmostEquals(result, 1.0)


    def test2(self):
        seed(2)
        ga = GeneticAlgorithm()
        result = ga.run()

        # Cantidad de generaciones realizada
        self.assertEquals(ga.get_generation(), 1000)

        # El branch coverage logrado al final del algoritmo por el mejor individuo
        self.assertAlmostEquals(result, 1.0)

    def test3(self):
        seed(3)
        ga = GeneticAlgorithm()
        result = ga.run()

        # Cantidad de generaciones realizada
        self.assertEquals(ga.get_generation(), 1000)

        # El branch coverage logrado al final del algoritmo por el mejor individuo
        self.assertAlmostEquals(result, 1.0)




