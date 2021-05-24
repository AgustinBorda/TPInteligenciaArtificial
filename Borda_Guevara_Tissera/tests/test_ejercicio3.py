from search import EightPuzzle, breadth_first_graph_search, depth_first_graph_search, InstrumentedProblem
from pytest_timeout import *
from Borda_Guevara_Tissera.resolutions.ejercicio2 import bidirectional_breadth_first_search, \
    instrumented_bidirectional_breadth_first_search

instance_one = (5, 6, 8, 1, 3, 4, 7, 0, 2)
instance_two = (6, 2, 8, 1, 3, 4, 7, 0, 5)
instance_three = (2, 8, 6, 1, 0, 3, 4, 7, 5)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

"""
instance_one
    bidirectional_breadth_first_search: 
        path_len: 22
        explored:nodes: 1495
    breadth_first_graph_search: 
        path_len: 24
        explored:nodes: 181439
    depth_first_graph_search
        path_len: 62784 
        explored_nodes: 79767
"""


@pytest.mark.timeout(30)
def test_bidirectional_breadth_first_search_instance_one():
    eight_puzzle = EightPuzzle(initial=instance_one, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=instance_one)
    res = bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed)
    print(res.path())
    assert res.state == goal


@pytest.mark.timeout(30)
def test_bidirectional_breadth_first_search_instance_two():
    eight_puzzle = EightPuzzle(initial=instance_two, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=instance_two)
    res = bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed)
    print(res.path())
    assert res.state == goal


@pytest.mark.timeout(30)
def test_bidirectional_breadth_first_search_instance_three():
    eight_puzzle = EightPuzzle(initial=instance_three, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=instance_three)
    res = bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed)
    print(res.path())
    assert res.state == goal


@pytest.mark.timeout(30)
def test_bidirectional_breadth_first_search_vs_breadth_first_graph_search():
    eight_puzzle = EightPuzzle(initial=instance_two, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=instance_two)
    ins_problem = InstrumentedProblem(eight_puzzle)
    res = instrumented_bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed, True)
    breadth_first_graph_search(ins_problem)
    assert (res[1]) <= ins_problem.explored


# Depth-first doesn't finish
@pytest.mark.timeout(30)
def test_bidirectional_breadth_first_search_vs_depth_first_graph_search():
    eight_puzzle = EightPuzzle(initial=instance_three, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=instance_three)
    ins_problem = InstrumentedProblem(eight_puzzle)
    res = instrumented_bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed, True)
    depth_first_graph_search(ins_problem)
    assert (res[1]) <= ins_problem.explored

