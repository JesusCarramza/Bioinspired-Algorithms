import numpy as np

# --- 1. Definir parámetros de ejecución ---
N = 20           # Número de partículas
iteraciones = 50 # Número de iteraciones
a = 0.4          # Inercia
b1 = 0.7         # Aprendizaje local (Influencia propia)
b2 = 1.2         # Aprendizaje global (Influencia social)

# --- 2. Definir función objetivo ---
def funcion_objetivo(x, y):
    # f(x,y) = x^2 + y^2 + [25 * (senx + seny)]
    return x**2 + y**2 + 25 * (np.sin(x) + np.sin(y))

