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

print("=== Inicio de la Optimización PSO Global ===")

# --- 4. Ciclo de iteraciones ---
for t in range(iteraciones):
    print(f"\n--- Iteración {t + 1} ---")
    
    for i in range(N):
        # Generar r1 y r2 aleatorios en [0, 1] en cada paso
        r1 = np.random.uniform(0, 1)
        r2 = np.random.uniform(0, 1)

        # i. Actualizar la velocidad de la partícula
        # En la iteración 1, velocidades[i] es 0, así que el término (a * velocidades[i]) se anula.
        velocidades[i] = (a * velocidades[i] +
                        b1 * r1 * (pbest_pos[i] - posiciones[i]) +
                        b2 * r2 * (gbest_pos - posiciones[i]))

        # ii. Actualizar la posición de la partícula
        posiciones[i] = posiciones[i] + velocidades[i]

        # Mantener las partículas estrictamente dentro de los límites (-5, 5)
        posiciones[i] = np.clip(posiciones[i], -5, 5)

        # iii. Evaluar la función de aptitud con la nueva posición
        aptitud_actual = funcion_objetivo(posiciones[i][0], posiciones[i][1])

        # iv. Actualizar los mejores valores (pbest y gbest)
        if aptitud_actual < pbest_val[i]:
            pbest_val[i] = aptitud_actual
            pbest_pos[i] = np.copy(posiciones[i])

        if aptitud_actual < gbest_val:
            gbest_val = aptitud_actual
            gbest_pos = np.copy(posiciones[i])

        # 5. Imprimir lo solicitado por las instrucciones
        print(f"Partícula {i+1:02d} | "
            f"Posición: [{posiciones[i][0]: 7.4f}, {posiciones[i][1]: 7.4f}] | "
            f"Velocidad: [{velocidades[i][0]: 7.4f}, {velocidades[i][1]: 7.4f}] | "
            f"pbest: {pbest_val[i]: 7.4f} | "
            f"gbest: {gbest_val: 7.4f}")

print("\n=== Resultado Final ===")
print(f"Mejor valor mínimo encontrado (gbest): {gbest_val:.4f}")
print(f"Coordenadas del mínimo: X = {gbest_pos[0]:.4f}, Y = {gbest_pos[1]:.4f}")