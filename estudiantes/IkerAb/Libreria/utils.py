"""
utils.py
--------
Funciones auxiliares de validación y cálculo matemático
utilizadas por los demás módulos de la librería stat_tools.
"""


def valida_1(data):
    """
    Valida que el argumento sea una lista de números flotantes.

    Parámetros
    ----------
    data : list
        Lista a validar.

    Retorna
    -------
    list
        La misma lista si pasa la validación.

    Lanza
    -----
    ValueError
        Si `data` no es una lista o no contiene exclusivamente flotantes.

    Ejemplo
    -------
    >>> valida_1([1.0, 2.0, 3.0])
    [1.0, 2.0, 3.0]
    """
    if not isinstance(data, list):
        raise ValueError("El dato no es una lista de numeros")
    if not all(isinstance(item, float) for item in data):
        raise ValueError("El dato no es una lista de enteros")
    return data


def valida_2(data1, data2):
    """
    Valida que ambos argumentos sean listas de números flotantes.

    Parámetros
    ----------
    data1 : list
        Primera lista a validar.
    data2 : list
        Segunda lista a validar.

    Retorna
    -------
    tuple[list, list]
        Las mismas listas si pasan la validación.

    Lanza
    -----
    ValueError
        Si alguna de las listas no es de tipo list o no contiene
        exclusivamente flotantes.

    Ejemplo
    -------
    >>> valida_2([1.0, 2.0], [3.0, 4.0])
    ([1.0, 2.0], [3.0, 4.0])
    """
    if not isinstance(data1, list) or not isinstance(data2, list):
        raise ValueError("El dato no es una lista de numeros")
    if not all(isinstance(item, float) for item in data1) or not all(isinstance(item, float) for item in data2):
        raise ValueError("El dato no es una lista de enteros")
    return data1, data2


def valida_probabilidad(p):
    """
    Valida que un valor sea una probabilidad válida (entre 0 y 1).

    Parámetros
    ----------
    p : int or float
        Valor a validar como probabilidad.

    Retorna
    -------
    int or float
        El mismo valor si pasa la validación.

    Lanza
    -----
    ValueError
        Si `p` es menor que 0, mayor que 1, o no es numérico.

    Ejemplo
    -------
    >>> valida_probabilidad(0.95)
    0.95
    """
    if p < 0 or p > 1 or not isinstance(p, (int, float)):
        raise ValueError("La probabilidad no puede ser menor que 0 o mayor que 1")
    return p


def factorial(n):
    """
    Calcula el factorial de un número entero no negativo de forma recursiva.

    Parámetros
    ----------
    n : int
        Número al que se le calculará el factorial.

    Retorna
    -------
    int
        El factorial de `n`.

    Lanza
    -----
    ValueError
        Si `n` es negativo.

    Ejemplo
    -------
    >>> factorial(5)
    120
    """
    if n < 0:
        raise ValueError("El numero no puede ser negativo")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combinatoria(n, k):
    """
    Calcula el coeficiente binomial "n sobre k" (combinaciones sin repetición).

    Parámetros
    ----------
    n : int
        Número total de elementos.
    k : int
        Número de elementos a elegir.

    Retorna
    -------
    float
        El número de combinaciones posibles de `k` elementos de un conjunto de `n`.

    Lanza
    -----
    ValueError
        Si `n` o `k` son negativos, o si `k` es mayor que `n`.

    Ejemplo
    -------
    >>> combinatoria(5, 2)
    10.0
    """
    if n < 0 or k < 0:
        raise ValueError("Los numeros no pueden ser negativos")
    if n < k:
        raise ValueError("El numero de elementos no puede ser mayor al numero total")
    return factorial(n) / (factorial(k) * factorial(n - k))


def z_critico(confianza):
    """
    Devuelve el valor crítico z de la distribución normal estándar
    para un nivel de confianza dado.

    Parámetros
    ----------
    confianza : float
        Nivel de confianza. Valores aceptados: 0.90, 0.95, 0.99.

    Retorna
    -------
    float
        Valor crítico z correspondiente al nivel de confianza.

    Lanza
    -----
    ValueError
        Si el nivel de confianza no es uno de los valores aceptados.

    Ejemplo
    -------
    >>> z_critico(0.95)
    1.96
    """
    tabla = {
        0.90: 1.645,
        0.95: 1.96,
        0.99: 2.576
    }
    if confianza not in tabla:
        raise ValueError("La confianza no es valida")
    return tabla[confianza]
    