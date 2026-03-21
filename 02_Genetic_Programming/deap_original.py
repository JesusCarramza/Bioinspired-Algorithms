import operator
import math
import random
import numpy
from deap import algorithms, base, creator, tools, gp

# 1. Proteccion division entre 0
def protectedDiv(left, right):
    try:
        return left / right
    except ZeroDivisionError:
        return 1

# 2. Creacion funciones matematicas basicas
pset = gp.PrimitiveSet("MAIN", 1)
pset.addPrimitive(operator.add, 2)
pset.addPrimitive(operator.sub, 2)
pset.addPrimitive(operator.mul, 2)
pset.addPrimitive(protectedDiv, 2)
pset.addPrimitive(operator.neg, 1)
pset.addPrimitive(math.cos, 1)
pset.addPrimitive(math.sin, 1)

# Renombrar constante
pset.renameArguments(ARG0='x')

# 3. Configuracion Fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMin)

# 4. Configurar Toolbox
toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

# Función de evaluación (Calculo  ECM (Error Cuadrático Medio))
def evalSymbReg(individual, points):
    func = toolbox.compile(expr=individual)
    sqerrors = ((func(x) - x**4 - x**3 - x**2 - x)**2 for x in points)
    return math.fsum(sqerrors) / len(points),

toolbox.register("evaluate", evalSymbReg, points=[x/10. for x in range(-10,10)])
toolbox.register("select", tools.selTournament, tournsize=3)
toolbox.register("mate", gp.cxOnePoint)
toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

# Decoradores para limitar la altura del árbol
toolbox.decorate("mate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))
toolbox.decorate("mutate", gp.staticLimit(key=operator.attrgetter("height"), max_value=17))

# 5. Ciclo principal
def main():
    random.seed(318)
    
    pop = toolbox.population(n=300)
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
    pop, log = algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.1, ngen=40, 
                                stats=mstats, halloffame=hof, verbose=True)
    
    print("\n¡Evolución terminada!")
    print("Mejor individuo encontrado (Ecuación):")
    print(hof[0])
    
    return pop, log, hof

if __name__ == "__main__":
    main()