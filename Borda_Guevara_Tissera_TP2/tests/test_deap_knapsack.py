from Borda_Guevara_Tissera_TP2.resolutions.deap_knapsack import GeneticKnapsack
from Borda_Guevara_Tissera_TP2.tests.test_knapsack import open_file


def test_knapsack_genetic_algorithm_large_scale_1():
    params = open_file("../dataset/large_scale/knapPI_1_200_1000_1")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve()
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_200_1000_1").readline()))
    assert optimum == 11238
