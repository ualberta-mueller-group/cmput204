# bfs, breadth-first search

from collections import deque
from sys import maxsize

def bfs(graph, distance, queue):
    while len(queue) > 0:
        node = queue.popleft();
        print ("node", node, "at distance", distance[node])
        d = distance[node] + 1 # neighbors are 1 further away
        for neighbor in graph[node]:
            if distance[neighbor] == maxsize:
                queue.append(neighbor)
                distance[neighbor] = d

def breadthFirstSearch(graph, start):
    distance = {}
    for node in graph:
        distance[node] = maxsize # a very large number used for "infinity"
    print ("starting bfs from", start)
    queue = deque()
    queue.append(start)
    distance[start] = 0
    bfs(graph, distance, queue)
