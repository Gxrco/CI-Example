"""Operaciones combinatorias."""

from mathlib.validation import ensure_non_negative


def factorial(n):
    """Retorna el factorial de un número entero no negativo.

    >>> factorial(5)
    120
    """
    ensure_non_negative(n)
    resultado = 1
    for factor in range(2, n + 1):
        resultado *= factor
    return resultado
