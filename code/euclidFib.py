import euclidTrace

def fib(n):
    a,b = 0,1
    for i in range(n):
        a, b = b, a+b
    return a

for i in range(21):
    print (fib(i))

euclidTrace.euclid(fib(19),fib(20))
