# Basic dfs, depth-first search with print statements at pre-and postvisits

def previsit(node):
    print ("Explore from", node)

def postvisit(node):
    print ("Done exploring from", node)

def explore(graph, node, visited):
    visited[node] = True
    previsit(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            explore(graph, neighbor, visited)
    postvisit(node)

def dfs(graph):
    visited = {}
    for node in graph:
        visited[node] = False
    for node in graph:
        if not visited[node]:
            print ("Explore new component from", node)
            explore(graph, node, visited)
            print ("Done exploring component from", node, "\n")
