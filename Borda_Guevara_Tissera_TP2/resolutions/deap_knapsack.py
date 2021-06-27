import deap.algorithms
from deap import base
from deap import creator
from deap import tools


from utils import probability


class GeneticKnapsack:

    def fitness(self, ind):
        weight = 0.0
        value = 0.0
        for i in range(len(ind)):
            if ind[i]:
                value += self.all_items[i][1]
                weight += self.all_items[i][0]
            if weight > self.MAX_WEIGHT:
                value = -1
        return value, 1/(weight+1)

    def __init__(self, max_weight, items):
        self.MAX_WEIGHT = max_weight
        self.all_items = items
        creator.create("Fitness", base.Fitness, weights=(1.0, 1.0))
        creator.create("Individual", list, fitness=creator.Fitness)
        self.toolbox = base.Toolbox()
        self.toolbox.register("attr_item", probability, 0)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual,
                              self.toolbox.attr_item, len(items))
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)
        self.toolbox.register("evaluate", self.fitness)
        self.toolbox.register("mate", tools.cxOnePoint)
        self.toolbox.register("mutate", tools.mutFlipBit, indpb=0.1)
        self.toolbox.register("select", tools.selTournament, tournsize=20)

    def solve(self, gens=500, inds=100, cxp=0.7, mtp=0.3):
        NUMBER_GENERATIONS = gens
        NUMBER_INDIVIDUALS = inds
        CROSS_PROB = cxp
        MUT_PROB = mtp
        pop = self.toolbox.population(n=NUMBER_INDIVIDUALS)
        hall_of_fame = tools.HallOfFame(NUMBER_INDIVIDUALS)
        return deap.algorithms.eaSimple(pop, self.toolbox, CROSS_PROB, MUT_PROB,
                                        NUMBER_GENERATIONS, halloffame=hall_of_fame, verbose=False)[0]

