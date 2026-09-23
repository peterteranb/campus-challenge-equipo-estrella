"""Añade pruebas para comportamientos no cubiertos en test_baseline.py.

Cada prueba debe:
- Tener un nombre que comience con test_.
- Comprobar el comportamiento mediante assert.
- Indicar el requisito correspondiente en un comentario o docstring.

Deriva el resultado esperado del requisito, no del resultado
que devuelve la implementación actual.
"""

from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    rotate_left,
    round_score_to_ten,
    unique_tags,
)

# --- Pruebas R-06 ---
def test_rank_teams_applies_score_order_before_case_insensitive_tie_breaking():
    """R-06: Primero ordena por puntuación descendente y luego resuelve cada empate alfabéticamente sin distinguir mayúsculas."""
    entries = [
        ("beta", 20),
        ("Zulu", 20),
        ("Charlie", 30),
        ("alpha", 20),
        ("Delta", 10),
    ]
    expected = [
        ("Charlie", 30),
        ("alpha", 20),
        ("beta", 20),
        ("Zulu", 20),
        ("Delta", 10),
    ]

    assert rank_teams(entries) == expected


def test_rank_teams_does_not_depend_on_input_order_for_ties():
    """R-06: Un empate debe producir el mismo orden alfabético aunque las entradas lleguen invertidas."""
    entries = [("gamma", 50), ("Alpha", 50), ("beta", 50)]
    expected = [("Alpha", 50), ("beta", 50), ("gamma", 50)]

    assert rank_teams(entries) == expected


def test_rank_teams_does_not_modify_nested_input_entries():
    """R-02 & R-06: La clasificación debe dejar intacta la colección recibida."""
    original = [("Beta", 10), ("Alpha", 30), ("Gamma", 20)]
    snapshot = list(original)

    result = rank_teams(original)

    assert original == snapshot
    assert result is not original