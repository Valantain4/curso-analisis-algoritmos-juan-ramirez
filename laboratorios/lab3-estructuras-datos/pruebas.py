"""Pruebas de la lista enlazada y de la tabla hash."""

import random

from estructuras import ListaEnlazada, TablaHash

ESTADOS = ("en bodega", "en reparto", "entregado")


def prueba_lista() -> None:
    """Busqueda exitosa e infructuosa en la lista."""
    lista = ListaEnlazada()
    assert lista.buscar(1000000010) is None
    lista.insertar(1000000010, "en bodega")
    lista.insertar(1000000024, "en reparto")
    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(1000000024) == "en reparto"
    assert lista.buscar(1000000099) is None
    assert lista.tamano == 2


def prueba_colision() -> None:
    """Con m = 7, las guias 10, 24 y 17 caen en la casilla 3."""
    tabla = TablaHash(7)
    for guia in (10, 24, 17):
        tabla.insertar(guia, "en bodega")
    assert tabla.hash(10) == 3
    assert tabla.hash(24) == 3
    assert tabla.hash(17) == 3
    assert tabla.casillas[3].tamano == 3
    assert tabla.buscar(10) == "en bodega"
    assert tabla.buscar(24) == "en bodega"
    assert tabla.buscar(17) == "en bodega"
    assert tabla.buscar(99) is None
    assert tabla.factor_carga() == 3 / 7


def prueba_aleatorias() -> None:
    """Veinte colecciones donde lista y tabla responden igual."""
    azar = random.Random(7)
    for _ in range(20):
        n = azar.randint(8, 40)
        m = azar.choice((7, 11, 13, 17, 23, 31))
        lista = ListaEnlazada()
        tabla = TablaHash(m)
        usadas: set[int] = set()
        pares: list[tuple[int, str]] = []
        while len(pares) < n:
            guia = azar.randint(10**9, 10**10 - 1)
            if guia in usadas:
                continue
            usadas.add(guia)
            estado = ESTADOS[len(pares) % 3]
            pares.append((guia, estado))
            lista.insertar(guia, estado)
            tabla.insertar(guia, estado)
        for guia, estado in pares:
            assert lista.buscar(guia) == estado
            assert tabla.buscar(guia) == estado
        for _ in range(5):
            fantasma = azar.randint(10**9, 10**10 - 1)
            if fantasma in usadas:
                continue
            assert lista.buscar(fantasma) is None
            assert tabla.buscar(fantasma) is None


if __name__ == "__main__":
    prueba_lista()
    prueba_colision()
    prueba_aleatorias()
    print("Todas las pruebas pasaron.")