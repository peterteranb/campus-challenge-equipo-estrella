"""Funciones iniciales de Campus Challenge.

Revisa su comportamiento según los requisitos de la actividad.
"""
import sys


def verify_python_version():
    """Devuelve True cuando Python es 3.10 o mas."""
    return sys.version_info >= (3, 10)

def normalize_answer(answer):
    """Normaliza una respuesta para compararla sin distinguir mayúsculas."""
    return answer.strip().casefold()


def rotate_left(items, steps):
    """Devuelve una lista nueva rotada a la izquierda."""
    copied = list(items)
    copied.rotate(-steps)
    return copied


def round_score_to_ten(score):
    """Redondea una puntuación no negativa a la decena más cercana."""
    return ((score + 5) // 10) * 10


def rank_teams(entries):
    """Ordena pares (equipo, puntuación) para la clasificación."""
    return sorted(entries, key=lambda item: -item[1])


def unique_tags(tags):
    """Elimina etiquetas repetidas."""
    seen = set()
    result = []
    for tag in tags:
        if tag not in seen:
            seen.add(tag)
            result.append(tag)
    return result


def average_score(scores):
    if len(scores) == 0:
        return 0.0

    return sum(scores) / len(scores)

def rank_teams(entries):
    return sorted(entries, key=lambda item: (-item[1], item[0].casefold()))

def rotate_left(items, steps):
    copied = list(items)

    if len(copied) == 0:
        return copied

    steps = steps % len(copied)

    return copied[steps:] + copied[:steps]