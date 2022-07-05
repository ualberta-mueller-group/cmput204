# Implements an edge in the adjacency list of a graph as a pair (otherEnd, length)
# This is a Python tuple with two elements.
# See https://docs.python.org/3.5/tutorial/datastructures.html#tuples-and-sequences

def otherEnd(edge):
    return edge[0]

def length(edge):
    return edge[1]

def makeEdge(otherEnd, length):
    return (otherEnd, length)
