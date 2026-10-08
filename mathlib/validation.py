"""Validaciones de entrada compartidas por los módulos de la librería."""

NUMBER_TYPES = (int, float)


def ensure_number(value, name="n"):
    """Valida que `value` sea int o float y lo retorna.

    Los booleanos se rechazan: aunque en Python son enteros, no son
    operandos matemáticos válidos para esta librería.
    """
    if isinstance(value, bool) or not isinstance(value, NUMBER_TYPES):
        raise TypeError(f"{name} debe ser un número, se recibió {type(value).__name__}")
    return value


def ensure_integer(value, name="n"):
    """Valida que `value` sea un entero y lo retorna."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} debe ser un entero, se recibió {type(value).__name__}")
    return value


def ensure_non_negative(value, name="n"):
    """Valida que `value` sea un entero mayor o igual a cero y lo retorna."""
    ensure_integer(value, name)
    if value < 0:
        raise ValueError(f"{name} no puede ser negativo, se recibió {value}")
    return value
