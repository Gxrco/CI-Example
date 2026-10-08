"""Pruebas de mathlib.primes.is_prime."""

import pytest

from mathlib import is_prime


@pytest.mark.parametrize("primo", [2, 3, 7, 17, 97, 7919])
def test_is_prime_reconoce_primos(primo):
    assert is_prime(primo) is True


@pytest.mark.parametrize("compuesto", [4, 9, 100, 7917])
def test_is_prime_reconoce_compuestos(compuesto):
    assert is_prime(compuesto) is False


@pytest.mark.parametrize("numero", [-7, 0, 1])
def test_is_prime_descarta_numeros_menores_a_dos(numero):
    assert is_prime(numero) is False


@pytest.mark.parametrize("invalido", [7.0, "7", None, True])
def test_is_prime_rechaza_valores_no_enteros(invalido):
    with pytest.raises(TypeError):
        is_prime(invalido)
