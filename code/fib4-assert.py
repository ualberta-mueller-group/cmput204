import time

def fib(n):
    return f[n]

now = time.time()
f = [0,1]
for n in range(2, 100):
    assert len(f) == n
    f.append(fib(n-1) + fib(n-2))
print ("Precomputation time used =", time.time() - now, "sec\n")

for n in range(100):
    now = time.time()
    fn = fib(n)
    print ("fib(", n, ") =", fn, ", time used =", time.time() - now, "sec")
