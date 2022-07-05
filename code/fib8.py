fib_memo = {}
NO_RESULT = -1

def lookup(n):
    if n in fib_memo:
        print ("Lookup of", n, "succeeded")
        return fib_memo[n]
    else:
        print ("Lookup of", n, "failed")
        return NO_RESULT

def store(n, result):
    assert(not n in fib_memo)
    fib_memo[n] = result

def fib(n):
    print ("Computing fib(",n,")")
    if (n<=1):
        print ("Computed result of fib(",n,")")
        return n
    result = lookup(n)
    if result == NO_RESULT:
        result = fib(n-1) + fib(n-2)
        print ("Computed result of fib(",n,")")
        store(n, result)
    return result 
