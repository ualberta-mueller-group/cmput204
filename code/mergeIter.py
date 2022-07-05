from collections import deque

# note: in book, append is called "inject", and popleft is called "eject"
# note: deque is used here as a FIFO queue, first in - first out

def merge(x,y):
    if len(x) == 0: return y
    if len(y) == 0: return x
    if x[0] <= y[0]:
        return x[0:1] + merge(x[1:], y)
    else:
        return y[0:1] + merge(x, y[1:])

def mergesort(a):
    q = deque()
    for i in range(len(a)):
        q.append([a[i]])
    while len(q) > 1:
        a1 = q.popleft()
        a2 = q.popleft()
        q.append(merge(a1,a2))
    return q.popleft()
