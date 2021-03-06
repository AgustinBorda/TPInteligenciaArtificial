from search import Problem
import random


class KnapsackState:
    # A KnapsackState represents the state of the knapsack in
    # a determinate moment in the knapsack problem
    # The form of the items in the knapsack is
    # (weight, value)
    def __init__(self, capacity, weight, value, obj_in):
        self.capacity = capacity
        self.weight = weight
        self.value = value
        self.objects_in = obj_in

    # Item = (weight, value), position = int+
    def add_item(self, item, object_place):
        if not self.objects_in[object_place]:
            obj_in = self.objects_in.copy()
            obj_in[object_place] = True
            return KnapsackState(self.capacity, self.weight + item[0], self.value + item[1], obj_in)

    # Item = (weight, value), position = int+
    def remove_item(self, item, position):
        if self.objects_in[position]:
            obj_in = self.objects_in.copy()
            obj_in[position] = False
            return KnapsackState(self.capacity, self.weight - item[0], self.value - item[1], obj_in)

    def __eq__(self, other):
        return (
                self.capacity == other.capacity and
                self.weight == other.weight and
                self.value == other.value and
                self.objects_in == other.objects_in
        )


class KnapsackProblem(Problem):

    def __init__(self, capacity, objects):
        self.initial = KnapsackState(capacity, 0, 0, [False for i in range(len(objects))])
        self.knapsack_objects = objects

    # This returns a tuple (flag, item, position)
    # where the flag is positive if the action is add or negative otherwise
    def actions(self, state):
        available_items = []
        for i in range(len(self.knapsack_objects)):
            if (self.knapsack_objects[i][0] + state.weight <= state.capacity) and not state.objects_in[i]:
                available_items.append((1, self.knapsack_objects[i], i))
        for i in range(len(state.objects_in)):
            if state.objects_in[i]:
                available_items.append((-1, self.knapsack_objects[i], i))  # We can sack the objects of the knapsack
        return available_items

    def result(self, state, action):
        if action[0] > 0:
            return state.add_item(action[1], action[2])
        else:
            return state.remove_item(action[1], action[2])

    def value(self, state):
        return state.value

    def objects(self, state):
        obj = []
        for i in range(len(state.objects_in)):
            if state.objects_in[i]:
                obj.append(self.knapsack_objects[i])
        return obj

    # The random restart fills a empty knapsack with random objects until
    # a random weight is reached, or until it fails to put in an element for 10 times in a row
    def random_restart(self):
        new_state = KnapsackState(self.initial.capacity, 0, 0, [False] * len(self.knapsack_objects))

        k = random.randint(0, self.initial.capacity)
        knapsack_objects = list(enumerate(self.knapsack_objects))
        failed_attempts = 0
        while new_state.weight < k and failed_attempts < 10:
            pos, item = random.choice(knapsack_objects)
            if (item[0] + new_state.weight <= new_state.capacity) and not new_state.objects_in[pos]:
                new_state = new_state.add_item(item, pos)
                failed_attempts = 0
            else:
                failed_attempts += 1
        return new_state
