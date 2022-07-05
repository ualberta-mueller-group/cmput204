# Neat trick from http://stackoverflow.com/questions/14822184/
# is-there-a-ceiling-equivalent-of-operator-in-python
def ceiling(x, y):
    return - (-x // y)

def dc(n, a, b, calls, level):
    assert b >= 2
    print ("  " * level, calls, "calls for n=", n)
    if (n == 1):
        print ("bottom of recursion for n=1")
        return calls
    else:
      n1 = ceiling(n,b)
      recursiveCalls = dc(n1, a, b, a * calls, level + 1)
      return calls + recursiveCalls

def dcsimulator(n, a, b):
    calls = dc(n, a, b, 1, 0)
    print("Total number of calls:", calls)
