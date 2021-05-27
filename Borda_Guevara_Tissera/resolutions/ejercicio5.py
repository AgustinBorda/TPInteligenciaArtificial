from search import Node
from Borda_Guevara_Tissera.resolutions.ejercicio4 import EightPuzzleExtended
from utils import PriorityQueue, memoize


class SixteenPuzzle(EightPuzzleExtended):
    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0)):
        super().__init__(initial, goal)

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only four possible actions
        in any given state of the environment """

        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square % 4 == 0:
            possible_actions.remove('LEFT')
        if index_blank_square < 4:
            possible_actions.remove('UP')
        if index_blank_square % 4 == 3:
            possible_actions.remove('RIGHT')
        if index_blank_square > 11:
            possible_actions.remove('DOWN')

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -4, 'DOWN': 4, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)


# heuristic limited best first search,
# only expands the nodes with f <= limit and
# the first with f > limit.
# with the right heuristic it becomes a cost limited astar search
def cost_limited_astar_search(problem, limit, f):
    frontier = PriorityQueue("min", lambda node: f(node))
    frontier.append(Node(problem.initial))
    res = limit  # Limit as a placeholder value
    cutoff = False
    explored = set()
    while frontier:
        n = frontier.pop()
        if problem.goal_test(n.state):
            return 1, n
        if not cutoff and n not in explored:
            frontier.extend(n.expand(problem))
            explored.add(n)
        if f(n) > limit:
            cutoff = True
            res = f(n)
    return 0, res


# iterative deepening a*, executes a cost limited a*
# with a growing limit (begins in 0)
def iterative_deepening_astar_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    prefix = 0
    cost_limit = 0
    result = None
    while not prefix:
        result = cost_limited_astar_search(problem, cost_limit, lambda n: n.path_cost + h(n))
        prefix = result[0]
        if not prefix:
            cost_limit = result[1]
    return result[1]
