# coding=utf-8

"""
Algorithm named Breadth-First Search, is an algorithm for traversing or searching tree or graph data structures.
It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a 'search key'),
and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.

It uses the opposite strategy as depth-first search,
which instead explores the node branch as far as possible before being forced to backtrack and expand other nodes.

From [Wikipedia](https://en.wikipedia.org/wiki/Breadth-first_search)
"""


def breadth_first_search(maze: list, start: int, end: int):
    return [start, end]  # TODO::
