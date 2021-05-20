from search import Node


# Implements depth first search algorithm with cycle detection.
# Ejercicio 1
def depth_first_tree_search_cycle_detection(problem):
    frontier = [Node(problem.initial)]  # Stack, with the initial state of the problem.
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node.state):
            return node
        if not cycle(node):
            frontier.extend(node.expand(problem))
    return None


# Returns true if exist a cycle between the current node and the problem start.
def cycle(node):
    n = node.parent
    while n:
        if node.state == n.state:
            return True
        n = n.parent
    return False
