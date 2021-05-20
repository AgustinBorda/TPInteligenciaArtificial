#@pytest.mark.timeout(30)
from Borda_Guevara_Tissera.resolutions.ejercicio2 import bidirectional_breadth_first_search
from search import GraphProblem, romania_map


def test_oradea_oradea():
    res = bidirectional_breadth_first_search(GraphProblem("Oradea", "Oradea", romania_map),
                                             GraphProblem("Oradea", "Oradea", romania_map))
    assert res.state == "Oradea"


def test_eforie_oradea():
    res = bidirectional_breadth_first_search(GraphProblem("Eforie", "Oradea", romania_map),
                                             GraphProblem("Oradea", "Eforie", romania_map))
    assert res.state == "Oradea"


def test_oradea_eforie():
    res = bidirectional_breadth_first_search(GraphProblem("Oradea", "Eforie", romania_map),
                                             GraphProblem("Eforie", "Oradea", romania_map))
    assert res.state == "Eforie"


def test_bucharest_arad():
    res = bidirectional_breadth_first_search(GraphProblem("Bucharest", "Arad", romania_map),
                                             GraphProblem("Arad", "Bucharest", romania_map))
    assert res.state == "Arad"


def test_arad_bucharest():
    res = bidirectional_breadth_first_search(GraphProblem("Arad", "Bucharest", romania_map),
                                             GraphProblem("Bucharest", "Arad", romania_map))
    assert res.state == "Bucharest"

# TODO: Comparar con breadth first tree (breadth_first.explored >= bidirectional1.explored+bidirectional2.explored)
