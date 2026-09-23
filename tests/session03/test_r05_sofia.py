from challenge_tools import round_score_to_ten


def test_round_score_to_ten_rounds_halfway_up():
    """R-05: En la mitad exacta, la puntuación debe redondearse hacia arriba."""
    assert round_score_to_ten(25) == 30

def test_round_score_exact_multiple_of_ten_is_unchanged():
    assert round_score_to_ten(30) == 30


def test_round_score_midpoint_five_rounds_up_to_ten():
    # R-05: punto medio 5 (entre 0 y 10) -> hacia arriba.
    assert round_score_to_ten(5) == 10


def test_round_score_midpoint_fifteen_rounds_up_to_twenty():
    # R-05: punto medio 15 (entre 10 y 20) -> hacia arriba.
    assert round_score_to_ten(15) == 20