"""Pruebas de mathlib.combinatorics.factorial."""

import pytest

from mathlib import factorial


@pytest.mark.parametrize(
    ("numero", "esperado"),
    [
        (3, 6),
        (5, 120),
        (10, 3_628_800),
    ],
)
def test_factorial_de_enteros_positivos(numero, esperado):
    assert factorial(numero) == esperado


@pytest.mark.parametrize("numero", [0, 1])
def test_factorial_de_cero_y_uno_es_uno(numero):
    assert factorial(numero) == 1


def test_factorial_cumple_la_relacion_recursiva():
    assert factorial(6) == 6 * factorial(5)


def test_factorial_rechaza_negativos():
    with pytest.raises(ValueError, match="no puede ser negativo"):
        factorial(-1)


@pytest.mark.parametrize("invalido", [2.5, "5", None, False])
def test_factorial_rechaza_valores_no_enteros(invalido):
    with pytest.raises(TypeError):
        factorial(invalido)
