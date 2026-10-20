"""Operaciones de potenciación."""

from mathlib.validation import ensure_number


def square(n):
    """Retorna el cuadrado de un número.

    >>> square(5)
    25
    """
    ensure_number(n)
    return n * n
