# Simple union-find operations
# NOT efficient, can create long chains of nodes

def makeset(parent, node):
    parent[node] = node

def find(parent, node):
    while parent[node] != node:
        node = parent[node]
    return node

def union(parent, x, y):
    xRep = find(parent, x)
    yRep = find(parent, y)
    if xRep != yRep:
        parent[yRep] = xRep

def rank(parent, node):
    r = 0
    while parent[node] != node:
        node = parent[node]
        r += 1
    return r

# below here is specific for graphs

def initializeUnionFindForGraph(graph):
    parent = {}
    for node in graph:
        makeset(parent, node)
    return parent

def printRank(graph, parent):
    for node in graph:
        print (rank(parent, node))
