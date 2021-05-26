from Borda_Guevara_Tissera.resolutions.ejercicio5 import SixteenPuzzle, iterative_deepening_astar_search
from search import InstrumentedProblem, astar_search

instance_one = (1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 12, 13, 14, 9, 15)
instance_two = (1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 0, 12, 13, 14, 9, 15)
instance_three = (1, 2, 3, 4, 5, 6, 7, 8, 0, 10, 11, 12, 13, 14, 9, 15)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)

# We use Gaschnig heuristic.


def test_iterative_deepening_astar_1():
    problem = InstrumentedProblem(SixteenPuzzle(initial=instance_one, goal=goal))
    result = iterative_deepening_astar_search(problem, problem.gaschnig_index)
    assert result.state == goal


def test_iterative_deepening_astar_2():
    problem = InstrumentedProblem(SixteenPuzzle(initial=instance_two, goal=goal))
    result = iterative_deepening_astar_search(problem, problem.gaschnig_index)
    assert result.state == goal


def test_iterative_deepening_astar_3():
    problem = InstrumentedProblem(SixteenPuzzle(initial=instance_three, goal=goal))
    result = iterative_deepening_astar_search(problem, problem.gaschnig_index)
    assert result.state == goal


def test_astar_1():
    problem = InstrumentedProblem(SixteenPuzzle(initial=instance_one, goal=goal))
    result = astar_search(problem, problem.gaschnig_index)
    assert result.state == goal


def test_astar_2():
    problem = InstrumentedProblem(SixteenPuzzle(initial=instance_two, goal=goal))
    result = astar_search(problem, problem.gaschnig_index)
    assert result.state == goal


def test_astar_3():
    problem = InstrumentedProblem(SixteenPuzzle(initial=instance_three, goal=goal))
    result = astar_search(problem, problem.gaschnig_index)
    assert result.state == goal

""" 
    Existen casos resolvibles por iterative deepening a* que a* no puede resolver
    como por ejemplo, si expandimos un nodo cuyos hijos nos llenarian la ram.
    Ejemplo en "explicacion_astar_vs_idastar.txt"
    Realizar estos tests seria muy costoso en tiempo y recursos, ya que precisamos agotar el heap
    de Python.
"""
