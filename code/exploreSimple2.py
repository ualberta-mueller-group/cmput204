# First try at depth-first search. Runs into an infinite loop.
# This version limits the number of dfs calls to 10.

from undirectedGraphs import westernCanada

def dfs(graph, node):
    global limit
    limit -= 1
    if limit <= 0: return
    print ("dfs from", node)
    for neighbor in graph[node]:
        dfs(graph, neighbor)

limit = 10
dfs(westernCanada, 'AB')