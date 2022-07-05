fib_memo = {}
def fib(n):
  if (n<=1):
    return n
  if not n in fib_memo:
    fib_memo[n] = fib(n-1) + fib(n-2)
  return fib_memo[n]
