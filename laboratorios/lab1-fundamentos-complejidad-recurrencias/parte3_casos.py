"""Experimento de peor caso, mejor caso y caso promedio para insertion sort."""

from collections.abc import Callable
from pathlib import Path
import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
DIR_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def verificar_instrumentacion() -> None:
    """Comprueba que insertion sort no muta la entrada y cuenta bien."""
    original = [3, 1, 4, 2]
    ordenada, _ = insertion_sort(original)
    if original != [3, 1, 4, 2]:
        raise RuntimeError("insertion_sort modifico la lista recibida")
    if ordenada != [4, 3, 2, 1]:
        raise RuntimeError("insertion_sort no ordeno de mayor a menor")
    _, comparaciones = insertion_sort([5, 4, 3, 2, 1])
    if comparaciones != 4:
        raise RuntimeError(
            "en una lista ya ordenada deben hacerse n-1 comparaciones"
        )


def medir(
    generador: Callable[[int], list[int]], n: int
) -> tuple[float, int]:
    """Cronometra insertion_sort y cuenta comparaciones para un lote de n.

    Args:
        generador: funcion que construye el lote de tamano n.
        n: tamano del lote.

    Returns:
        Mediana del tiempo en segundos y numero de comparaciones.
    """
    datos = generador(n)
    tiempos: list[float] = []
    comparaciones = 0
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos), comparaciones


def graficar(
    tamanos: list[int],
    series: dict[str, list[float]],
    titulo: str,
    etiqueta_y: str,
    archivo: str,
) -> None:
    """Dibuja varias series contra el tamano de entrada y guarda el PNG."""
    plt.figure(figsize=(8, 5))
    for nombre, valores in series.items():
        plt.plot(tamanos, valores, marker="o", label=nombre)
    plt.title(titulo)
    plt.xlabel("Tamano de entrada (numero de registros)")
    plt.ylabel(etiqueta_y)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    DIR_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(DIR_GRAFICAS / archivo, dpi=150)
    plt.close()


def main() -> None:
    """Ejecuta el experimento de la Parte 3 y genera las graficas."""
    verificar_instrumentacion()
    comparaciones_a: list[float] = []
    comparaciones_b: list[float] = []
    comparaciones_c: list[float] = []
    tiempos_a: list[float] = []
    tiempos_b: list[float] = []
    tiempos_c: list[float] = []

    print("n\tescenario\ttiempo_s\tcomparaciones")
    escenarios = [
        ("A", generar_aleatorio, comparaciones_a, tiempos_a),
        ("B", generar_casi_ordenado, comparaciones_b, tiempos_b),
        ("C", generar_inverso, comparaciones_c, tiempos_c),
    ]
    for n in TAMANOS:
        for nombre, generador, lista_comp, lista_tiempo in escenarios:
            tiempo, comparaciones = medir(generador, n)
            lista_comp.append(float(comparaciones))
            lista_tiempo.append(tiempo)
            print(f"{n}\t{nombre}\t{tiempo:.6f}\t{comparaciones}")

    graficar(
        TAMANOS,
        {
            "A — Aleatorio": comparaciones_a,
            "B — Casi ordenado": comparaciones_b,
            "C — Orden inverso": comparaciones_c,
        },
        "Insertion sort: comparaciones vs. tamano de entrada",
        "Numero de comparaciones entre elementos",
        "parte3_comparaciones.png",
    )
    graficar(
        TAMANOS,
        {
            "A — Aleatorio": tiempos_a,
            "B — Casi ordenado": tiempos_b,
            "C — Orden inverso": tiempos_c,
        },
        "Insertion sort: tiempo vs. tamano de entrada",
        "Tiempo de ejecucion (segundos)",
        "parte3_tiempo.png",
    )
    print("Graficas guardadas en graficas/")


if __name__ == "__main__":
    main()