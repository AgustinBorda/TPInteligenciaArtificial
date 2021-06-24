from Borda_Guevara_Tissera_TP2.resolutions.knapsack import KnapsackProblem, KnapsackState
from search import hill_climbing, InstrumentedProblem


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


def test_knapsack_actions():
    problem = KnapsackProblem(20, [(25, 30), (5, 9), (20, 200)])
    actions = problem.actions(problem.initial)
    assert actions.__contains__(((5, 9), 1))
    assert actions.__contains__(((20, 200), 2))
    assert not actions.__contains__(((25, 30), 0))


def test_knapsack_value():
    problem = KnapsackProblem(20, [(25, 30), (5, 9), (20, 200)])
    state = KnapsackState(20, 20, 20, [False])
    assert problem.value(state) == state.value


def test_knapsack_hill_climbing_1():
    problem = KnapsackProblem(100, [(115, 20), (50, 1), (1, 1000), (2, 500), (1, 1001)])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing(ins_problem)
    assert result.value == 2502
    assert result.weight == 54
    assert result.capacity == 100
    obj = ins_problem.objects(result)
    assert obj.__contains__((50, 1))
    assert obj.__contains__((1, 1000))
    assert obj.__contains__((2, 500))
    assert obj.__contains__((1, 1001))
    assert not obj.__contains__((115, 20))


def open_file(file):
    file = open(file)
    line = file.readline()
    index = 0
    data = []
    capacity = 0
    cant = 0

    while line != '':
        line = file.readline()
        element_list = line.split()
        if index == 0:
            cant = int(element_list[0])
            capacity = int(element_list[1])
        if (index > 0) and (index <= cant):
            data.append((int(element_list[1]), int(element_list[0])))
        index += 1

    return capacity, data


# Optimum = 9147
# Value = 4427
def test_knapsack_hill_climbing_2():
    params = open_file("../dataset/large_scale/knapPI_1_100_1000_1")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing(ins_problem)
    assert result.value == 9147


def test_knapsack_hill_climbing_3():
    params = open_file("../dataset/low-dimensional/f8_l-d_kp_23_10000")
    problem = KnapsackProblem(params[0], params[1])
    ins_problem = InstrumentedProblem(problem)
    result = hill_climbing(ins_problem)
    assert result.value == 11238
