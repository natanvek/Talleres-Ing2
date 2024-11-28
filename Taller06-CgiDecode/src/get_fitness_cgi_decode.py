from typing import List

from src.evaluate_condition import clear_maps, get_true_distance, get_false_distance, has_reached_condition
from src.cgi_decode_instrumented import cgi_decode_instrumented

def get_fitness_cgi_decode(test_suite: List[str]) -> float:
    # Borro la información de branch coverage de ejecuciones anteriores
    # Recuerden que los diccionarios true_distances y false_distances son globales
    clear_maps()

    fitness = 0

    for test_case in test_suite:
        try:
            cgi_decode_instrumented(test_case)
        except Exception as _:
            pass

    for c_num in range(1, 6):

        true_distance = get_true_distance(c_num)
        false_distance = get_false_distance(c_num)

        if true_distance is not None:
            fitness += normalizar(true_distance)
        else:
            fitness += 1

        if false_distance is not None:
            fitness += normalizar(false_distance)
        else:
            fitness += 1


    return fitness

def normalizar(x: int) -> float:
    return x / (x + 1)
