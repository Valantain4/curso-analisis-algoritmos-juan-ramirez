"""Mide busquedas infructuosas en la lista y en la tabla hash."""

from pathlib import Path
import random
import statistics
import time

import matplotlib.pyplot as plt

from estructuras import ListaEnlazada, TablaHash

SEMILLA = 7
BUSQUEDAS = 200
REPETICIONES = 3
TAMANOS = [100, 500, 1000, 5000, 20000, 50000]
N_ALFA = 20000
ALFAS_OBJETIVO = [0.5, 1.0, 4.0, 10.0]
ESTADOS = ("en bodega", "en reparto", "entregado")
DIR_GRAFICAS = Path(__file__).resolve().parent / "graficas"


def es_primo(numero: int) -> bool:
    """Dice si un entero es primo."""
    if numero < 2:
        return False
    if numero % 2 == 0:
        return numero == 2
    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True


def primo_cercano(objetivo: int) -> int:
    """Devuelve el primo mas cercano. Si hay empate, el menor."""
    if objetivo <= 2:
        return 2
    if es_primo(objetivo):
        return objetivo
    distancia = 1
    while True:
        menor = objetivo - distancia
        if menor >= 2 and es_primo(menor):
            return menor
        if es_primo(objetivo + distancia):
            return objetivo + distancia
        distancia += 1


def generar_guias(n: int, semilla: int = SEMILLA) -> list[int]:
    """Genera n guias distintas de diez digitos, en orden reproducible."""
    azar = random.Random(semilla)
    usadas: set[int] = set()
    guias: list[int] = []
    while len(guias) < n:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in usadas:
            usadas.add(guia)
            guias.append(guia)
    return guias


def generar_guias_inexistentes(
    existentes: set[int], cantidad: int, semilla: int = 7
) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion.

    Args:
        existentes: guias almacenadas en las estructuras.
        cantidad: cuantas guias inexistentes generar.
        semilla: semilla del generador, para reproducir la medicion.

    Returns:
        Una lista con `cantidad` guias que no pertenecen a `existentes`.
    """
    azar = random.Random(semilla)
    inexistentes: list[int] = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def construir(guias: list[int], m: int) -> tuple[ListaEnlazada, TablaHash]:
    """Inserta las mismas guias en la lista y en la tabla."""
    lista = ListaEnlazada()
    tabla = TablaHash(m)
    for indice, guia in enumerate(guias):
        estado = ESTADOS[indice % 3]
        lista.insertar(guia, estado)
        tabla.insertar(guia, estado)
    return lista, tabla


def verificar_muestra(lista: ListaEnlazada, tabla: TablaHash, guias: list[int]) -> None:
    """Comprueba que lista y tabla devuelven el mismo estado."""
    for guia in guias[:30]:
        estado_lista = lista.buscar(guia)
        estado_tabla = tabla.buscar(guia)
        if estado_lista != estado_tabla or estado_lista is None:
            raise RuntimeError(f"la guia {guia} no coincide")


def tiempo_medio(estructura: ListaEnlazada | TablaHash, consultas: list[int]) -> float:
    """Mediana de tres tandas. Cada tanda promedia 200 busquedas."""
    medias: list[float] = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        for guia in consultas:
            estructura.buscar(guia)
        medias.append((time.perf_counter() - inicio) / len(consultas))
    return statistics.median(medias)


def experimento_a() -> None:
    """Lista contra tabla, con alfa cerca de 2."""
    ns: list[int] = []
    tiempos_lista: list[float] = []
    tiempos_tabla: list[float] = []
    print("n\tm\talfa\tlista_s\ttabla_s")
    for n in TAMANOS:
        guias = generar_guias(n)
        m = primo_cercano(n // 2)
        lista, tabla = construir(guias, m)
        verificar_muestra(lista, tabla, guias)
        consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS, SEMILLA)
        t_lista = tiempo_medio(lista, consultas)
        t_tabla = tiempo_medio(tabla, consultas)
        ns.append(n)
        tiempos_lista.append(t_lista)
        tiempos_tabla.append(t_tabla)
        print(f"{n}\t{m}\t{tabla.factor_carga():.4f}\t{t_lista:.8f}\t{t_tabla:.8f}")

    factor_n = ns[-1] / ns[-2]
    print(f"n consecutivos: {ns[-2]} -> {ns[-1]}")
    print(f"n se multiplico por {factor_n:.4f}")
    print(f"la lista se multiplico por {tiempos_lista[-1] / tiempos_lista[-2]:.4f}")
    print(f"la tabla se multiplico por {tiempos_tabla[-1] / tiempos_tabla[-2]:.4f}")

    plt.figure(figsize=(8, 5))
    plt.plot(ns, tiempos_lista, marker="o", label="Lista enlazada")
    plt.plot(ns, tiempos_tabla, marker="o", label="Tabla hash")
    plt.title("Tiempo medio de búsqueda de una guía inexistente")
    plt.xlabel("Número de guías (n)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    DIR_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(DIR_GRAFICAS / "lista_vs_tabla.png", dpi=150)
    plt.close()


def experimento_b() -> None:
    """Tiempo de la tabla al variar el factor de carga, con n fijo."""
    guias = generar_guias(N_ALFA)
    consultas = generar_guias_inexistentes(set(guias), BUSQUEDAS, SEMILLA)
    alfas: list[float] = []
    tiempos: list[float] = []
    print("n\tm\talfa\tojetivo\ttabla_s")
    for objetivo in ALFAS_OBJETIVO:
        m = primo_cercano(round(N_ALFA / objetivo))
        lista, tabla = construir(guias, m)
        verificar_muestra(lista, tabla, guias)
        t_tabla = tiempo_medio(tabla, consultas)
        alfa = tabla.factor_carga()
        alfas.append(alfa)
        tiempos.append(t_tabla)
        print(f"{N_ALFA}\t{m}\t{alfa:.4f}\t{objetivo}\t{t_tabla:.8f}")

    teorico = (1 + alfas[-1]) / (1 + alfas[0])
    print(f"alfa {alfas[0]:.4f} -> {alfas[-1]:.4f}")
    print(f"(1+alfa) se multiplico por {teorico:.4f}")
    print(f"el tiempo se multiplico por {tiempos[-1] / tiempos[0]:.4f}")

    plt.figure(figsize=(8, 5))
    plt.plot(alfas, tiempos, marker="o", label=f"Tabla hash (n = {N_ALFA})")
    plt.title("Tiempo medio de búsqueda frente al factor de carga")
    plt.xlabel("Factor de carga α (guías por casilla)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    DIR_GRAFICAS.mkdir(exist_ok=True)
    plt.savefig(DIR_GRAFICAS / "tiempo_vs_alfa.png", dpi=150)
    plt.close()
    print("Graficas guardadas en graficas/")


if __name__ == "__main__":
    experimento_a()
    experimento_b()