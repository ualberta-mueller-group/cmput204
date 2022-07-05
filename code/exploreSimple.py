# First try at depth-first search. Runs into an infinite loop.
# Also see explore-simple2.py.

from undirectedGraphs import westernCanada

def dfs(graph, node):
    print ("dfs from", node)
    for neighbor in graph[node]:
        dfs(graph, neighbor)

dfs(westernCanada, 'AB')