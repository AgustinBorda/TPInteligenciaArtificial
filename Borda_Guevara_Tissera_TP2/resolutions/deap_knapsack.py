import deap.algorithms
from deap import base
from deap import creator
from deap import tools


import random

from utils import probability


class GeneticKnapsack:

    def fitness(self, ind):
        weight = 0.0
        value = 0.0
        for i in range(len(ind)):
            if ind[i] == 1:
                value += self.all_items[i][1]
                weight += self.all_items[i][0]
        if weight >= self.MAX_WEIGHT:
            weight = weight * 10000
            value = -value
        return weight, value

    def __init__(self, max_weight, items):
        self.MAX_WEIGHT = max_weight
        self.all_items = items
        creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
        creator.create("Individual", list, fitness=creator.Fitness)
        self.toolbox = base.Toolbox()
        self.toolbox.register("attr_item", probability, 0.001)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual,
                              self.toolbox.attr_item, len(items))
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("evaluate", self.fitness)
        self.toolbox.register("mate", tools.cxOnePoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.01)
        self.toolbox.register("select", tools.selNSGA2)

    def solve(self):
        NUMBER_GENERATIONS = 1000
        NUMBER_INDIVIDUALS = 50
        CROSS_PROB = 0.7
        MUT_PROB = 0.1
        pop = self.toolbox.population(n=NUMBER_INDIVIDUALS)
        hall_of_fame = tools.HallOfFame(NUMBER_INDIVIDUALS)
        return deap.algorithms.eaSimple(pop, self.toolbox, CROSS_PROB, MUT_PROB,
                                        NUMBER_GENERATIONS, halloffame=hall_of_fame)[0]

