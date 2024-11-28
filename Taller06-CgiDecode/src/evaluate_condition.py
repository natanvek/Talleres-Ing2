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

def evaluate_condition(condition_num: int, op: str, lhs: Union[str, int], rhs: Union[str, int, Dict]) -> bool:
    global distances_true, distances_false

    K = 1

    # Caso diccionario
    if isinstance(lhs, str) and len(lhs) == 1 and isinstance(rhs, dict) and op == "In":
        d_true = min((abs(ord(lhs) - ord(key)) for key in rhs.keys()), default=sys.maxsize)
        d_false = 0 if d_true > 0 else K
        update_maps(condition_num, d_true, d_false)
        return d_true == 0

    # Caso caracteres
    if isinstance(lhs, str) and len(lhs) == 1 and isinstance(rhs, str) and len(rhs) == 1:
        lhs = ord(lhs)
        rhs = ord(rhs)
    elif not isinstance(lhs, int) or not isinstance(rhs, int):
        raise ValueError("Operación no válida.")

    dif = abs(lhs - rhs)
    d_true = 0
    d_false = 0
    match op:
        case "Eq": 
            if dif == 0 : 
                d_false = K
            else :
                d_true = dif
        case "Ne":
            if dif == 0 : 
                d_true = K
            else :
                d_false = dif
        case "Lt":
            if(lhs < rhs) :
                d_false = dif
            else : 
                d_true = dif + K
        case "Le":
            if(lhs <= rhs) :
                d_false = dif + K
            else : 
                d_true = dif
        case "Gt":
            if(lhs > rhs) :
                d_false = dif + K
            else : 
                d_true = dif
        case "Ge":
            if(lhs >= rhs) :
                d_false = dif
            else : 
                d_true = dif + K
        case _:
            raise ValueError("Operación no válida.")

    update_maps(condition_num, d_true, d_false)

    return d_true == 0
    
