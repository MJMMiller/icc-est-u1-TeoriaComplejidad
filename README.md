# 🧪 Teoría de la Complejidad: Análisis de Algoritmos de Ordenamiento

## 📌 Información General

* **Título:** Comparación de Algoritmos de Ordenamiento - Tiempos de Ejecución
* **Asignatura:** Estructura de Datos
* **Carrera:** Computación
* **Estudiantes:** Nicolas Cedillo & Mateo Miller
* **Fecha:** 11 / 05 / 2025
* **Profesor:** Pablo Torres

---

## 🛠️ Descripción

Este proyecto en Python evalúa y compara el rendimiento de distintos algoritmos de ordenamiento (`Burbuja`, `Burbuja con Ajuste`, `Selección`, `Inserción` y `Shell`) mediante la medición del tiempo que cada uno tarda en ordenar conjuntos de números aleatorios.

El objetivo principal es analizar su complejidad temporal utilizando arreglos de distintos tamaños:

* 5.000
* 10.000
* 30.000
* 50.000
* 100.000

El sistema garantiza la equidad en las pruebas: todos los algoritmos se ejecutan sobre los mismos datos usando copias del arreglo original.
---

## 🗂️ Diagrama
![](https://raw.githubusercontent.com/MJMMiller/EST_DIAGRAMS/refs/heads/main/Teoria%20de%20la%20complejidad.png)

---

## 🌱 Estructura del Proyecto

```bash
ordenamiento_project/
│
├── app.py                # Script principal: ejecuta las pruebas y muestra resultados
├── benchMarking.py       # Módulo encargado de medir y registrar los tiempos
└── sortMethods.py        # Implementaciones de los algoritmos de ordenamiento
```

---

## 🚀 Ejecución

Asegúrate de tener Python 3.10 o superior.

Ejecuta el script principal:

```bash
python app.py
```

Verás una salida como:

```yaml
Tamaño: 5000, Algoritmo: burbuja, Tiempo: 1.234 segundos
Tamaño: 5000, Algoritmo: burbuja_mejorado, Tiempo: 0.954 segundos
Tamaño: 5000, Algoritmo: seleccion, Tiempo: 0.678 segundos
Tamaño: 5000, Algoritmo: insercion, Tiempo: 0.712 segundos
Tamaño: 5000, Algoritmo: shell, Tiempo: 0.087 segundos
```

---

## 🖼️ Captura de Resultados

Muestra la ejecución real del programa con tiempos de cada algoritmo impreso en consola. Sirve como evidencia del funcionamiento y comparación directa de los resultados obtenidos.

![](https://raw.githubusercontent.com/MJMMiller/EST_RESULTADOS/refs/heads/main/Captura%20de%20Resultados%20-%20Analisis%20de%20complejidad.jpg)
  
---

## 📈 Gráfica Comparativa

Se generó una gráfica de líneas en la que:

* El eje X representa la cantidad de elementos del arreglo.
* El eje Y muestra el tiempo de ejecución en segundos.
* Se trazó una línea por cada algoritmo.
  
![](https://raw.githubusercontent.com/MJMMiller/EST_RESULTADOS/refs/heads/main/Gr%C3%A1fica%20Comparativa%20-%20Analisis%20Complejidad.jpg)

---

## 🧮 Tabla de Resultados

| Tamaño | Burbuja (s) | Burbuja Ajuste (s) | Selección (s) | Inserción (s) | Shell (s) |
| ------ | ----------- | ------------------ | ------------- | ------------- | --------- |
| 5000   | 1.234       | 0.954              | 0.678         | 0.712         | 0.087     |
| 10000  | 5.821       | 4.392              | 3.445         | 3.212         | 0.169     |
| 30000  | 72.05       | 80.36              | 33.17         | 30.04         | 0.155     |
| 50000  | 199.6       | 206.3              | 90.28         | 83.54         | 0.305     |
| 100000 | 935.9       | 999.0              | 518.1         | 418.0         | 1.016     |

---

## 📚 Tecnologías Utilizadas

* **Lenguaje de Programación:** Python

* **Librerías:**

  * `time` (para medir ejecución)
  * `matplotlib` (para graficar resultados)
  * `random` (para generación de datos aleatorios)
  * `copy` (para clonar arreglos entre pruebas)
    
---

## ✅ Resultados Obtenidos

* Se implementaron correctamente 5 algoritmos de ordenamiento clásicos.
* Se generaron arreglos de prueba con crecimiento incremental.
* Se ejecutaron pruebas múltiples sobre los mismos datos para garantizar resultados imparciales.
* Se midieron y graficaron los tiempos para comparar su rendimiento.

---

## 📌 Conclusion Nicolas Cedillo

En base a los datos obtenidos, es claramente visible que el método Shell es el más efectivo, pues tiene un O(n log n), seguido por el selección e inserción, ambos con un O(n^2), y por último los métodos burbuja, con un O(n^2). A pesar que los 4 últimos tienen el mismo  O(n^2), depende mucho del orden en que se encuentren los datos del arreglo, y pueden llegar a ser uno mejor que otro en ciertas ocasiones, pero aún así el método Shell los supera por mucho.

---

## 📌 Conclusion Mateo Miller

Los métodos de Burbuja y Selección son ineficientes para grandes volúmenes de datos debido a su complejidad O(n²). Inserción, aunque también O(n²) en el peor caso, es más eficiente con datos casi ordenados. Shell, ofrece mejor rendimiento, con una complejidad variable entre O(n) y O(n²), dependiendo de la teoría de gaps lo que lo hace más eficiente en grandes conjuntos de datos.

---

## 🧠 Recomendaciones

* Priorizar algoritmos eficientes para datos grandes.
* Validar que cada método reciba una copia del arreglo original para evitar pruebas incorrectas.
* Implementar visualizaciones para facilitar el análisis comparativo.

---

## 👥 Colaboradores

* **Nicolas Cedillo** - [@nicolascedillo](https://github.com/nicolascedillo)
* **Mateo Miller** - [@MJMMiller](https://github.com/MJMMiller)

---
