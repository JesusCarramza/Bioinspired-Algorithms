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

def calcular_aptitud(cromosoma):
    """Calcula el valor total. Aplica penalización severa si excede el peso o incumple mínimos."""
    peso_total = sum(cromosoma[i] * pesos[i] for i in range(7))
    valor_total = sum(cromosoma[i] * valores[i] for i in range(7))
    
    # Verificar restricciones
    if peso_total > MAX_PESO:
        return 0.01 # Penalización por exceder peso (usamos 0.01 para no romper la ruleta)
    
    for i in range(7):
        if cromosoma[i] < CANTIDAD_MINIMA[i] or cromosoma[i] > MAX_CANTIDAD:
            return 0.01 # Penalización por ser mayor a la cantidad maxima o menor a la cantidad minima
            
    return valor_total

def seleccion_ruleta(poblacion, aptitudes):
    """Selección proporcional (Ruleta) calculando P_sel y P_sel_acum."""
    # 1. Calcular el Total de las aptitudes
    total_aptitud = sum(aptitudes)
    
    # 2. Calcular P_sel para cada individuo: f(x) / Total
    p_sel = [aptitud / total_aptitud for aptitud in aptitudes]
    
    # 3. Calcular P_sel_acum (Suma acumulada de P_sel)
    p_sel_acum = []
    acumulado = 0.0
    for p in p_sel:
        acumulado += p
        p_sel_acum.append(acumulado)
        
    # 4. Generar número aleatorio r con distribución uniforme continua
    r = random.uniform(0, 1)
    
    # 5. Seleccionar al individuo evaluando r contra P_sel_acum
    for i, p_acum in enumerate(p_sel_acum):
        if r <= p_acum:
            return poblacion[i]

def cruza_uniforme(padre1, padre2):
    """
    Ejecuta la cruza uniforme gen a gen asumiendo que la probabilidad ya se cumplió.
    """
    hijo1, hijo2 = [], []
    for i in range(7):
        u = random.uniform(0, 1)
        if u <= 0.5:
            hijo1.append(padre1[i])
            hijo2.append(padre2[i])
        else:
            hijo1.append(padre2[i])
            hijo2.append(padre1[i])
    return hijo1, hijo2

def mutacion_uniforme(cromosoma):
    """Mutación uniforme: evalúa la probabilidad de mutación gen por gen."""
    for i in range(len(cromosoma)):
        # Se genera un número aleatorio entre 0 y 1 por cada gen
        if random.uniform(0, 1) < PROB_MUTACION:
            # Se muta el gen asignando un nuevo valor entre 0 y 10.
            # Se mantiene CANTIDAD_MINIMA para no generar individuos inválidos de origen.
            cromosoma[i] = random.randint(CANTIDAD_MINIMA[i], MAX_CANTIDAD)
    return cromosoma