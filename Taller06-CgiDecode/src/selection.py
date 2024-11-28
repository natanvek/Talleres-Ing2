from random import sample
from typing import Tuple


def selection(fitness_by_individual: dict, tournament_size: int) -> Tuple[str, float]:
    """
    fitness_by_individual: Diccionario que contiene a los individuos de la población como keys y su fitness como valores.
    tournament_size: Tamaño del torneo (entero positivo).
    """

    participantes = sample(list(fitness_by_individual.keys()), tournament_size)
    winner = min(participantes, key = lambda x: fitness_by_individual[x])
    
    return winner, fitness_by_individual[winner]
