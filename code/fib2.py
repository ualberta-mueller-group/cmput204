import time

def fib(n):
  a,b = 0,1
  for i in range(n):
    a, b = b, a+b
  return a

for n in range(100):
    now = time.time()
    fn = fib(n)
    used = time.time() - now
    print("fib(", n, ") =", fn, ", time used =", used, "sec")
