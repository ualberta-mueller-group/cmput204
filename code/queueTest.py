from collections import deque

def printQueue(q):
    print("Queue is now", q)

q = deque()
printQueue(q)
q.append('A')
printQueue(q)
q.append('B')
printQueue(q)
q.append('C')
printQueue(q)

while len(q) > 0:
    element = q.popleft();
    print ("Processing", element)
    printQueue(q)
