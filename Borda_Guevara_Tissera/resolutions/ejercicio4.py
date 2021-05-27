from search import EightPuzzle


class EightPuzzleExtended(EightPuzzle):

    def value(self, state):
        pass

    # Quantity of misplaced elements in rows +
    # misplaced element in columns
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

    # Manhattan's distance:
    # the sum of the list of
    # the sum of the sub of
    # each goal index minus the actual index divided 3
    # and the rest of that div
    def manhattan_distance(self, node):
        return sum([abs((self.goal.index(x) - node.state.index(x)) // 3) +
                    abs((self.goal.index(x) - node.state.index(x)) % 3) for x in node.state])

    # Gaschnig's heuristic
    # Quantity of direct exchanges between the blank tile and
    # other elements.
    def gaschnig_index(self, node):
        state = [i for i in node.state]
        goal = [i for i in self.goal]
        moves = 0
        blank_tile = -1
        element_tile = -1
        while state != goal:
            for i in range(len(state)):
                if state[i] == 0:
                    blank_tile = i
                    break
            for i in range(len(state)):
                if state[i]-1 == blank_tile:
                    element_tile = i
            if blank_tile == element_tile or element_tile < 0 or blank_tile < 0:
                for i in range(len(state)):
                    if state[i] != goal[i] and state[i] != 0:
                        element_tile = i
            aux = state[element_tile]
            state[element_tile] = state[blank_tile]
            state[blank_tile] = aux
            moves += 1
        return moves
