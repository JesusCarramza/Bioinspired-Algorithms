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

# --- 3. Inicialización aleatoria de posiciones y VELOCIDAD CERO ---
# Las posiciones deben estar en el intervalo (-5, 5)
posiciones = np.random.uniform(-5, 5, (N, 2))

# Velocidad inicial en 0 para todas las partículas
velocidades = np.zeros((N, 2))

# Inicialización de pbest (mejor posición propia)
pbest_pos = np.copy(posiciones)
pbest_val = np.array([funcion_objetivo(p[0], p[1]) for p in posiciones])

# Inicialización de gbest (mejor posición global para minimización)
gbest_idx = np.argmin(pbest_val)
gbest_pos = np.copy(pbest_pos[gbest_idx])
gbest_val = pbest_val[gbest_idx]

