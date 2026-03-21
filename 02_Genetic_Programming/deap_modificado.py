import operator
import math
import random
import numpy
from deap import algorithms, base, creator, tools, gp
import sympy

numpy.seterr(all='ignore')

# 1. Proteccion division entre 0
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

# 2. Creacion funciones matematicas basicas
def sq(x): return x**2
def cube(x): return x**3

pset = gp.PrimitiveSet("MAIN", 2)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(protectedDiv, 2)
pset.addPrimitive(operator.neg, 1)
# pset.addPrimitive(math.cos, 1)
# pset.addPrimitive(math.sin, 1)

# Funciones nuevas propuestas
pset.addEphemeralConstant("rand", lambda: random.randint(1, 5))
pset.addPrimitive(sq, 1)
pset.addPrimitive(cube, 1)

# Renombrar constante
pset.renameArguments(ARG0='x', ARG1='y')

# 3. Configuracion Fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

# 4. Configurar Toolbox
toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

def evalSymbReg(individual, points):
    func = toolbox.compile(expr=individual)
    try:
        # Usamos corchetes para evaluar todos los puntos aquí mismo
        sqerrors = [(func(x, y) - ((x**3) * 5 * (y**2) + x/2))**2 for x, y in points]
        return math.fsum(sqerrors) / len(points),
    except OverflowError:
        # Si la ecuación explota, le damos el peor puntaje posible (infinito)
        return float('inf'),

# Se genera una cuadrícula 2D de puntos (x, y) para evaluar la superficie
puntos_evaluacion = [(x/10., y/10.) for x in range(-10, 10) for y in range(-10, 10)]
toolbox.register("evaluate", evalSymbReg, points=puntos_evaluacion)
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

# Decoradores para limitar la altura del árbol
toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=6))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=6))

# 5. Ciclo principal
def main():
    random.seed(318)
    
    pop = toolbox.population(n=1000)
    hof = tools.HallOfFame(1)
    
    # Configurar las estadísticas para visualizar el progreso de cada generacion
    stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
    stats_size = tools.Statistics(len)
    mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
    mstats.register("avg", numpy.mean)
    mstats.register("std", numpy.std)
    mstats.register("min", numpy.min)
    mstats.register("max", numpy.max)
    
    print("Iniciando evolución con DEAP...")
    # eaSimple = algoritmo evolutivo básico
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.8, mutpb=0.1, ngen=200, 
                                stats=mstats, halloffame=hof, verbose=True)
    
    print("\n¡Evolución terminada!")
    print("Mejor individuo encontrado (Ecuación):")
    print(hof[0])
    
    print("\n--- Post-procesamiento: Simplificación Algebraica ---")
    # 1. Declaramos nuestras variables matemáticas reales
    x_sym, y_sym = sympy.symbols('x y')
    
    # 2. Diccionario para traducir el lenguaje de DEAP a matemáticas de SymPy
    mapeo_operaciones = {
        'add': lambda a, b: a + b,
        'sub': lambda a, b: a - b,
        'mul': lambda a, b: a * b,
        # Para la simplificación, tratamos la división protegida como una división normal
        'protectedDiv': lambda a, b: a / b, 
        'neg': lambda a: -a,
        'sq': lambda a: a**2,
        'cube': lambda a: a**3,
        'x': x_sym,
        'y': y_sym
    }
    
    try:
        # 3. Convertimos el texto del mejor individuo en una ecuación ejecutable
        ecuacion_cruda = eval(str(hof[0]), {"__builtins__": None}, mapeo_operaciones)
        
        # 4. Magia de SymPy: Expandimos y simplificamos los términos
        ecuacion_limpia = sympy.expand(ecuacion_cruda)
        
        print("Ecuación Original (Cruda):", str(hof[0]))
        print("\nEcuación Simplificada (SymPy):")
        print(ecuacion_limpia)
        
    except Exception as e:
        print("No se pudo simplificar matemáticamente:", e)

    return pop, log, hof

if __name__ == "__main__":
    main()