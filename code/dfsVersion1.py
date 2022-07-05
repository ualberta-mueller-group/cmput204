# Version 1 of dfs, depth-first search
# Correct algorithm, easy to implement, but uses inefficient list
# to represent visited nodes

from undirectedGraphs import westernCanada, westernCanadaPlus2, bookFigure3Point2

def explore(graph, node, visited):
    visited.append(node)
    print("explore from", node, "visited", visited)
    for neighbor in graph[node]:
        if not neighbor in visited:
            explore(graph, neighbor, visited)
    print("done exploring from", node)

def dfs(graph):
    visited = []
    for node in graph:
        if not node in visited:
            print("Exploring a new component")
            explore(graph, node, visited)
            print("Done exploring this component")

print("dfs westernCanada")
dfs(westernCanada)

print("\n\ndfs westernCanadaPlus2")
dfs(westernCanadaPlus2)

print("\n\ndfs bookFigure3Point2")
dfs(bookFigure3Point2)
