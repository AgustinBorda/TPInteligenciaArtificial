from search import Node
from Borda_Guevara_Tissera.resolutions.ejercicio4 import EightPuzzleExtended
from utils import *
import sys


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


def cost_limited_astar_search(problem, limit, f):
    def recursive_cost_limited_astar_search(node, problem, limit, f):
        if problem.goal_test(node.state):
            return node
        elif f(node) > limit:
            return 'cutoff'
        else:
            cutoff_occurred = False
            for child in node.expand(problem):
                result = recursive_cost_limited_astar_search(child, problem, limit - 1, f)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None
    f = memoize(f, 'f')
    return recursive_cost_limited_astar_search(Node(problem.initial), problem, limit, f)


def iterative_deepening_astar_search(problem, h=None):
    h = memoize(h or problem.h, 'h')
    for cost_limit in range(sys.maxsize):
        result = cost_limited_astar_search(problem, cost_limit, lambda n: n.path_cost + h(n))
        if result != 'cutoff':
            return result
