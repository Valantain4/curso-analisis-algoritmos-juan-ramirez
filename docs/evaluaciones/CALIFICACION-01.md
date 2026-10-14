# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Juan Andrés Ramírez Castañeda · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-14 23:59 · **Versión revisada:** commit `c4d6d36`

Muy buen trabajo: el informe y las mediciones son sólidos y se nota que entendió el caso.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 21 / 25 |
| Calidad de la explicación teórica | 20 / 25 |
| Corrección de la implementación | 17 / 20 |
| Calidad del análisis de las gráficas | 18 / 20 |
| Documentación y organización del informe | 10 / 10 |
| **Total** | **86 / 100** |
| **Nota (0–5)** | **4.30** |

## 1. Corrección conceptual (21 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que sea viable, y nombra la ventana de cuatro horas como la restricción que se incumple.
- Explica con números (20.000 a 1.200.000 registros, unas 3600 veces más trabajo) por qué un servidor el doble de rápido solo aplaza el problema.
- En la Parte 2 relaciona el tiempo de ejecución con el consumo de energía acumulado durante años, da dos perjuicios (paciente y operador) y reconoce que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- El segundo ejemplo (matrículas universitarias) es razonable, pero es una búsqueda y no tiene cifras claras de cuántos datos se recorren; dé números concretos de lo que se procesa.
- Al decir quién asume el costo, el caso del operador queda diluido ("nuevamente los pacientes"). Sea más preciso en qué pierde cada persona.

## 2. Calidad de la explicación teórica (20 / 25)
**Lo que hizo bien:**
- Define mejor, peor y promedio sobre entradas del mismo tamaño n, justifica usar el peor caso por la ventana estricta y deja la predicción escrita antes del experimento.
- Plantea la recurrencia de merge sort, explica cada término y la resuelve con el método maestro verificando la condición del caso 2.
- Incluye la tabla de complejidades.

**Lo que puede mejorar:**
- El análisis de insertion sort no se hizo línea a línea: faltó indicar cuántas veces se ejecuta cada línea de su código y sumar esos costos.
- El caso promedio de insertion sort se afirma sin explicarlo (por qué en promedio se desplaza cerca de la mitad).

## 3. Corrección de la implementación (17 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien de mayor a menor, no cambian la lista recibida, cuentan comparaciones entre elementos y no usan `sorted()` ni `sort()`.
- Los generadores dan listas del tamaño pedido, sin repetidos, y son reproducibles con semilla.

**Lo que puede mejorar:**
- Las funciones internas `mezclar` y `ordenar` de `merge_sort`, y `graficar`, no tienen docstring completo (faltan Args/Returns).
- En `medir_algoritmo`, el parámetro `algoritmo` no tiene *type hint*.

## 4. Calidad del análisis de las gráficas (18 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes rotulados, leyenda y curvas en los mismos ejes; coinciden con las cifras del informe (por ejemplo, C llega a unos 2.1 s en n = 6400).
- Identifica con evidencia C como peor caso, B como mejor y A como aproximación al promedio, y contrasta con su predicción.
- El concepto técnico recomienda merge sort, responde a la propuesta del servidor con datos medidos, estima la ventana de cuatro horas declarándola estimación y menciona la memoria adicional.

**Lo que puede mejorar:**
- Contraste de forma más explícita el resultado de la gráfica con las complejidades de 4.1 (por ejemplo, comparando cuánto crece cada curva al doblar n).
- Discuta también la estabilidad o el riesgo de que el escenario B deje de ser casi ordenado con datos medidos.

## 5. Documentación y organización del informe (10 / 10)
- Carpeta en `laboratorios/lab1-fundamentos-complejidad-recurrencias/`, ubicación válida, con todos los archivos pedidos.
- Informe por partes, gráficas visibles, enlaces al código en cada parte, instrucciones de reproducción y cinco commits con mensajes descriptivos.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, ordenan bien y regeneran las tres gráficas con resultados parecidos a los publicados.

## Para el próximo laboratorio
- Cuando se pida un análisis línea a línea, escriba una tabla con cuántas veces se ejecuta cada línea y súmelas.
- Dé cifras concretas (cantidad de datos y restricción) en los ejemplos propios.
- Ponga docstring completo y *type hints* en todas las funciones, incluidas las internas.
- Contraste siempre lo medido con la complejidad calculada usando números de la gráfica.
