from random import random
from typing import List

from src.create_population import create_population
from src.crossover import crossover
from src.evaluate_population import evaluate_population
from src.mutate import mutate
from src.selection import selection

class GeneticAlgorithm():
    def __init__(self):
        self.population_size = 100
        self.tournament_size = 5
        self.p_crossover = 0.70
        self.p_mutation = 0.20

        self.generation = 0
        self.best_individual = None
        self.fitness_best_individual = None

    def get_best_individual(self):
        return self.best_individual
    
    def get_fitness_best_individual(self):
        return self.fitness_best_individual
    
    def get_generation(self):
        return self.generation

    def generate_crossovers(self, population: List[List[str]], fitness_by_individual: dict) -> List[List[str]]:

        crossovers = []

        while len(crossovers) < self.population_size:
            parent_1_idx, _ = selection(fitness_by_individual, self.tournament_size)
            parent_2_idx, _ = selection(fitness_by_individual, self.tournament_size)

            if random() < self.p_crossover:
                child_1, child_2 = crossover(population[parent_1_idx], population[parent_2_idx])
                crossovers.append(child_1)
                crossovers.append(child_2)
            else:
                crossovers.append(population[parent_1_idx])
                crossovers.append(population[parent_2_idx])

        return crossovers

    def generate_mutations(self, population: List[List[str]]) -> List[List[str]]:

        mutations = []

        for individual in population:
            if random() < self.p_mutation:
                mutations.append(mutate(individual))
            else:
                mutations.append(individual)

        return mutations

    def covered_all_branches(self, fitness_individual: float) -> bool:
        # return abs(fitness_individual) < 1e-9
        return fitness_individual == 0

    def run(self):
        # Generar y evaluar la poblacion inicial
        population = create_population(self.population_size)
        fitness_by_individual = evaluate_population(population)

        # Imprimir el mejor valor de fitness encontrado
        self.best_individual = max(fitness_by_individual, key = lambda x: fitness_by_individual[x])
        self.fitness_best_individual = fitness_by_individual[self.best_individual]
        print(self.fitness_best_individual)

        # Continuar mientras la cantidad de generaciones es menor que 1000
        # y no haya ningun individuo que cubra todos los objetivos

        while self.generation < 1000 and not self.covered_all_branches(self.fitness_best_individual):

            # Producir una nueva poblacion en base a la anterior.
            # Usar selection, crossover y mutation.
            crossovers = self.generate_crossovers(population, fitness_by_individual)
            new_population = self.generate_mutations(crossovers)

            # Una vez creada, reemplazar la poblacion anterior con la nueva
            self.generation += 1
            population = new_population

            # Evaluar la nueva poblacion e imprimir el mejor valor de fitness
            fitness_by_individual = evaluate_population(population)
            self.best_individual = max(fitness_by_individual, key = lambda x: fitness_by_individual[x])
            self.fitness_best_individual = fitness_by_individual[self.best_individual]

        # retornar el mejor individuo de la ultima generacion
        return self.best_individual