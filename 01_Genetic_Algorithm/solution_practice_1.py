import random
import os

# Limpieza del entorno
# 'nt' corresponde a arquitecturas Windows (cls), entornos POSIX (macOS/Linux) usan 'clear'
CLEAR_CMD = 'cls' if os.name == 'nt' else 'clear'

# Colores en la salida del terminal
class Color:
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    RESET = '\033[0m'

# --- DEFINICIÓN DEL PROBLEMA ---
# Índices:
# 0: Decoy Detonators [w: 4, v: 10]
# 1: Fever Fudge [w: 2, v: 3]
# 2: Love Potion [w: 2, v: 8]
# 3: Puking Pastilles [w: 1.5, v: 2]
# 4: Extendable Ears [w: 5, v: 12]
# 5: Nosebleed Nougat [w: 1, v: 2]
# 6: Skiving Snackbox [w: 5, v: 6]

pesos = [4, 2, 2, 1.5, 5, 1, 5]
valores = [10, 3, 8, 2, 12, 2, 6]

# Restricciones
MAX_PESO = 30
MAX_CANTIDAD = 10
CANTIDAD_MINIMA = [0, 0, 3, 0, 0, 0, 2] # Restricciones de Love Potion y Skiving Snackbox

# Parámetros del AG
POBLACION_TAM = 10
GENERACIONES = 50
PROB_CRUZA = 0.85
PROB_MUTACION = 0.1

def generar_cromosoma():
    """
    Genera un cromosoma válido mediante muestreo por rechazo.
    Garantiza que el individuo cumpla con las restricciones de peso máximo 
    y el inventario mínimo antes de integrarse a la población inicial.
    """
    while True:
        # 1. Generar candidato con las restricciones de cantidad
        candidato = [random.randint(CANTIDAD_MINIMA[i], MAX_CANTIDAD) for i in range(7)]
        
        # 2. Calcular su peso total
        peso_total = sum(candidato[i] * pesos[i] for i in range(7))
        
        # 3. Condición de aceptación: Si el peso es válido, se retorna.
        # Si excede MAX_PESO, el ciclo repite el proceso y genera uno nuevo.
        if peso_total <= MAX_PESO:
            return candidato

