# A good version of dfs exploration which keeps track of visited nodes
# For simplicity, uses a list for visited.
# Testing whether nodes are in visited will be slow for large graphs.
# Use boolean arrays for efficiency if needed.

from undirectedGraphs import westernCanada

def explore(graph, node, visited):
    visited.append(node)
    print ("explore from", node, ", visited", visited)
    for neighbor in graph[node]:
        if neighbor in visited:
            print("Skip neighbor", neighbor, "of", node, ", already visited")
        else:
            explore(graph, neighbor, visited)
    print ("done exploring from", node)

explore(westernCanada, 'AB', [])

#explore(westernCanada, 'MB', [])