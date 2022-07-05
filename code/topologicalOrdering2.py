# dfs, depth-first search for topological ordering
# Version 2, for case where adjacency list has edges with lengths
# Otherwise, the algorithm is identical to topologicalOrdering.py

from edgeWithLength import otherEnd, length

def previsit(node):
    pass

def postvisit(node):
    global result
    result.append(node)

def explore(graph, node, visited):
    visited[node] = True
    previsit(node)
    for edge in graph[node]:
        neighbor = otherEnd(edge)
        if not visited[neighbor]:
            explore(graph, neighbor, visited)
    postvisit(node)

def initVisited(graph, visited):
    for node in graph:
        visited[node] = False

def dfs(graph):
    visited = {}
    initVisited(graph, visited)
    global result
    result = []
    for node in graph:
        if not visited[node]:
            explore(graph, node, visited)
    return result

def dfsSingleSource(graph, start):
    visited = {}
    initVisited(graph, visited)
    global result
    result = []
    explore(graph, start, visited)
    return result
