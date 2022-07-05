# Implements Dijkstra's algorithm, and keeps track of 
# shortest path information through "previous" links
# The graph may not contain a node named 'nil'.

import pq as priorityQueue
from sys import maxsize
from edgeWithLength import otherEnd, length

def dijkstra(graph, start):
    distance = {}
    for node in graph:
        distance[node] = maxsize # a very large number used for "infinity"
    distance[start] = 0
    previous = {}
    previous[start] = 'nil'
    q = priorityQueue.makeQueue(distance) 
    # priority queue using distance-values as keys
    while len(q) > 0:
        (value, u) = priorityQueue.deletemin(q)
        for edge in graph[u]:
            l = length(edge)
            v = otherEnd(edge)
            if distance[v] > distance[u] + l:
                distance[v] = distance[u] + l
                previous[v] = u
                priorityQueue.decreasekey(q, v, distance[v])
                print ("Decreasekey for", v, "to", distance[v])
    #print ("Dijkstra from", start, ":")
    #print ("Distances:", distance)
    #print ("Previous:", previous)
    #return distance
    return (distance, previous)
    