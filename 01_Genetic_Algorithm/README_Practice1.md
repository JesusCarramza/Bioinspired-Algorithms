# Práctica 1: Algoritmos Genéticos - El Problema de la Mochila 🧙‍♂️🎒

## 📝 Descripción del Problema

Esta primera práctica consiste en resolver una variante del clásico "Problema de la Mochila" (Knapsack Problem) utilizando un Algoritmo Genético.

El contexto del problema se centra en Fred y George Weasley, quienes se preparan para un nuevo trimestre en la escuela Hogwarts. Ellos están planeando vender los nuevos productos de su tienda de bromas a los estudiantes de la escuela. Para obtener las mayores ganancias posibles, deben preparar una mochila con la mayor cantidad de productos. Como su madre les ha prohibido vender estos productos, deben llevarlos escondidos en una mochila pequeña.

### ⚖️ Restricciones del Inventario
- **Capacidad de la mochila:** 30 libras.
- **Stock disponible:** Tienen 10 productos de cada tipo actualmente.
- **Reglas de negocio:** Han decidido que deben empacar obligatoriamente al menos 3 pociones de amor (Love Potion) y al menos 2 cajas surtidas (Skiving Snackbox).

### 📦 Catálogo de Productos
Se deben empacar los siguientes artículos, buscando maximizar el valor total en galleons sin superar el peso máximo:
- **Decoy Detonators:** Peso: 4 libras | Precio: 10 galleons.
- **Fever Fudge:** Peso: 2 libras | Precio: 3 galleons.
- **Love Potion:** Peso: 2 libras | Precio: 8 galleons.
- **Puking Pastilles:** Peso: 1.5 libras | Precio: 2 galleons.
- **Extendable Ears:** Peso: 5 libras | Precio: 12 galleons.
- **Nosebleed Nougat:** Peso: 1 libras | Precio: 2 galleons.
- **Skiving Snackbox:** Peso: 5 libras | Precio: 6 galleons.

(Nota: El documento original con las instrucciones de la práctica se encuentra adjunto en este repositorio y en esta direccion, se encuentra como `Practice_1.pdf`).

## ⚙️ Parámetros del Algoritmo
Para la solución, el algoritmo genético fue diseñado cumpliendo con la siguiente tabla de parámetros:
- **Población:** 10 cromosomas.
- **Generaciones:** 50.
- **Probabilidad de cruza:** 0.85.
- **Probabilidad de mutación:** 0.1.
- **Selección de padres:** Ruleta.
- **Método de cruza:** Cruza uniforme (u =< 0.5).
- **Método de mutación:** Mutación uniforme.
- **Selección de sobreviviente:** Generacional con reemplazo del padre más débil.

## 🧠 Desarrollo y Abordaje del Problema
Para traducir este problema biológico y matemático a código Python, el desarrollo se dividió en las siguientes fases lógicas:

**1. Representación del Cromosoma (Individuo)**

Se decidió utilizar un arreglo (lista) de 7 posiciones (una para cada tipo de producto). El valor numérico en cada índice representa la cantidad de ese producto que se empacará en la mochila (valores enteros del 0 al 10).

- Para evitar procesar generaciones llenas de individuos inviables, la función de generación inicial (`generar_cromosoma`) utiliza un enfoque de muestreo por rechazo: crea individuos aleatorios, asegurando que desde su nacimiento tengan las cantidades mínimas requeridas (3 Love Potions y 2 Skiving Snackbox) y no excedan las 30 libras.

**2. Función de Aptitud (Fitness) y Penalizaciones**

La función `calcular_aptitud` es el núcleo de la evaluación. Multiplica la cantidad de cada producto por su valor en galleons.

- **Manejo de infractores:** Si durante las iteraciones de cruza/mutación un individuo supera el peso de 30 libras o pierde las cantidades mínimas obligatorias, se le asigna una aptitud casi nula (`0.01`). Esto es una penalización severa que asegura que estos individuos tengan casi cero por ciento de probabilidad de ser elegidos en la ruleta, "muriendo" y desapareciendo del pool genético sin romper los cálculos de probabilidad.

**3. Selección y Operadores Genéticos**

- **Ruleta:** Se programó una función que calcula la probabilidad de selección acumulada (`P_sel_acum`). Los individuos más valiosos ocupan un mayor "porcentaje" de la ruleta, garantizando la supervivencia de los más aptos.

- **Cruza Uniforme:** Dado un número aleatorio, el gen (cantidad de un producto) tiene un 50% de probabilidad de heredarse del Padre 1 o del Padre 2.

- **Mutación Uniforme:** Se iteran los genes del individuo mutado. Existe un 10% de probabilidad en cada gen de que su valor cambie por uno completamente nuevo (respetando siempre los mínimos obligatorios para no corromper la genética base).

4. Ciclo Generacional y Reemplazo

En el ciclo principal, se crean nuevas poblaciones de 10 individuos. En lugar de un reemplazo tradicional ciego, se implementó una **evaluación familiar** para cumplir con la regla de reemplazo: de los 2 padres originales y los 2 hijos generados, se ordenan por aptitud y solo los 2 mejores avanzan a la siguiente generación. Esto asegura un progreso monotónico (la población nunca empeora de una generación a otra).

## 🚀 Cómo ejecutar la práctica

1. Clona este repositorio en tu máquina local.

2. Navega mediante la terminal a esta carpeta (`01_Genetic_Algorithm`).

3. Ejecuta el script de Python:

```Bash
python solution_practice_1.py
```

4. El programa limpiará la consola automáticamente y mostrará el arreglo con la mejor combinación encontrada, la ganancia total obtenida en Galleons y el peso final que ocupan en la mochila.