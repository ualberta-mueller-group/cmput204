def extendedeuclid(a,b):
  assert b >= 0
  if b == 0:
    return 1, 0, a
  x, y, d = extendedeuclid(b, a % b)
  return y, x - (a // b) * y, d
