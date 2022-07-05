# Shortest distance in DAG with a DP algorithm
# sets each distance only once, finds shortest path right away

from edgeWithLength import otherEnd, length
from reverse2 import reverse
from sys import maxsize
from topologicalOrdering2 import dfsSingleSource

# loop over all in-edges of v (which are out-edges in reverse dag)
def findShortestPath(rDag, v, distance):
    shortest = maxsize
    for edge in rDag[v]:
        d = distance[otherEnd(edge)] + length(edge)
        if d < shortest:
            shortest = d
    return shortest

def dagShortestDistance(dag, start):
    stack = dfsSingleSource(dag, start) # can pop from stack in top. order
    distance = {}
    stack.pop() # pop start off the stack - set is distance directly
    distance[start] = 0
    rDag = reverse(dag) # adj. list of reverse(dag) has all in-edges
    while len(stack) > 0:
        v = stack.pop() # next node in top. order
        distance[v] = findShortestPath(rDag, v, distance)
    return distance


