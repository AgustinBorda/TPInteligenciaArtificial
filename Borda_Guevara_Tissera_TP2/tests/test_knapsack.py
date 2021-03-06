from Borda_Guevara_Tissera_TP2.resolutions.knapsack import KnapsackProblem, KnapsackState
from Borda_Guevara_Tissera_TP2.resolutions.simulated_annealing_plot import simulated_annealing_plot
from search import hill_climbing, InstrumentedProblem, simulated_annealing, hill_climbing_random_restart


def test_knapsack_problem_initial():
    problem = KnapsackProblem(20, [(0, 0), (0, 0)])
    assert problem.initial.capacity == 20
    assert problem.value(problem.initial) == 0
    assert problem.initial.weight == 0


def test_knapsack_add():
    knapsack = KnapsackState(20, 0, 0, [False])
    added_knapsack = knapsack.add_item((10, 15), 0)
    assert added_knapsack.capacity == knapsack.capacity
    assert added_knapsack.value == 15
    assert added_knapsack.weight == 10
    assert knapsack.value == 0
    assert knapsack.weight == 0
    assert added_knapsack.objects_in[0]
    assert not knapsack.objects_in[0]


def test_knapsack_remove():
    knapsack = KnapsackState(20, 10, 15, [True])
    removed_knapsack = knapsack.remove_item((10, 15), 0)
    assert removed_knapsack.capacity == knapsack.capacity
    assert removed_knapsack.value == 0
    assert removed_knapsack.weight == 0
    assert knapsack.value == 15
    assert knapsack.weight == 10
    assert not removed_knapsack.objects_in[0]
    assert knapsack.objects_in[0]


def test_knapsack_actions():
    problem = KnapsackProblem(20, [(25, 30), (5, 9), (20, 200)])
    actions = problem.actions(problem.initial)
    assert actions.__contains__((1, (5, 9), 1))
    assert actions.__contains__((1, (20, 200), 2))
    assert not actions.__contains__((1, (25, 30), 0))


def test_knapsack_value():
    problem = KnapsackProblem(20, [(25, 30), (5, 9), (20, 200)])
    state = KnapsackState(20, 20, 20, [False])
    assert problem.value(state) == state.value


def open_file(file):
    file = open(file)
    data = []
    line = file.readline()
    element_list = line.split()
    cant = int(element_list[0])
    capacity = int(element_list[1])

    for i in range(0, cant):
        line = file.readline()
        element_list = line.split()
        data.append((int(element_list[1]), int(element_list[0])))

    return capacity, data


# Hill Climbing Tests.
def test_knapsack_hill_climbing_large_scale_1():
    params = open_file("../dataset/large_scale/knapPI_1_200_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_200_1000_1").readline()))
    print(result.value)
    assert optimum == 11238
    assert result.value <= 7000
    assert result.value >= 4500


def test_knapsack_hill_climbing_large_scale_2():
    params = open_file("../dataset/large_scale/knapPI_1_100_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_100_1000_1").readline()))
    assert optimum == 9147
    assert result.value <= 5500
    assert result.value >= 2500


def test_knapsack_hill_climbing_large_scale_3():
    params = open_file("../dataset/large_scale/knapPI_1_500_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_500_1000_1").readline()))
    assert optimum == 28857
    assert result.value <= 10000
    assert result.value >= 9800


def test_knapsack_hill_climbing_large_scale_4():
    params = open_file("../dataset/large_scale/knapPI_1_1000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_1000_1000_1").readline()))
    assert optimum == 54503
    assert result.value <= 16000
    assert result.value >= 13000


def test_knapsack_hill_climbing_large_scale_5():
    params = open_file("../dataset/large_scale/knapPI_1_2000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_2000_1000_1").readline()))
    assert optimum == 110625
    assert result.value <= 29000
    assert result.value >= 22000


def test_knapsack_hill_climbing_large_scale_6():
    params = open_file("../dataset/large_scale/knapPI_1_5000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_5000_1000_1").readline()))
    assert optimum == 276457
    assert result.value <= 100000
    assert result.value >= 48000


# Simulated Annealing tests.
def test_knapsack_simulated_annealing_large_scale_1():
    params = open_file("../dataset/large_scale/knapPI_1_200_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_200_1000_1").readline()))
    assert optimum == 11238
    assert result.value <= 4000
    assert result.value >= 2000


def test_knapsack_simulated_annealing_large_scale_2():
    params = open_file("../dataset/large_scale/knapPI_1_100_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_100_1000_1").readline()))
    assert optimum == 9147
    assert result.value <= 4500
    assert result.value >= 400


def test_knapsack_simulated_annealing_large_scale_3():
    params = open_file("../dataset/large_scale/knapPI_1_500_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_500_1000_1").readline()))
    assert optimum == 28857
    assert result.value <= 8000
    assert result.value >= 1400


def test_knapsack_simulated_annealing_large_scale_4():
    params = open_file("../dataset/large_scale/knapPI_1_1000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_1000_1000_1").readline()))
    assert optimum == 54503
    assert result.value <= 13000
    assert result.value >= 5300


def test_knapsack_simulated_annealing_large_scale_5():
    params = open_file("../dataset/large_scale/knapPI_1_2000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_2000_1000_1").readline()))
    assert optimum == 110625
    assert result.value <= 14200
    assert result.value >= 8500


def test_knapsack_simulated_annealing_large_scale_6():
    params = open_file("../dataset/large_scale/knapPI_1_5000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing(ins_problem)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_5000_1000_1").readline()))
    assert optimum == 276457
    assert result.value <= 40000
    assert result.value >= 25000


# Hill Climbing Random reset tests
def test_knapsack_hill_climbing_rr_large_scale_1():
    params = open_file("../dataset/large_scale/knapPI_1_200_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing_random_restart(ins_problem, 100)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_200_1000_1").readline()))
    assert optimum == 11238
    assert result.value <= 7000
    assert result.value >= 4500


def test_knapsack_hill_climbing_rr_large_scale_2():
    params = open_file("../dataset/large_scale/knapPI_1_100_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing_random_restart(ins_problem, 300)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_100_1000_1").readline()))
    assert optimum == 9147
    assert result.value <= 8500
    assert result.value >= 6100


def test_knapsack_hill_climbing_rr_large_scale_3():
    params = open_file("../dataset/large_scale/knapPI_1_500_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing_random_restart(ins_problem, 100)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_500_1000_1").readline()))
    assert optimum == 28857
    assert result.value <= 13000
    assert result.value >= 9800


def test_knapsack_hill_climbing_rr_large_scale_4():
    params = open_file("../dataset/large_scale/knapPI_1_1000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing_random_restart(ins_problem, 100)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_1000_1000_1").readline()))
    assert optimum == 54503
    assert result.value <= 20000
    assert result.value >= 17000


def test_knapsack_hill_climbing_rr_large_scale_5():
    params = open_file("../dataset/large_scale/knapPI_1_2000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing_random_restart(ins_problem, 100)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_2000_1000_1").readline()))
    assert optimum == 110625
    assert result.value <= 30000
    assert result.value >= 27000


def test_knapsack_hill_climbing_rr_large_scale_6():
    params = open_file("../dataset/large_scale/knapPI_1_5000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing_random_restart(ins_problem, 100)
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_5000_1000_1").readline()))
    assert optimum == 276457
    assert result.value <= 100000
    assert result.value >= 48000


# Simulated Annealing tests.
def test_knapsack_simulated_annealing_plot_large_scale_1():
    params = open_file("../dataset/large_scale/knapPI_1_200_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (1000, 0.0005, 4000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_200_1000_1").readline()))
    assert optimum == 11238
    assert result.value <= 11238
    assert result.value >= 10000


def test_knapsack_simulated_annealing_plot_large_scale_2():
    params = open_file("../dataset/large_scale/knapPI_1_100_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (1000, 0.0005, 5000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_100_1000_1").readline()))
    assert optimum == 9147
    assert result.value <= optimum
    assert result.value >= 8400


def test_knapsack_simulated_annealing_plot_large_scale_3():
    params = open_file("../dataset/large_scale/knapPI_1_500_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (1000, 0.0005, 10000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_500_1000_1").readline()))
    assert optimum == 28857
    assert result.value <= 28857
    assert result.value >= 1400


def test_knapsack_simulated_annealing_plot_large_scale_4():
    params = open_file("../dataset/large_scale/knapPI_1_1000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (1000, 0.0005, 10000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_1000_1000_1").readline()))
    assert optimum == 54503
    assert result.value <= 54503
    assert result.value >= 5300


# Time to finish 50 sec
def test_knapsack_simulated_annealing_plot_large_scale_5_1():
    params = open_file("../dataset/large_scale/knapPI_1_2000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (1000, 0.0005, 10000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_2000_1000_1").readline()))
    assert optimum == 110625
    assert result.value <= 100000
    assert result.value >= 89000


# Time to finish 27 sec
def test_knapsack_simulated_annealing_plot_large_scale_5_2():
    params = open_file("../dataset/large_scale/knapPI_1_2000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (1000, 0.0005, 6000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_2000_1000_1").readline()))
    assert optimum == 110625
    assert result.value <= 110625
    assert result.value >= 8500


# Time to finish 19 sec
def test_knapsack_simulated_annealing_plot_large_scale_5_3():
    params = open_file("../dataset/large_scale/knapPI_1_2000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (500, 0.0005, 6000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_2000_1000_1").readline()))
    assert optimum == 110625
    assert result.value <= 110625
    assert result.value >= 8500


# Time to finish 13 sec
def test_knapsack_simulated_annealing_plot_large_scale_5_4():
    params = open_file("../dataset/large_scale/knapPI_1_2000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (500, 0.0005, 3000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_2000_1000_1").readline()))
    assert optimum == 110625
    assert result.value <= 90000
    assert result.value >= 85000


# Time to finish 4 min
def test_knapsack_simulated_annealing_plot_large_scale_6_1():
    params = open_file("../dataset/large_scale/knapPI_1_5000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (1000, 0.0005, 10000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_5000_1000_1").readline()))
    assert optimum == 276457
    assert result.value <= 276457
    assert result.value >= 25000


# Time to finish 6 min
def test_knapsack_simulated_annealing_plot_large_scale_6_2():
    params = open_file("../dataset/large_scale/knapPI_1_5000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (2000, 0.0005, 10000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_5000_1000_1").readline()))
    assert optimum == 276457
    assert result.value <= 276457
    assert result.value >= 25000


# Time to finish 3 min
def test_knapsack_simulated_annealing_plot_large_scale_6_3():
    params = open_file("../dataset/large_scale/knapPI_1_5000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (500, 0.0005, 3000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_5000_1000_1").readline()))
    assert optimum == 276457
    assert result.value <= 276457
    assert result.value >= 25000


# Time to finish 3 min
def test_knapsack_simulated_annealing_plot_large_scale_6_4():
    params = open_file("../dataset/large_scale/knapPI_1_5000_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = simulated_annealing_plot(ins_problem, (800, 0.0005, 4000))
    optimum = int((open("../dataset/large_scale-optimum/knapPI_1_5000_1000_1").readline()))
    assert optimum == 276457
    assert result.value <= 230000
    assert result.value >= 190000
