def euclid(a, b):
  assert b >= 0
  if b == 0:
    return a
  return euclid(b, a % b)