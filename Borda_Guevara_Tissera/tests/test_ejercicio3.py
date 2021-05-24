from search import EightPuzzle, breadth_first_graph_search, depth_first_graph_search
import random
from Borda_Guevara_Tissera.resolutions.ejercicio2 import bidirectional_breadth_first_search

instance_one = (5, 6, 8, 1, 3, 4, 7, 0, 2)
instance_two = (7, 8, 3, 1, 5, 4, 0, 2, 6)
instance_three = (7, 4, 8, 1, 2, 6, 3, 5, 0)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

"""
instance_one
    bidirectional_breadth_first_search: 
        path_len: 22
        explored:nodes: 1495
    breadth_first_graph_search: 
        path_len: 24
        explored:nodes: 181439
    depth_first_graph_search
        path_len: 62784 
        explored_nodes: 79767
"""
def test_bidirectional_breadth_first_search_instance_one():
    eight_puzzle = EightPuzzle(initial=instance_one, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=instance_one)
    res = bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed)
    print(res.path())


def test_bidirectional_breadth_first_search_instance_two():
    eight_puzzle = EightPuzzle(initial=instance_two, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=instance_two)
    res = bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed)
    print(res.path())


def test_bidirectional_breadth_first_search_instance_three():
    eight_puzzle = EightPuzzle(initial=instance_three, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=instance_three)
    res = bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed)
    print(res.path())


def test_bidirectional_breadth_first_search_vs_breadth_first_graph_search():
    initial_state = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    eight_puzzle = EightPuzzle(initial=instance_one, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=instance_one)
    res_0 = bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed, explored_nodes=True)
    res_1 = breadth_first_graph_search(eight_puzzle, explored_nodes=True)
    assert res_0[1] <= res_1[1]


def test_bidirectional_breadth_first_search_vs_depth_first_graph_search():
    initial_state = (1, 2, 3, 4, 5, 6, 7, 0, 8)
    eight_puzzle = EightPuzzle(initial=initial_state, goal=goal)
    eight_puzzle_reversed = EightPuzzle(initial=goal, goal=initial_state)
    res_0 = bidirectional_breadth_first_search(eight_puzzle, eight_puzzle_reversed, explored_nodes=True)
    res_1 = breadth_first_graph_search(eight_puzzle, explored_nodes=True)
    assert res_0[1] <= res_1[1]
