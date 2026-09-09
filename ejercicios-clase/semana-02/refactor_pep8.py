def calcular_promedio(lista: list[int]) -> float:
    """Calcula el promedio de una lista de números.

    Args:
        lista: Lista de números enteros.

    Returns:
        Promedio de los valores contenidos en la lista.
    """
    suma = 0

    for numero in lista:
        suma = suma + numero

    return suma / len(lista)


def main() -> None:
    """Punto de entrada del programa."""
    numeros = [1, 2, 3, 4, 5]
    promedio = calcular_promedio(numeros)

    print(promedio)


if __name__ == "__main__":
    main()