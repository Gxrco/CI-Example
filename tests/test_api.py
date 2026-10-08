"""Pruebas de la API pública del paquete mathlib."""

import mathlib


def test_el_paquete_expone_las_cinco_funciones():
    assert mathlib.__all__ == ["square", "factorial", "is_prime", "gcd", "lcm"]


def test_las_funciones_exportadas_son_invocables():
    for nombre in mathlib.__all__:
        assert callable(getattr(mathlib, nombre))


def test_el_paquete_declara_version():
    assert mathlib.__version__
