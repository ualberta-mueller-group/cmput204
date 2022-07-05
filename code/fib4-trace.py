import time

def fib(n):
    return f[n]

now = time.time()
f = [0,1]
for n in range(2, 10):
    print(n,f)
    f.append(fib(n-1) + fib(n-2))

