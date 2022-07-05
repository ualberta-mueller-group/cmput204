# Version 2 of dfs, depth-first search
# The regular version of dfs uses an efficient array of booleans
# to represent visited nodes
# This Python code just uses a dictionary, amortized O(1) visited test

from undirectedGraphs import westernCanada, westernCanadaPlus2, bookFigure3Point2

def explore(graph, node, visited):
    visited[node] = True
    print ("explore from", node, "visited", visited)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            explore(graph, neighbor, visited)
    print ("done exploring from", node)

def dfs(graph):
    visited = {}
    for node in graph:
        visited[node] = False
    for node in graph:
        if not visited[node]:
            print ("Exploring a new component")
            explore(graph, node, visited)
            print ("Done exploring this component")

print("dfs westernCanada")
dfs(westernCanada)

print("\n\ndfs westernCanadaPlus2")
dfs(westernCanadaPlus2)

print("\n\ndfs bookFigure3Point2")
dfs(bookFigure3Point2)
