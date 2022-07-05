import random
from gaussmultiply import multiply

# This test takes about 8 seconds on my laptop
for n in range(2,1000):
    for _ in range(10): # repeat each test 10 times
        x = random.randrange(1 << n) # random number up to n-1 bits
        y = random.randrange(1 << n)
        m = multiply(x,y)
        assert m == x*y # compare with Python's built-in multiply
