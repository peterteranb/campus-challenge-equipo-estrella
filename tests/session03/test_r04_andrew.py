from challenge_tools import (
    average_score,
    normalize_answer,
    rank_teams,
    rotate_left,
    round_score_to_ten,
    unique_tags,
)

# --- Pruebas R-04 ---
def test_rotate_left_empty_list():
    """R-04: La rotación circular debe admitir una lista vacía."""
    assert rotate_left([], 3) == []


def test_rotate_left_zero_steps_keeps_values_and_returns_new_list():
    """R-02 & R-04: Cero pasos conserva el contenido, sin reutilizar la lista de entrada."""
    original = [1, 2, 3]
    result = rotate_left(original, 0)

    assert result == [1, 2, 3]
    assert result is not original
    assert original == [1, 2, 3]


def test_rotate_left_negative_steps_larger_than_length_is_circular():
    """R-04: Una cantidad negativa mayor que la longitud debe rotar circularmente hacia la derecha."""
    assert rotate_left([1, 2, 3, 4], -5) == [4, 1, 2, 3]


def test_rotate_left_single_item_is_unchanged():
    """R-04: Una lista de un elemento permanece igual con cualquier rotación válida."""
    assert rotate_left([42], 100) == [42]