from Borda_Guevara_Tissera.resolutions.ejercicio2 import instrumented_bidirectional_breadth_first_search
from Borda_Guevara_Tissera.resolutions.ejercicio4 import EightPuzzleExtended
from Borda_Guevara_Tissera.resolutions.ejercicio5 import iterative_deepening_astar_search
from search import EightPuzzle, breadth_first_graph_search, depth_first_graph_search, InstrumentedProblem, astar_search
from pytest_timeout import *

instance_one = (5, 6, 8, 1, 3, 4, 7, 0, 2)
instance_two = (6, 2, 8, 1, 3, 4, 7, 0, 5)
instance_three = (2, 8, 6, 1, 0, 3, 4, 7, 5)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)


# Execution time: 3.48s
# 3975 nodes explored
def test_astar_misplaced_tiles_1():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_one, goal=goal))
    res = astar_search(eight_problem, eight_problem.h)
    assert res.state == goal


# Execution time: 0.13s
# 618 nodes explored
def test_astar_misplaced_tiles_2():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_two, goal=goal))
    res = astar_search(eight_problem, eight_problem.h)
    assert res.state == goal


# Execution time: 0.06s
# 227 nodes explored
def test_astar_misplaced_tiles_3():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_three, goal=goal))
    res = astar_search(eight_problem, eight_problem.h)
    assert res.state == goal


# Mean of execution misplaced tiles: 1.22s


# Execution time: 0.43s
# 1272 nodes explored
def test_astar_misplaced_tiles_cols_rows_1():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_one, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).misplaced_cols_rows)
    assert res.state == goal


# Execution time: 0.07s
# 296 nodes explored
def test_astar_misplaced_tiles_cols_rows_2():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_two, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).misplaced_cols_rows)
    assert res.state == goal


# Execution time: 0.05s
# 141 nodes explored
def test_astar_misplaced_tiles_cols_rows_3():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_three, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).misplaced_cols_rows)
    assert res.state == goal


# Mean of execution misplaced cols and rows: 0.18s


# Execution time: 0.10s
# 392 nodes explored
def test_astar_manhattan_1():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_one, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).manhattan_distance)
    assert res.state == goal


# Execution time: 0.14s
# 514 nodes explored
def test_astar_manhattan_2():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_two, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).manhattan_distance)
    assert res.state == goal


# Execution time: 0.05s
# 223 nodes explored
def test_astar_manhattan_3():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_three, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).manhattan_distance)
    assert res.state == goal


# Mean of execution manhattan: 0.09s


# Execution time: 1.17s
# 2117 nodes explored
def test_astar_gaschnig_1():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_one, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).gaschnig_index)
    assert res.state == goal


# Execution time: 0.09s
# 367 nodes explored
def test_astar_gaschnig_2():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_two, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).gaschnig_index)
    assert res.state == goal


# Execution time: 0.04s
# 114 nodes explored
def test_astar_gaschnig_3():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_three, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).gaschnig_index)
    assert res.state == goal


# Mean gaschnig: 0.43s

# breadth first search doesn't finish
# before time out
@pytest.mark.timeout(30)
def test_astar_gaschnig_vs_breadth_first():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_one, goal=goal))
    eight_problem1 = InstrumentedProblem(EightPuzzle(initial=instance_one, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).gaschnig_index)
    res1 = breadth_first_graph_search(eight_problem1)
    assert res.state == goal
    assert res1.state == goal
    assert eight_problem.explored < eight_problem1.explored


# depth first search doesn't finish
# before time out
@pytest.mark.timeout(30)
def test_astar_gaschnig_vs_depth_first():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_one, goal=goal))
    eight_problem1 = InstrumentedProblem(EightPuzzle(initial=instance_one, goal=goal))
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).gaschnig_index)
    res1 = depth_first_graph_search(eight_problem1)
    assert res.state == goal
    assert res1.state == goal
    assert eight_problem.explored < eight_problem1.explored


# a* explore more nodes
# than bidirectional search
@pytest.mark.timeout(30)
def test_astar_gaschnig_vs_bidirectional_breadth_first():
    eight_problem = InstrumentedProblem(EightPuzzle(initial=instance_one, goal=goal))
    eight_problem1 = EightPuzzle(initial=instance_one, goal=goal)
    inversed_eight_problem = EightPuzzle(initial=goal, goal=instance_one)
    res = astar_search(eight_problem, EightPuzzleExtended(eight_problem).gaschnig_index)
    res1 = instrumented_bidirectional_breadth_first_search(eight_problem1, inversed_eight_problem, True)
    assert res.state == goal
    n = res1[0]
    assert n.state == goal
    assert eight_problem.explored > res1[1]
