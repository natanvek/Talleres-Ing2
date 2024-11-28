from typing import List

from src.get_fitness_cgi_decode import get_fitness_cgi_decode

def evaluate_population(population: List[List[str]]) -> dict:
    fitness = {}

    for idx, individual in enumerate(population):
        fitness[idx] = get_fitness_cgi_decode(individual)

    return fitness
