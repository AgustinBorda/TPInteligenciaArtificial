from abc import ABC

from search import EightPuzzle


class EightPuzzleExtended(EightPuzzle):

    def value(self, state):
        pass

    def misplaced_cols_rows(self, node):
        state = node.state
        goal = self.goal
        misplaced_cols = 0
        for i in range(3):
            for j in range(i, len(goal), 3):
                if state[j] != goal[j]:
                    misplaced_cols += 1
        misplaced_rows = sum(s != g for (s, g) in zip(node.state, self.goal))
        return misplaced_cols + misplaced_rows

    def manhattan_distance(self, node):
        return sum([abs((self.goal.index(x) - node.state.index(x)) // 3) + abs((self.goal.index(x) - node.state.index(x)) % 3) for x in node.state])

    def gaschnig_index(self, node):
        state = node.state
        goal = self.goal
        moves = 0
        while state != goal:
            for i in range(len(goal)):
                if state[i] != goal[i] and state[i] != 0:
                    blank_index = state.index(0)
                    aux = state[i]
                    state[i] = state[blank_index]
                    state[blank_index] = aux
                    moves += 1
        return moves
