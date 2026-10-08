"""Medicion comparativa de fuerza bruta y divide y venceras."""

from pathlib import Path
import random
import statistics
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

TAMANOS = [10, 50, 100, 500, 1000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 42
DIR_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def generar_serie(n: int) -> list[float]:
    """Genera n variaciones enteras entre -100 y 100, con semilla fija."""
    rng = random.Random(SEMILLA)
    return [float(rng.randint(-100, 100)) for _ in range(n)]


def medir(algoritmo, valores: list[float]) -> float:
    """Cronometra solo la llamada al algoritmo y devuelve la mediana."""
    tiempos: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        if algoritmo is subarreglo_fuerza_bruta:
            algoritmo(valores)
        else:
            algoritmo(valores, 0, len(valores) - 1)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def main() -> None:
    """Mide ambos algoritmos, verifica sumas y guarda la grafica."""
    tiempos_fb: list[float] = []
    tiempos_dyv: list[float] = []

    print("n\tfuerza_bruta_s\tdivide_y_venceras_s\tsuma")
    for n in TAMANOS:
        valores = generar_serie(n)
        suma_fb = subarreglo_fuerza_bruta(valores)[2]
        suma_dyv = subarreglo_maximo(valores, 0, n - 1)[2]
        if suma_fb != suma_dyv:
            raise RuntimeError(f"las sumas no coinciden en n={n}")

        t_fb = medir(subarreglo_fuerza_bruta, valores)
        t_dyv = medir(subarreglo_maximo, valores)
        tiempos_fb.append(t_fb)
        tiempos_dyv.append(t_dyv)
        print(f"{n}\t{t_fb:.6f}\t{t_dyv:.6f}\t{suma_fb}")

    plt.figure(figsize=(8, 5))
    plt.plot(TAMANOS, tiempos_fb, marker="o", label="Fuerza bruta")
    plt.plot(TAMANOS, tiempos_dyv, marker="o", label="Divide y venceras")
    plt.title("Tiempo de ejecucion vs. tamano de la serie")
    plt.xlabel("Tamano de entrada (numero de dias)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    DIR_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(DIR_GRAFICAS / "tiempo_vs_n.png", dpi=150)
    plt.close()
    print("Grafica guardada en graficas/tiempo_vs_n.png")


if __name__ == "__main__":
    main()