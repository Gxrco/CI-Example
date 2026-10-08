"""Pruebas de mathlib.powers.square."""

import pytest

from mathlib import square


@pytest.mark.parametrize(
    ("numero", "esperado"),
    [
        (5, 25),
        (12, 144),
        (-4, 16),
        (2.5, 6.25),
    ],
)
def test_square_retorna_el_cuadrado(numero, esperado):
    assert square(numero) == esperado


def test_square_de_cero_es_cero():
    assert square(0) == 0


@pytest.mark.parametrize("invalido", ["5", None, True, [2]])
def test_square_rechaza_valores_no_numericos(invalido):
    with pytest.raises(TypeError):
        square(invalido)
