"""Operaciones sobre divisores y múltiplos comunes."""

from mathlib.validation import ensure_integer


def gcd(a, b):
    """Retorna el máximo común divisor de dos enteros (algoritmo de Euclides).

    >>> gcd(12, 18)
    6
    """
    ensure_integer(a, "a")
    ensure_integer(b, "b")
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return b


def lcm(a, b):
    """Retorna el mínimo común múltiplo de dos enteros.

    Si alguno de los operandos es cero el resultado es cero.

    >>> lcm(4, 6)
    12
    """
    ensure_integer(a, "a")
    ensure_integer(b, "b")
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, a)
