# dfs, depth-first search with timestamps for pre-and postvisits

def previsit(node):
    global clock
    pre[node] = clock
    clock += 1

def postvisit(node):
    global clock
    post[node] = clock
    clock += 1

def explore(graph, node, visited):
    visited[node] = True
    previsit(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            explore(graph, neighbor, visited)
    postvisit(node)

def dfs(graph):
    global pre, post, clock
    pre = {}
    post = {}
    clock = 1
    visited = {}
    for node in graph:
        visited[node] = False
    for node in graph:
        if not visited[node]:
            explore(graph, node, visited)
    print ("Timestamps:")
    for node in graph:
        print (node, '[', pre[node], ':', post[node], ']')


