import time

def fib(n):
  if (n<=1):
    return n
  return fib(n-1) + fib(n-2)

for n in range(100):
  now = time.time()
  fn = fib(n)
  print("fib(", n, ") =", fn, ", time used =", time.time() - now, "sec")
