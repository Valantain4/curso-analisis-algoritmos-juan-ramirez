"""Medicion comparativa de insertion sort y merge sort sobre el escenario A."""

from pathlib import Path
import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3
DIR_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def medir_algoritmo(algoritmo, datos: list[int]) -> float:
    """Cronometra una funcion de ordenamiento sobre una lista ya generada.

    Args:
        algoritmo: insertion_sort o merge_sort.
        datos: lote de indices de riesgo.

    Returns:
        Mediana del tiempo de ejecucion en segundos.
    """
    tiempos: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        algoritmo(datos)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def main() -> None:
    """Compara ambos algoritmos en el escenario A y guarda la grafica."""
    tiempos_insertion: list[float] = []
    tiempos_merge: list[float] = []

    print("n\talgoritmo\ttiempo_s")
    for n in TAMANOS:
        datos = generar_aleatorio(n)
        t_insertion = medir_algoritmo(insertion_sort, datos)
        t_merge = medir_algoritmo(merge_sort, datos)
        tiempos_insertion.append(t_insertion)
        tiempos_merge.append(t_merge)
        print(f"{n}\tinsertion_sort\t{t_insertion:.6f}")
        print(f"{n}\tmerge_sort\t{t_merge:.6f}")

    plt.figure(figsize=(8, 5))
    plt.plot(TAMANOS, tiempos_insertion, marker="o", label="Insertion sort")
    plt.plot(TAMANOS, tiempos_merge, marker="o", label="Merge sort")
    plt.title("Tiempo de ejecucion vs. tamano de entrada (escenario A)")
    plt.xlabel("Tamano de entrada (numero de registros)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    DIR_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(DIR_GRAFICAS / "parte4_tiempo.png", dpi=150)
    plt.close()
    print("Grafica guardada en graficas/parte4_tiempo.png")


if __name__ == "__main__":
    main()