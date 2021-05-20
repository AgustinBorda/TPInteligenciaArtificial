from search import GraphProblem, breadth_first_tree_search, romania_map


def romania_problem_test():
    problem = GraphProblem('Arad', 'Bucharest', romania_map)
    s = breadth_first_tree_search(problem)
    assert s.state == "Bucharest"
