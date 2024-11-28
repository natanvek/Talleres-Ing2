from random import randint
from typing import List, Tuple


def crossover(parent1: List[str], parent2: List[str]) -> Tuple[List[str], List[str]]:
    # considerando que a el tamaño de los hijos es variable, tomamos un punto fijo aleatorio
    # del hijo de menor tamaño y hacemos el crossover en el punto fijo 
    point = randint(1, min(len(parent1), len(parent2)))

    offspring1 = parent1[:point] + parent2[point:]
    offspring2 = parent2[:point] + parent1[point:]

    return offspring1, offspring2
