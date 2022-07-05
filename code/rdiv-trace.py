def rdiv(x, y):
  assert y >= 1
  assert x >= 0
  print ('rdiv(',x,',',y,')')
  if x == 0:
    return 0, 0
  q, r = rdiv(x // 2, y)
  q, r = 2 * q, 2 * r
  if 1 == x % 2:
    r = r + 1
  if r >= y:
    q, r = q + 1, r - y
  print (x, '=', q, '*', y, '+', r)
  return q, r
