# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Juan Andres Ramirez Castañeda · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `2e238d2`

Muy buen trabajo, su laboratorio está sólido y bien documentado.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 17 / 20 |
| Calidad de la explicación teórica | 17 / 20 |
| Corrección de la implementación | 24 / 25 |
| Calidad del análisis de las gráficas | 23 / 25 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **91 / 100** |
| **Nota (0–5)** | **4.55** |

## 1. Corrección conceptual (17 / 20)
**Lo que hizo bien:**
- Identifica que divide y vencerás empieza a ganar desde n = 100 y lo apoya con sus tiempos.
- Compara con el máximo de un arreglo y llega a que dividir no mejora (`Θ(n)` en ambos casos).
- La estimación a 1.000.000 de registros está declarada como estimación y no usa una regla de tres lineal.

**Lo que puede mejorar:**
- En la pregunta 4, explique con más detalle por qué combinar cuesta solo `Θ(1)` en el máximo y `Θ(n)` en el subarreglo, y cómo eso cambia el resultado.
- En la pregunta 3, el empate cerca de n = 50 merece una frase más cuidadosa, porque ahí los tiempos son casi iguales.

## 2. Calidad de la explicación teórica (17 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término.
- Resuelve con el método maestro y llega a `Θ(n log n)`.
- Justifica el `Θ(n²)` de la fuerza bruta.

**Lo que puede mejorar:**
- Al verificar la condición del método maestro, diga claramente por qué se cumple el caso 2 (`f(n)` crece igual que `n^(log_b a)`), no solo que "corresponde".
- Explique de dónde sale el caso cruzado lineal y cuántos pares (i, j) hay exactamente en la fuerza bruta (`n(n+1)/2`).

## 3. Corrección de la implementación (24 / 25)
**Lo que hizo bien:**
- Las tres funciones respetan las firmas, resuelven los tres casos y no llaman a la fuerza bruta.
- No modifican la lista recibida y las pruebas cubren todos los casos pedidos, con 25 listas aleatorias.
- Código ordenado, con type hints y docstrings.

**Lo que puede mejorar:**
- En `pruebas.py` y `medicion.py`, las funciones `suma_de` y `medir` no indican el tipo del parámetro `algoritmo`.

## 4. Calidad del análisis de las gráficas (23 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda, ambas curvas en los mismos ejes y 7 tamaños.
- Calcula el factor al duplicar n (4000 a 8000): 3.81 para fuerza bruta y 2.04 para divide y vencerás, y los contrasta con la teoría.
- Incluye una tabla con los valores medidos y explica que repitió cada medición tres veces.

**Lo que puede mejorar:**
- Para `n log n` el factor esperado al duplicar es un poco mayor que 2 (cerca de 2.17); compare con ese número.

## 5. Documentación y organización del informe (10 / 10)
**Lo que hizo bien:**
- Estructura de carpetas correcta, `README.md` en el orden pedido, gráfica visible y enlaces al código en cada parte.
- Instrucciones de reproducción y varios commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden con listas aleatorias adicionales y `medicion.py` genera la gráfica sin errores.

## Para el próximo laboratorio
- Verifique explícitamente la condición del método maestro, paso a paso.
- Compare los factores medidos con el valor teórico exacto de cada complejidad.
- Anote los tipos de todos los parámetros de sus funciones auxiliares.
