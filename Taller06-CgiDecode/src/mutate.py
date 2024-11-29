from random import choice
from typing import List

from src.create_population import create_test_case, get_random_character


def add_character(test_case: str) -> str:

    position = choice(range(len(test_case) + 1))
    character = get_random_character()

    test_case = test_case[:position] + character + test_case[position:]

    return test_case


def remove_character(test_case: str) -> str:

    position = choice(range(len(test_case)))

    test_case = test_case[:position] + test_case[position + 1:]

    return test_case


def modify_character(test_case: str) -> str:

    position = choice(range(len(test_case)))
    character = get_random_character()

    test_case = test_case[:position] + character + test_case[position + 1:]

    return test_case


def add_test_case(individual: List[str]) -> List[str]:

    new_test_case = create_test_case()
    individual.append(new_test_case)

    return individual


def remove_test_case(individual: List[str]) -> List[str]:

    index = choice(range(len(individual)))
    individual.pop(index)

    return individual


def modify_test_case(individual: List[str]) -> List[str]:

    index = choice(range(len(individual)))

    # Se eligan las opciones que pueden ser consideradas
    choices = []
    if len(individual[index]) > 1:
        choices.append("remove")
    if len(individual[index]) < 10:
        choices.append("add")
    if len(individual[index]) > 0:
        choices.append("modify")

    # Elegimos aleatoriamente
    tipo = choice(choices)

    if tipo == "add":
        individual[index] = add_character(individual[index])
    elif tipo == "remove":
        individual[index] = remove_character(individual[index])
    else:
        individual[index] = modify_character(individual[index])

    return individual


def mutate(individual: List[str]) -> List[str]:

    # Se eligan las opciones que pueden ser consideradas
    choices = []
    if len(individual) > 1:
        choices.append("remove")
    if len(individual) < 15:
        choices.append("add")
    if len(individual) > 0:
        choices.append("modify")

    # Elegimos aleatoriamente
    tipo = choice(choices)

    if tipo == "add":
        individual = add_test_case(individual)
    elif tipo == "remove":
        individual = remove_test_case(individual)
    else:
        individual = modify_test_case(individual)    

    return individual

