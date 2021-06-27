import random
from matplotlib import pyplot as plt
from utils import probability
from pylab import np
from search import Node, sys

def exp_schedule(k, lam, limit):
    """One possible schedule function for simulated annealing"""
    return lambda t: (k * np.exp(-lam * t) if t < limit else 0)

def simulated_annealing_plot(problem, values_for_schedule):
    """[Figure 4.5] CAUTION: This differs from the pseudocode as it
    returns a state instead of a Node."""
    schedule = exp_schedule(values_for_schedule[0], values_for_schedule[1], values_for_schedule[2])
    x = list()
    y = list()
    current = Node(problem.initial)
    for t in range(sys.maxsize):
        T = schedule(t)
        if T == 0:
            plt.scatter(x, y)
            plt.show()
            return current.state
        neighbors = current.expand(problem)
        if not neighbors:
            plt.plot(x, y, '.b-')
            plt.show()
            return current.state
        next_choice = random.choice(neighbors)
        delta_e = problem.value(next_choice.state) - problem.value(current.state)
        y.append(problem.value(current.state))
        x.append(t)
        if delta_e > 0 or probability(np.exp(delta_e / T)):
            current = next_choice
