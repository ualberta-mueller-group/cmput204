# Connected components of a graph with dfs

def previsit(node):
    global cc
    global ccnum
    ccnum[node] = cc

def postvisit(node):
    pass # nothing to do

def explore(graph, node, visited):
    visited[node] = True
    previsit(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            explore(graph, neighbor, visited)
    postvisit(node)

def printComponent(ccnum, i):
    print("Component",i)
    for node in ccnum:
        if ccnum[node] == i:
            print(node)

def dfs(graph):
    global ccnum, cc
    ccnum = {} # used to store cc information for each node
    cc = 0 # a number to be used to represent the connected component of each node
    visited = {}
    for node in graph:
        visited[node] = False
    for node in graph:
        if not visited[node]:
            cc += 1
            explore(graph, node, visited)
    print ("This graph has", cc, "components:", ccnum)
    for i in range(1, cc + 1):
        printComponent(ccnum, i)

