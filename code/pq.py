# Naive priority queue implementation for Dijkstra.
# This uses a list of pairs (distance, node)
# VERY SLOW for larger graphs!!!
# Both deletemin and decreasekey here are O(n)
# Compare with heap implementations, see heap.py

def makeQueue(distance):
    pq = []
    for node in distance:
        pq.append((distance[node], node))
    return pq

def deletemin(pq):
    theMin = min(pq)
    pq.remove(theMin)
    return theMin

def decreasekey(pq, key, value):
    for i in range(len(pq)):
        pair = pq[i]
        if pair[1] == key:
            assert pair[0] > value
            pq[i] = (value, key)
            return
