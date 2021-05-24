from search import Node
from collections import deque


def bidirectional_breadth_first_search(problem, inverse_problem):
    frontier = [(0, Node(problem.initial)), (1, Node(inverse_problem.initial)), ]
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
            frontier.extend(map(lambda node: (prefix, node), current_node.expand(problem)))
        else:
            if current_node in explored:
                return create_solution([node for node in explored if node.state == current_node.state][0], current_node)
            inverse_explored.add(current_node)
            frontier.extend(map(lambda node: (prefix, node), current_node.expand(inverse_problem)))

    return None


def create_solution(frontier_from_initial, frontier_from_final):
    current_parent = frontier_from_initial
    current_element = frontier_from_final.parent
    if not frontier_from_final.parent:  # If the frontier is a solution, does not have a parent,
        return frontier_from_initial    # so return the frontier from initial.
    while True:
        aux_node = current_element.parent
        current_element.parent = current_parent
        current_parent = current_element
        if not aux_node:
            return current_element
        current_element = aux_node
    return None
