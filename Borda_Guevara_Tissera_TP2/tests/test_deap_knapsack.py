from Borda_Guevara_Tissera_TP2.resolutions.deap_knapsack import GeneticKnapsack
from Borda_Guevara_Tissera_TP2.resolutions.knapsack import KnapsackProblem
from Borda_Guevara_Tissera_TP2.tests.test_knapsack import open_file
from search import InstrumentedProblem, simulated_annealing, exp_schedule


def test_knapsack_genetic_algorithm_low_dimensional_1():
    params = open_file("../dataset/low-dimensional/f1_l-d_kp_10_269")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve()
    optimum = int((open("../dataset/low-dimensional-optimum/f1_l-d_kp_10_269").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 295
    assert result[0].fitness.values[0] == optimum


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
    assert result[0].fitness.values[0] == optimum


def test_knapsack_genetic_algorithm_low_dimensional_5():
    params = open_file("../dataset/low-dimensional/f6_l-d_kp_10_60")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve()
    optimum = int((open("../dataset/low-dimensional-optimum/f6_l-d_kp_10_60").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 52
    assert result[0].fitness.values[0] == optimum


def test_knapsack_simulated_annealing_low_dimensional_1():
    params = open_file("../dataset/low-dimensional/f1_l-d_kp_10_269")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem,  exp_schedule(2000, 0.00005, 200000))
    optimum = int((open("../dataset/low-dimensional-optimum/f1_l-d_kp_10_269").readline()))
    assert optimum == 295
    assert result.value <= optimum
    assert result.value >= 293


def test_knapsack_simulated_annealing_low_dimensional_2():
    params = open_file("../dataset/low-dimensional/f2_l-d_kp_20_878")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem,  exp_schedule(2000, 0.00005, 200000))
    optimum = int((open("../dataset/low-dimensional-optimum/f2_l-d_kp_20_878").readline()))
    assert optimum == 1024
    assert result.value == optimum



def test_knapsack_simulated_annealing_large_scale_1():
    params = open_file("../dataset/large_scale/knapPI_1_100_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem,  exp_schedule(1000, 0.0005, 4000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_100_1000_1").readline()))
    assert optimum == 9147
    assert result.value <= optimum
    assert result.value >= 8000


def test_knapsack_genetic_algorithm_large_scale_1():
    params = open_file("../dataset/large_scale/knapPI_1_100_1000_1")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve(300, 100, mu=400, l=1600)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_100_1000_1").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 9147
    assert result[0].fitness.values[0] <= 8500
    assert result[0].fitness.values[0] >= 7000


def test_knapsack_simulated_annealing_large_scale_2():
    params = open_file("../dataset/large_scale/knapPI_1_200_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem,  exp_schedule(1000, 0.0005, 4000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_200_1000_1").readline()))
    assert optimum == 11238
    assert result.value <= optimum
    assert result.value >= 9500


def test_knapsack_genetic_algorithm_large_scale_2():
    params = open_file("../dataset/large_scale/knapPI_1_200_1000_1")
    knapsack = GeneticKnapsack(params[0], params[1])
    result = knapsack.solve(500, 100, mu=400, l=1600)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_200_1000_1").readline()))
    result = sorted(result, key=lambda item: item.fitness, reverse=True)
    assert optimum == 11238
    assert result[0].fitness.values[0] <= optimum
    assert result[0].fitness.values[0] >= 6500
