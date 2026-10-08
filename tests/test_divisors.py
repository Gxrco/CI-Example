"""Pruebas de mathlib.divisors.gcd y lcm."""

import pytest

from mathlib import gcd, lcm


@pytest.mark.parametrize(
    ("a", "b", "esperado"),
    [
        (12, 18, 6),
        (48, 18, 6),
        (7, 13, 1),
        (-12, 18, 6),
    ],
)
def test_gcd_retorna_el_maximo_comun_divisor(a, b, esperado):
    assert gcd(a, b) == esperado


def test_gcd_con_cero_retorna_el_otro_operando():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 5


@pytest.mark.parametrize(
    ("a", "b", "esperado"),
    [
        (4, 6, 12),
        (21, 6, 42),
        (7, 13, 91),
        (-4, 6, 12),
    ],
)
def test_lcm_retorna_el_minimo_comun_multiplo(a, b, esperado):
    assert lcm(a, b) == esperado


@pytest.mark.parametrize(("a", "b"), [(0, 5), (5, 0), (0, 0)])
def test_lcm_con_cero_es_cero(a, b):
    assert lcm(a, b) == 0


def test_gcd_por_lcm_es_igual_al_producto():
    assert gcd(12, 18) * lcm(12, 18) == 12 * 18


@pytest.mark.parametrize("invalido", [1.5, "4", None, True])
def test_gcd_rechaza_valores_no_enteros(invalido):
    with pytest.raises(TypeError):
        gcd(invalido, 2)


@pytest.mark.parametrize("invalido", [1.5, "4", None, True])
def test_lcm_rechaza_valores_no_enteros(invalido):
    with pytest.raises(TypeError):
        lcm(2, invalido)
