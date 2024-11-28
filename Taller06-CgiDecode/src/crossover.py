from random import randint
from typing import List, Tuple


def crossover(parent1: List[str], parent2: List[str]) -> Tuple[List[str], List[str]]:

    mid = len(parent1) // 2

    offspring1 = parent1[:mid] + parent2[mid:]
    offspring2 = parent2[:mid] + parent1[mid:]

    return offspring1, offspring2
