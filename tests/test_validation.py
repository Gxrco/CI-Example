"""Pruebas de los validadores internos de mathlib."""

import pytest

from mathlib.validation import ensure_integer, ensure_non_negative, ensure_number


@pytest.mark.parametrize("valor", [0, 7, -3, 2.5])
def test_ensure_number_acepta_numeros_y_los_retorna(valor):
    assert ensure_number(valor) == valor


@pytest.mark.parametrize("valor", [0, 7, -3])
def test_ensure_integer_acepta_enteros_y_los_retorna(valor):
    assert ensure_integer(valor) == valor


@pytest.mark.parametrize("valor", [0, 1, 42])
def test_ensure_non_negative_acepta_cero_y_positivos(valor):
    assert ensure_non_negative(valor) == valor


def test_ensure_integer_rechaza_flotantes():
    with pytest.raises(TypeError):
        ensure_integer(2.5)


def test_ensure_non_negative_rechaza_negativos():
    with pytest.raises(ValueError):
        ensure_non_negative(-1)


@pytest.mark.parametrize("validador", [ensure_number, ensure_integer, ensure_non_negative])
def test_los_validadores_rechazan_booleanos(validador):
    with pytest.raises(TypeError):
        validador(True)


def test_el_mensaje_de_error_incluye_el_nombre_del_parametro():
    with pytest.raises(TypeError, match="^a debe ser un entero"):
        ensure_integer("x", "a")
