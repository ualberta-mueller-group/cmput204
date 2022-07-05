import time
#from heapq import merge
#from merge import merge
from mergesort import merge
import random


def randomlist(length):
    L = []
    for _ in range(length):
        L.append(random.randrange(1000000))
    return L

lastTime = 0
for i in range(1,10):
    length = 1 << i
    x = randomlist(length)
    y = randomlist(length)
    startTime = time.time()
    z = merge(x,y)
    timeUsed = time.time() - startTime
    print ("Length", length, "time", timeUsed)
    if lastTime > 0:
        print ("Ratio", timeUsed / lastTime)
    lastTime = timeUsed

