# Implements the Bellman-Ford algorithm for shortest paths 
# It works as long as the graph has no negative cycles.

from sys import maxsize
from edgeWithLength import otherEnd, length

def update(distance, previous, u, v, length_uv):
    if distance[v] > distance[u] + length_uv:
        print("Updating distance to", v, "from", distance[v], "to", distance[u] + length_uv)
        distance[v] = distance[u] + length_uv
        previous[v] = u

def bellmanFord(graph, start):
    distance = {}
    previous = {}
    for node in graph:
        distance[node] = maxsize # a very large number used for "infinity"
        previous[node] = 'nil'
    distance[start] = 0
    for _ in range(len(graph) - 1):
        for u in graph:
            for edge in graph[u]:
                length_uv = length(edge)
                v = otherEnd(edge)
                update(distance, previous, u, v, length_uv)
    return (distance, previous)
    