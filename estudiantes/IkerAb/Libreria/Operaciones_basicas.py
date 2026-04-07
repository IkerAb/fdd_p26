"""
basic.py
--------
Operaciones aritméticas básicas sobre listas de números.
Todos los módulos de stat_tools dependen de estas funciones.
"""

from .utils import valida_1


def suma(data):
    """
    Calcula la suma de todos los elementos de una lista.

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    float
        Suma de todos los elementos de `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> suma([1.0, 2.0, 3.0])
    6.0
    """
    valida_1(data)
    return sum(data)


def conteo(data):
    """
    Cuenta el número de elementos de una lista.

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    int
        Número de elementos en `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> conteo([1.0, 2.0, 3.0])
    3
    """
    valida_1(data)
    return len(data)


def suma_cuadrados(data):
    """
    Calcula la suma de los cuadrados de todos los elementos de una lista.

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    float
        Suma de los cuadrados de cada elemento de `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> suma_cuadrados([1.0, 2.0, 3.0])
    14.0
    """
    valida_1(data)
    suma = 0
    for item in data:
        suma += item ** 2
    return suma


def producto(data):
    """
    Calcula el producto de todos los elementos de una lista.

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    float
        Producto de todos los elementos de `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> producto([1.0, 2.0, 3.0])
    6.0
    """
    valida_1(data)
    producto = 1
    for item in data:
        producto *= item
    return producto