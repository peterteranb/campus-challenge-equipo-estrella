from challenge_tools import normalize_answer

# ---------------------------------------------------------------------------
# R-03: normalize_answer — recorte de espacios exteriores + casefold Unicode
# ---------------------------------------------------------------------------

def test_normalize_answer_strips_non_breaking_space():
    # R-03: el espacio de no separación (U+00A0) también es whitespace
    # Unicode y str.strip() lo reconoce como tal en los bordes.
    assert normalize_answer("\xa0Python\xa0") == "python"


def test_normalize_answer_equates_greek_sigma_forms():
    # R-03 (Unicode avanzado): el griego tiene tres formas de sigma:
    # Σ (mayúscula), σ (minúscula media) y ς (minúscula final).
    # casefold() las trata como la MISMA letra para comparación caseless;
    # lower() por sí solo NO iguala ς con σ.
    assert (
        normalize_answer("Σ")
        == normalize_answer("σ")
        == normalize_answer("ς")
    )


def test_normalize_answer_empty_string_stays_empty():
    # Caso límite: cadena vacía.
    assert normalize_answer("") == ""


def test_normalize_answer_only_whitespace_becomes_empty():
    # Caso límite: cadena compuesta solo por espacios.
    assert normalize_answer("   ") == ""
