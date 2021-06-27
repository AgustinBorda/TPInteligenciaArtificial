from Borda_Guevara_Tissera_TP2.resolutions.deap_knapsack import GeneticKnapsack
from Borda_Guevara_Tissera_TP2.tests.test_knapsack import open_file


def test_knapsack_genetic_algorithm_low_dimensional_1():
    params = open_file("../dataset/low-dimensional/f1_l-d_kp_10_269")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve()
    optimum = int((open("../dataset/low-dimensional-optimum/f1_l-d_kp_10_269").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 295
    assert result[0].fitness.values[0] <= optimum
    assert result[0].fitness.values[0] >= 294


def test_knapsack_genetic_algorithm_low_dimensional_2():
    params = open_file("../dataset/low-dimensional/f2_l-d_kp_20_878")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve()
    optimum = int((open("../dataset/low-dimensional-optimum/f2_l-d_kp_20_878").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 1024
    assert result[0].fitness.values[0] == optimum


def test_knapsack_genetic_algorithm_low_dimensional_3():
    params = open_file("../dataset/low-dimensional/f3_l-d_kp_4_20")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve()
    optimum = int((open("../dataset/low-dimensional-optimum/f3_l-d_kp_4_20").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 35
    assert result[0].fitness.values[0] == optimum


def test_knapsack_genetic_algorithm_low_dimensional_4():
    params = open_file("../dataset/low-dimensional/f4_l-d_kp_4_11")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve()
    optimum = int((open("../dataset/low-dimensional-optimum/f4_l-d_kp_4_11").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 23
    assert result[0].fitness.values[0] <= optimum
    assert result[0].fitness.values[0] >= 22


def test_knapsack_genetic_algorithm_low_dimensional_5():
    params = open_file("../dataset/low-dimensional/f6_l-d_kp_10_60")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve()
    optimum = int((open("../dataset/low-dimensional-optimum/f6_l-d_kp_10_60").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 52
    assert result[0].fitness.values[0] == optimum


def test_knapsack_genetic_algorithm_large_scale_1():
    params = open_file("../dataset/large_scale/knapPI_1_100_1000_1")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve(9000, 200)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_100_1000_1").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 9147
    assert result[0].fitness.values[0] <= 9000
    assert result[0].fitness.values[0] >= 7500
