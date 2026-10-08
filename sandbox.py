
import mathlib


def probar(etiqueta, funcion, *args):
    """Ejecuta una función y muestra el resultado o el error que levantó."""
    try:
        print(f"{etiqueta:<22} -> {funcion(*args)!r}")
    except (TypeError, ValueError) as error:
        print(f"{etiqueta:<22} -> {type(error).__name__}: {error}")


def main():
    print(f"mathlib {mathlib.__version__} | API: {mathlib.__all__}\n")

    print("-- square --")
    for n in (0, 5, -4, 2.5):
        probar(f"square({n})", mathlib.square, n)

    print("\n-- factorial --")
    for n in (0, 1, 5, 10):
        probar(f"factorial({n})", mathlib.factorial, n)

    print("\n-- is_prime --")
    for n in (-7, 0, 1, 2, 9, 17, 97, 100):
        probar(f"is_prime({n})", mathlib.is_prime, n)

    print("\n-- gcd / lcm --")
    for a, b in ((12, 18), (7, 13), (0, 5), (-12, 18)):
        probar(f"gcd({a}, {b})", mathlib.gcd, a, b)
        probar(f"lcm({a}, {b})", mathlib.lcm, a, b)

    print("\n-- validaciones --")
    probar("factorial(-1)", mathlib.factorial, -1)
    probar("factorial(2.5)", mathlib.factorial, 2.5)
    probar("is_prime('7')", mathlib.is_prime, "7")
    probar("square(True)", mathlib.square, True)
    probar("gcd(1.5, 2)", mathlib.gcd, 1.5, 2)


if __name__ == "__main__":
    main()
