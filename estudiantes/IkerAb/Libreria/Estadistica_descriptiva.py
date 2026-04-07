"""
Estadistica_descriptiva.py
--------------
Funciones de estadística descriptiva sobre listas de números.
Depende de utils.py y Operaciones_basicas.py.
"""

from math import sqrt
from .utils import valida_1
from .Operaciones_basicas import suma, conteo, suma_cuadrados


def media(data):
    """
    Calcula la media aritmética de una lista de números.

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    float
        Media aritmética de los elementos de `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> media([1.0, 2.0, 3.0])
    2.0
    """
    valida_1(data)
    return suma(data) / conteo(data)


def varianza(data):
    """
    Calcula la varianza muestral de una lista de números.

    Utiliza el estimador insesgado dividiendo entre (n-1).

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    float
        Varianza muestral de los elementos de `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> varianza([1.0, 2.0, 3.0])
    1.0
    """
    valida_1(data)
    return 1 / (conteo(data) - 1) * (suma_cuadrados(data) - (suma(data) ** 2) / conteo(data))


def desviacion_estandar(data):
    """
    Calcula la desviación estándar muestral de una lista de números.

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    float
        Desviación estándar muestral de los elementos de `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> desviacion_estandar([1.0, 2.0, 3.0])
    1.0
    """
    valida_1(data)
    return sqrt(varianza(data))


def minimo(data):
    """
    Encuentra el valor mínimo de una lista de números.

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    float
        El valor más pequeño de `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> minimo([1.0, 2.0, 3.0])
    1.0
    """
    valida_1(data)
    return min(data)


def maximo(data):
    """
    Encuentra el valor máximo de una lista de números.

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    float
        El valor más grande de `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> maximo([1.0, 2.0, 3.0])
    3.0
    """
    valida_1(data)
    return max(data)


def rango(data):
    """
    Calcula el rango de una lista de números.

    El rango es la diferencia entre el valor máximo y el mínimo.

    Parámetros
    ----------
    data : list[float]
        Lista de números flotantes.

    Retorna
    -------
    float
        Diferencia entre el máximo y el mínimo de `data`.

    Lanza
    -----
    ValueError
        Si `data` no es una lista de flotantes.

    Ejemplo
    -------
    >>> rango([1.0, 2.0, 3.0])
    2.0
    """
    valida_1(data)
    return maximo(data) - minimo(data)