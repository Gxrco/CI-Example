"""mathlib: librería de matemática básica.

Expone la API pública del paquete para que los consumidores importen
siempre desde `mathlib` y no desde los módulos internos.
"""

from mathlib.combinatorics import factorial
from mathlib.divisors import gcd, lcm
from mathlib.powers import square
from mathlib.primes import is_prime

__version__ = "0.1.0"

__all__ = ["square", "factorial", "is_prime", "gcd", "lcm"]
