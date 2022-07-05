# Reverse graph for graph with edge lengths
from edgeWithLength import otherEnd, length, makeEdge

def reverse(graph):
    rGraph = {}
    for node in graph:
        rGraph[node] = [] # initialize adj. lists
    for node in graph:
        for edge in graph[node]:
            neighbor = otherEnd(edge)
            rGraph[neighbor].append(makeEdge(node, length(edge)))
    return rGraph
