from challenge_tools import unique_tags

# ---------------------------------------------------------------------------
# R-07: unique_tags — quita duplicados, conserva primera aparición y
#                     orden original; comparación SENSIBLE a mayúsculas
# ---------------------------------------------------------------------------

def test_unique_tags_preserves_order_of_first_appearance():
    # R-07: se conserva el ORDEN ORIGINAL según la primera aparición,
    # no un orden arbitrario (como el que produce un set()).
    assert unique_tags(["b", "a", "b", "c", "a"]) == ["b", "a", "c"]


def test_unique_tags_is_case_sensitive():
    # R-07: la comparación distingue mayúsculas/minúsculas -> "Tag" y
    # "tag" son etiquetas DISTINTAS y ambas se conservan.
    # A propósito, esta función NO debe llamar a casefold()/lower():
    # eso pertenece a R-03 (normalize_answer), no a R-07.
    assert unique_tags(["Tag", "tag", "Tag"]) == ["Tag", "tag"]


def test_unique_tags_combines_case_sensitivity_with_order_and_dedup():
    # R-07 combinado: tres etiquetas distintas por mayúscula/minúscula,
    # con una repetición exacta al final que sí debe eliminarse.
    result = unique_tags(["Python", "python", "PYTHON", "Python"])
    assert result == ["Python", "python", "PYTHON"]


def test_unique_tags_single_element_list():
    assert unique_tags(["x"]) == ["x"]


def test_unique_tags_returns_new_list_and_does_not_mutate_input():
    # R-02: no debe modificar la lista recibida.
    original = ["x", "y", "x"]
    original_copy = list(original)
    result = unique_tags(original)
    assert original == original_copy
    assert result is not original
