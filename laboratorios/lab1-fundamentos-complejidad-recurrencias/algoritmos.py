"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.
    El resultado queda de mayor a menor indice de riesgo.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    lista = datos.copy()
    comparaciones = 0
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if lista[j] < clave:
                lista[j + 1] = lista[j]
                j -= 1
            else:
                break
        lista[j + 1] = clave
    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.
    El resultado queda de mayor a menor indice de riesgo.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    comparaciones = 0

    def mezclar(izquierda: list[int], derecha: list[int]) -> list[int]:
        nonlocal comparaciones
        resultado: list[int] = []
        i = 0
        j = 0
        while i < len(izquierda) and j < len(derecha):
            comparaciones += 1
            if izquierda[i] >= derecha[j]:
                resultado.append(izquierda[i])
                i += 1
            else:
                resultado.append(derecha[j])
                j += 1
        resultado.extend(izquierda[i:])
        resultado.extend(derecha[j:])
        return resultado

    def ordenar(lista: list[int]) -> list[int]:
        if len(lista) <= 1:
            return lista
        mitad = len(lista) // 2
        izquierda = ordenar(lista[:mitad])
        derecha = ordenar(lista[mitad:])
        return mezclar(izquierda, derecha)

    return ordenar(datos.copy()), comparaciones