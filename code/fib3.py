import time

def fib(n):
  a,b = 0,1
  for i in range(n):
    a, b = b, a+b
  return a

n = 10000
for i in range(8):
  now = time.time()
  fn = fib(n)
  print ("= fib(", n, "), time used =", time.time() - now, "sec\n")
  n *= 2
