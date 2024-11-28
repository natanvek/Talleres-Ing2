import sys
from typing import Dict, Union

# Inicializar mappings globales
distances_true: Dict[int, int] = {}
distances_false: Dict[int, int] = {}


def update_maps(condition_num: int, d_true: int, d_false: int):
    global distances_true, distances_false

    if condition_num in distances_true.keys():
        distances_true[condition_num] = min(
            distances_true[condition_num], d_true)
    else:
        distances_true[condition_num] = d_true

    if condition_num in distances_false.keys():
        distances_false[condition_num] = min(
            distances_false[condition_num], d_false)
    else:
        distances_false[condition_num] = d_false


def clear_maps():
    global distances_true, distances_false
    distances_true.clear()
    distances_false.clear()


def get_true_distance(condition_num: int) -> Union[int, None]:
    global distances_true
    if condition_num in distances_true.keys():
        return distances_true[condition_num]
    else:
        return None


def get_false_distance(condition_num: int) -> Union[int, None]:
    global distances_false
    if condition_num in distances_false.keys():
        return distances_false[condition_num]
    else:
        return None


def has_reached_condition(condition_num: int) -> bool:
    global distances_true, distances_false
    return condition_num in distances_true.keys() or condition_num in distances_false.keys()

def evaluate_condition(condition_num: int, op: str, lhs: Union[str, Dict], rhs: Union[str, Dict]) -> bool:
    global distances_true, distances_false

    K = 1

    # Convertimos caracteres a su valor ordinal
    if isinstance(lhs, str) and len(lhs) == 1:
        lhs = ord(lhs)
    if isinstance(rhs, str) and len(rhs) == 1:
        rhs = ord(rhs)
    elif isinstance(rhs, dict):
        # Convertimos diccionario a lista de claves
        rhs = list(rhs.keys())
        rhs = [ord(k) if isinstance(k, str) and len(k) == 1 else k for k in rhs]

    result = False
    if op == "Eq": 
        result = lhs == rhs
        d_true = abs(lhs - rhs)
        d_false = 0 if not result else K
    elif op == "Ne":
        result = lhs != rhs
        d_true = 0 if result else K
        d_false = abs(lhs - rhs)
    elif op == "Lt":
        result = lhs < rhs
        d_true = 0 if result else (lhs - rhs) + K
        d_false = 0 if not result else (rhs - lhs)
    elif op == "Le":
        result = lhs <= rhs
        d_true = 0 if result else (lhs - rhs)
        d_false = 0 if not result else (rhs - lhs) + K
    elif op == "Gt":
        result = lhs > rhs
        d_true = 0 if result else (rhs - lhs) + K
        d_false = 0 if not result else (lhs - rhs)
    elif op == "Ge":
        result = lhs >= rhs
        d_true = 0 if result else (rhs - lhs)
        d_false = 0 if not result else (lhs - rhs) + K
    elif op == "In" and isinstance(rhs, list):
        result = lhs in rhs
        d_true = sys.maxsize if not rhs else min(abs(lhs - x) for x in rhs)
        d_false = 0 if result else K
    else:
        raise ValueError("Operación no válida.")

    update_maps(condition_num, d_true, d_false)

    return result
    
