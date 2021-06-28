import deap.algorithms
from deap import base
from deap import creator
from deap import tools

from utils import probability


class GeneticKnapsack:

    # Fitness function
    def fitness(self, ind):
        weight = 0.0
        value = 0.0
        for i in range(len(ind)):
            if ind[i]:
                value += self.all_items[i][1]
                weight += self.all_items[i][0]
            if weight > self.MAX_WEIGHT:
                value = -1
        return value, weight

    def __init__(self, max_weight, items):
        self.MAX_WEIGHT = max_weight
        self.all_items = items  # Set constraints and item list
        creator.create("Fitness", base.Fitness, weights=(1.0, -1.0))  # Create fitness
        creator.create("Individual", list, fitness=creator.Fitness)  # Create individual
        self.toolbox = base.Toolbox()
        self.toolbox.register("attr_item", probability, 0.023)  # Register Allele
        self.toolbox.register("individual", tools.initRepeat, creator.Individual,
                              self.toolbox.attr_item, len(items))  # Register individual
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)  # Register population
        self.toolbox.register("evaluate", self.fitness)
        self.toolbox.register("mate", tools.cxOnePoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        self.toolbox.register("select", tools.selTournament, tournsize=20)  # Register ga operators

    def solve(self, gens=100, inds=50, cxp=0.7, mtp=0.3, mu=20, l=80):
        NUMBER_GENERATIONS = gens
        NUMBER_INDIVIDUALS = inds
        CROSS_PROB = cxp
        MUT_PROB = mtp
        pop = self.toolbox.population(n=NUMBER_INDIVIDUALS)
        return deap.algorithms.eaMuCommaLambda(pop, self.toolbox, mu, l, CROSS_PROB, MUT_PROB, NUMBER_GENERATIONS,
                                               verbose=False)[0]
