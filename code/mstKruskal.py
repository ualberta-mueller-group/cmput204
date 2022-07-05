#import unionFindVersion1 as uf
import unionFindVersion3 as uf
from edgeWithLength import otherEnd, length

# edge for sorting, represented as 3-element list [length, u, v]
def endpoint(edge, index):
    assert index >= 1
    assert index <= 2
    return edge[index]

# Generate list of undirected graph edges in format [length, u, v]
# which makes it easy to sort by length
# Only takes edges for which comparison u < v is true
# this avoids duplicates and loops
def extractEdges(graph):
    edges = []
    for node in graph:
        for edge in graph[node]:
            v = otherEnd(edge)
            if node < v:
                edges.append([length(edge), node, v])
    return edges

def sortEdges(graph):
    edges = extractEdges(graph)
    edges.sort()
    return edges

def minimumSpanningTree(graph):
    parent = uf.initializeUnionFindForGraph(graph)
    mst = []
    sortedEdges = sortEdges(graph)
    for edge in sortedEdges:
        u = endpoint(edge, 1)
        v = endpoint(edge, 2)
        if uf.find(parent, u) != uf.find(parent, v):
            mst.append(edge)
            uf.union(parent, u, v)
    return mst