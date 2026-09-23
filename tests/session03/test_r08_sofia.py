from challenge_tools import average_score


def test_average_score_handles_empty_input():
    """R-08: Una colección vacía debe devolver 0.0."""
    assert average_score([]) == 0.0

def test_average_score_preserves_fractional_average():
    """R-08: La media aritmética debe conservar su parte fraccionaria."""
    assert average_score([1, 2, 4]) == 7 / 3

def test_average_score_does_not_mutate_input_list():
    """R-02: no debe modificar la colección recibida."""
    original = [10, 20, 30]
    original_copy = list(original)
    average_score(original)
    assert original == original_copy