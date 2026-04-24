import random

# ==========================================
# 1. DEFINICIÓN DE DATOS Y PARÁMETROS
# ==========================================

# Matriz de adyacencia (distancias entre ciudades)
distancias = [
    [0,  6,  9, 17, 13, 21],
    [6,  0, 19, 21, 12, 18],
    [9, 19,  0, 20, 23, 11],
    [17, 21, 20,  0, 15, 10],
    [13, 12, 23, 15,  0, 21],
    [21, 18, 11, 10, 21,  0]
]

NUM_CIUDADES = len(distancias) 
NUM_HORMIGAS = NUM_CIUDADES   # 1 hormiga por cada nodo (o ciudad)

RHO = 0.2                     # Tasa de evaporación
Q = 1.0                       # Constante de depósito
ALPHA = 1.5                   # Importancia de la feromona (a)
BETA = 0.8                    # Importancia de la visibilidad/heurística (b)

ITERACIONES = 50              # Número de iteraciones
FEROMONA_INICIAL = 0.1        # Valor inicial positivo y pequeño

# ==========================================
# 2. FUNCIONES DE INICIALIZACIÓN
# ==========================================

def inicializar_feromonas():
    """Crea la matriz de feromonas con el valor inicial."""
    return [[FEROMONA_INICIAL for _ in range(NUM_CIUDADES)] for _ in range(NUM_CIUDADES)]


def calcular_visibilidad():
    """Calcula la matriz heurística (1 / distancia) - LETRA "eta". 
    Si es 0, la visibilidad es 0."""
    visibilidad = [[0.0 for _ in range(NUM_CIUDADES)] for _ in range(NUM_CIUDADES)]
    for i in range(NUM_CIUDADES):
        for j in range(NUM_CIUDADES):
            if i != j and distancias[i][j] > 0:
                visibilidad[i][j] = 1.0 / distancias[i][j]
    return visibilidad

# ==========================================
# 3. FUNCIONES DE TRANSICIÓN Y RUTAS
# ==========================================

def seleccionar_siguiente_ciudad(ciudad_actual, visitadas, feromonas, visibilidad):
    """Selecciona la siguiente ciudad usando el método de la ruleta."""
    probabilidades = []
    suma_total = 0.0
    
    # Calcular el numerador de la fórmula de transición para ciudades no visitadas
    for j in range(NUM_CIUDADES):
        if j not in visitadas:
            tau = feromonas[ciudad_actual][j] ** ALPHA
            eta = visibilidad[ciudad_actual][j] ** BETA
            valor = tau * eta
            probabilidades.append((j, valor))
            suma_total += valor

    # Si por alguna razón no hay opciones válidas, tomar una al azar (prevención de errores)
    if suma_total == 0:
        no_visitadas = [j for j in range(NUM_CIUDADES) if j not in visitadas]
        return random.choice(no_visitadas)
        
    # Selección por Ruleta
    limite = random.uniform(0, suma_total)
    suma_acumulada = 0.0
    
    for ciudad, probabilidad in probabilidades:
        suma_acumulada += probabilidad
        if suma_acumulada >= limite:
            return ciudad
            
    '''Si limite y suma_acumulada son iguales y por culpa del redondeo
    suma_acumulada no alcanza a ser mayor que limite se debe retornar
    el ultimo termino''' 
    return probabilidades[-1][0]

def calcular_distancia_ruta(ruta):
    """Calcula la distancia total de una ruta construida."""
    distancia_total = 0
    for i in range(len(ruta) - 1):
        distancia_total += distancias[ruta[i]][ruta[i+1]]
    return distancia_total

# ==========================================
# 4. ACTUALIZACIÓN DE FEROMONAS
# ==========================================

def actualizar_feromonas(feromonas, todas_las_rutas, distancias_rutas):
    """Evapora feromonas viejas y deposita nuevas según la calidad de las rutas."""
    # 1. Evaporación
    for i in range(NUM_CIUDADES):
        for j in range(NUM_CIUDADES):
            feromonas[i][j] = (1 - RHO) * feromonas[i][j]
            
    # 2. Depósito de nuevas feromonas
    for k in range(NUM_HORMIGAS):
        ruta = todas_las_rutas[k]
        longitud_ruta = distancias_rutas[k]
        aporte = Q / longitud_ruta
        
        # Depositar en cada arista recorrida (y su inverso, al ser grafo no dirigido)
        for i in range(len(ruta) - 1):
            origen = ruta[i]
            destino = ruta[i+1]
            feromonas[origen][destino] += aporte
            feromonas[destino][origen] += aporte # Simetría
            
    return feromonas

# ==========================================
# 5. BUCLE PRINCIPAL (ACO)
# ==========================================

def ejecutar_aco():
    feromonas = inicializar_feromonas()
    visibilidad = calcular_visibilidad()
    
    mejor_ruta_global = None
    mejor_distancia_global = float('inf')
    
    for iteracion in range(ITERACIONES):
        todas_las_rutas = []
        distancias_rutas = []
        
        # Cada hormiga sale de una ciudad diferente (0 a 5)
        for k in range(NUM_HORMIGAS):
            ciudad_origen = k 
            ruta_actual = [ciudad_origen]
            visitadas = set([ciudad_origen])
            ciudad_actual = ciudad_origen
            
            # Construir ruta recorriendo todas las ciudades
            while len(visitadas) < NUM_CIUDADES:
                siguiente_ciudad = seleccionar_siguiente_ciudad(ciudad_actual, visitadas, feromonas, visibilidad)
                ruta_actual.append(siguiente_ciudad)
                visitadas.add(siguiente_ciudad)
                ciudad_actual = siguiente_ciudad
                
            # Regresar a la ciudad de origen
            ruta_actual.append(ciudad_origen)
            
            # Guardar la ruta y su longitud
            distancia = calcular_distancia_ruta(ruta_actual)
            todas_las_rutas.append(ruta_actual)
            distancias_rutas.append(distancia)
            
            # Actualizar el mejor global
            if distancia < mejor_distancia_global:
                mejor_distancia_global = distancia
                mejor_ruta_global = list(ruta_actual)
                
        # Actualizar matriz de feromonas al final de cada caminata
        feromonas = actualizar_feromonas(feromonas, todas_las_rutas, distancias_rutas)
        
        print(f"Iteración {iteracion + 1:02d} | Mejor distancia actual: {mejor_distancia_global}")

    # Ajustar para mostrar ciudades del 1 al 6 (en lugar de 0 a 5)
    ruta_legible = [ciudad + 1 for ciudad in mejor_ruta_global]

    print("\n" + "="*40)
    print("RESULTADO FINAL")
    print("="*40)
    print(f"Mejor ruta encontrada: {ruta_legible}")
    print(f"Distancia mínima: {mejor_distancia_global}")

# ==========================================
# EJECUCIÓN DEL SCRIPT
# ==========================================
if __name__ == "__main__":
    ejecutar_aco()