from random import choice
from string import printable
from typing import List


def get_random_character():
    return choice(printable)


def create_test_case() -> str:
    length = choice(range(0, 11))
    return ''.join(get_random_character() for _ in range(length))


def create_individual() -> List[str]:
    num_cases = choice(range(1, 16))
    return [create_test_case() for _ in range(num_cases)]


def create_population(population_size) -> List[List[str]]:
    population = [create_individual() for _ in range(population_size)]
    return population
