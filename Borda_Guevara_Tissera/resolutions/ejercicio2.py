from search import Node
from collections import deque


def bidirectional_breadth_first_search(problem, inverse_problem):
    frontier = [(1, Node(inverse_problem.initial)), (0, Node(problem.initial))]
    explored = set()
    inverse_explored = set()
    while frontier:
        current = frontier.pop(0)
        prefix = current[0]
        current_node = current[1]
        if prefix == 0:
            if current_node in inverse_explored:
                return create_solution(current_node, [node for node in inverse_explored
                                                      if node.state == current_node.state][0])
            explored.add(current_node)
            frontier.extend(map(lambda node: (prefix, node), current_node.expand(problem)))  # Welcome to Python, enjoy
        else:
            if current_node in explored:
                return create_solution([node for node in explored if node.state == current_node.state][0], current_node)
            inverse_explored.add(current_node)
            frontier.extend(map(lambda node: (prefix, node), current_node.expand(inverse_problem)))
    return None
# TODO: Hacerlo mas legible o Ponzio nos mata

# TODO: pensar esto
def create_solution(frontier_initial, frontier_goal):
    current_parent = frontier_initial
    current_element = frontier_goal.parent
    while current_:
        aux_element = current_element.parent
        current_element.parent = current_parent
        current_parent = current_element
        current_element = aux_element
    return current_element
