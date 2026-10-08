"""Operaciones sobre números primos."""

from mathlib.validation import ensure_integer


def is_prime(n):
    """Retorna True si `n` es un número primo.

    Descarta los pares de una vez y luego prueba divisores impares
    hasta la raíz cuadrada de `n`.

    >>> is_prime(7)
    True
    """
    ensure_integer(n)
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 2
    return True
