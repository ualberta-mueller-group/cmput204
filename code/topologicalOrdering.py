# dfs, depth-first search

def previsit(node):
    pass

def postvisit(node):
    global result
    result.append(node)

def explore(graph, node, visited):
    visited[node] = True
    previsit(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            explore(graph, neighbor, visited)
    postvisit(node)

def printInReverse(list):
    for node in reversed(list): print(node)

def dfs(graph):
    visited = {}
    for node in graph:
        visited[node] = False
    global result
    result = []
    for node in graph:
        if not visited[node]:
            explore(graph, node, visited)
    print ("Topological ordering of", graph, ":")
    printInReverse(result)
