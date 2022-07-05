# Union-find with union-by-rank

def makeset(parent, node):
    parent[node] = node
    global rank
    rank[node] = 0

def find(parent, node):
    while parent[node] != node:
        node = parent[node]
    return node

def union(parent, x, y):
    global rank
    xRep = find(parent, x)
    yRep = find(parent, y)
    if xRep != yRep:
        if rank[xRep] > rank[yRep]:
            parent[yRep] = xRep
        else:
            parent[xRep] = yRep
            if rank[xRep] == rank[yRep]:
                rank[yRep] += 1

# below here is specific for graphs

def initializeUnionFindForGraph(graph):
    parent = {}
    global rank
    rank = {}
    for node in graph:
        makeset(parent, node)
    return parent

def printRank(graph, parent):
    global rank
    print (rank)