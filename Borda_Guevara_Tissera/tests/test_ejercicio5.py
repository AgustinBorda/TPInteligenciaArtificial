from Borda_Guevara_Tissera.resolutions.ejercicio5 import SixteenPuzzle, iterative_deepening_astar_search
from search import InstrumentedProblem

# instance_one = (3, 8, 12, 0, 1, 14, 10, 9, 11, 13, 2, 15, 4, 5, 7, 6)
instance_two = (10, 3, 13, 5, 8, 2, 12, 11, 14, 7, 4, 15, 9, 6, 1, 0)
instance_three = (10, 7, 15, 4, 13, 5, 1, 6, 2, 9, 14, 3, 0, 11, 12, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

instance_one = (1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 12, 13, 14, 9, 15)


def test_iterative_deepening_astar_search_misplaced_tiles_cols_rows_1():
    sixteen_puzzle = InstrumentedProblem(SixteenPuzzle(initial=instance_one, goal=goal))
    res = iterative_deepening_astar_search(sixteen_puzzle, SixteenPuzzle(sixteen_puzzle).misplaced_cols_rows)
    assert res.state == goal


def test_iterative_deepening_astar_search_manhattan_1():
    sixteen_puzzle = InstrumentedProblem(SixteenPuzzle(initial=instance_one, goal=goal))
    res = iterative_deepening_astar_search(sixteen_puzzle, SixteenPuzzle(sixteen_puzzle).manhattan_distance)
    assert res.state == goal


def test_iterative_deepening_astar_search_gaschnig_1():
    sixteen_puzzle = InstrumentedProblem(SixteenPuzzle(initial=instance_one, goal=goal))
    res = iterative_deepening_astar_search(sixteen_puzzle, SixteenPuzzle(sixteen_puzzle).gaschnig_index)
    assert res.state == goal

