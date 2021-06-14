from search import Problem


class KnapsackState:
    def __init__(self, capacity, weight, value):
        self.capacity = capacity
        self.weight = weight
        self.value = value

    def add_item(self, item):
        return KnapsackState(self.capacity, self.weight + item[0], self.value + item[1])

# TODO: eficiencia de las listas, hacer que solo se pueda meter un elemento por vez (listas en el state)

class KnapsackProblem(Problem):

    def __init__(self, capacity, objects):
        self.initial = KnapsackState(capacity, 0, 0)
        self.knapsack_objects = objects

    def actions(self, state):
        available_items = []
        for t in self.knapsack_objects:
            if state.weight + t[0] <= state.capacity:  # t[0] == The weight of item t
                available_items.append(t)
        return available_items

    def result(self, state, action):
        return state.add_item(action)

    def value(self, state):
        return state.value
