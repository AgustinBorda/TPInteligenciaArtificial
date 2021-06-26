import deap.algorithms
from deap import base
from deap import creator
from deap import tools
from deap.algorithms import eaSimple

import random


class GeneticKnapsack:

    def fitness(self, ind):
        weight = 0.0
        value = 0.0
        for item in ind:
            value += self.all_items[item][1]
            weight += self.all_items[item][0]
        if weight >= self.MAX_WEIGHT:
            return weight * 2, value * 0.5  # Penalize the individual if isn't valid
        return weight, value

    def crossover(self, ind1, ind2):
        cut = random.uniform(0, min(len(ind1), len(ind2)))
        son = set()
        for i in range(0, cut):
            son.add(ind1[i])
        for i in range(cut, len(ind2)):
            son.add(ind2[i])
        return son

    def mutation(self, ind):
        if random.uniform(0, 1) < 0.5 and len(ind) == 0:
            ind.remove(random.uniform(0, len(ind)))
        else:
            ind.add(random.uniform(0, len(self.all_items)))
        return ind

    def __init__(self, max_weight, items):
        self.MAX_WEIGHT = max_weight
        self.all_items = items
        creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
        creator.create("Individual", set, fitness=creator.Fitness)
        self.toolbox = base.Toolbox()
        self.toolbox.register("attr_item", random.randrange)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual,
                              self.toolbox.attr_item, n=5000)
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("evaluate", self.fitness)
        self.toolbox.register("mate", self.crossover)
        self.toolbox.register("mutate", self.mutation)
        self.toolbox.register("select", tools.selNSGA2)

    def solve(self):
        NUMBER_GENERATIONS = 100
        NUMBER_INDIVIDUALS = 50
        CROSS_PROB = 0.7
        MUT_PROB = 0.3
        pop = self.toolbox.population(n=NUMBER_INDIVIDUALS)
        hall_of_fame = tools.HallOfFame(NUMBER_INDIVIDUALS)
        deap.algorithms.eaSimple(pop, self.toolbox, CROSS_PROB, MUT_PROB, NUMBER_GENERATIONS, halloffame=hall_of_fame)
        return pop
