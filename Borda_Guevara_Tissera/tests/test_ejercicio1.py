from Borda_Guevara_Tissera.resolutions.ejercicio1 import depth_first_tree_search_cycle_detection
from Borda_Guevara_Tissera.resolutions.ejercicio2 import bidirectional_breadth_first_search
from search import depth_first_tree_search, romania_map, GraphProblem, InstrumentedProblem
from pytest_timeout import *


@pytest.mark.timeout(15)
# This test fails because the dfs algorithm gets stuck in a cycle
def test_depth_first_tree_search_without_cycle_detection():
    res = depth_first_tree_search(GraphProblem("Arad", "Bucharest", romania_map))
    assert res.state == "Bucharest"


# With cycle detection, this problem can be solved.
def test_depth_first_search_with_cycle_detections():
    res = depth_first_tree_search_cycle_detection(GraphProblem("Arad", "Bucharest", romania_map))
    assert res.state == "Bucharest"

#@pytest.mark.timeout(30)
def test_1():
    res = bidirectional_breadth_first_search(GraphProblem("Bucharest", "Timisoara", romania_map),GraphProblem("Timisoara", "Bucharest", romania_map))
    assert res.state == "Timisoara"
    print(res.path())
