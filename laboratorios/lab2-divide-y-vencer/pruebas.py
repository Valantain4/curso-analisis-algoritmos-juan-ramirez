"""Pruebas de coincidencia entre fuerza bruta y divide y venceras."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def suma_de(algoritmo, valores: list[float]) -> float:
    """Devuelve solo la suma del tramo que reporta el algoritmo."""
    if algoritmo is subarreglo_fuerza_bruta:
        return algoritmo(valores)[2]
    return algoritmo(valores, 0, len(valores) - 1)[2]


def main() -> None:
    """Verifica los casos minimos de la Parte 1."""
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

    un_elemento = [-4.5]
    assert suma_de(subarreglo_fuerza_bruta, un_elemento) == -4.5
    assert suma_de(subarreglo_maximo, un_elemento) == -4.5

    negativos = [-8, -3, -11, -1, -6]
    assert suma_de(subarreglo_fuerza_bruta, negativos) == -1
    assert suma_de(subarreglo_maximo, negativos) == -1

    positivos = [2, 4, 1, 3]
    assert suma_de(subarreglo_fuerza_bruta, positivos) == 10
    assert suma_de(subarreglo_maximo, positivos) == 10

    cruzado = [1, -10, 5, 6]
    assert suma_de(subarreglo_fuerza_bruta, cruzado) == 11
    assert suma_de(subarreglo_maximo, cruzado) == 11

    rng = random.Random(42)
    for _ in range(25):
        n = rng.randint(1, 40)
        lista = [float(rng.randint(-20, 20)) for _ in range(n)]
        suma_fb = suma_de(subarreglo_fuerza_bruta, lista)
        suma_dyv = suma_de(subarreglo_maximo, lista)
        assert suma_fb == suma_dyv

    print("Todas las pruebas pasaron.")


if __name__ == "__main__":
    main()