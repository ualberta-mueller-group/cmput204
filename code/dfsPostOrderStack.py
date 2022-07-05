# uses dfs to create a stack of all nodes in postorder

def previsit(node):
    pass

def postvisit(node):
    global stack
    stack.append(node)

def explore(graph, node, visited):
    visited[node] = True
    previsit(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            explore(graph, neighbor, visited)
    postvisit(node)

def dfsPostOrderStack(graph):
    global stack
    stack = []
    visited = {}
    for node in graph:
        visited[node] = False
    for node in graph:
        if not visited[node]:
            explore(graph, node, visited)
    return stack

