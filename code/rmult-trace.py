def rmult(x,y):
  print("Multiply",x,y)
  assert x >= 0
  assert y >= 0
  if y == 0:
    res = 0
  elif 0 == y % 2:
    res = rmult(x, y // 2)
    print("Computing 2 *", res)
    res = 2 * res
  else:
    res = rmult(x, y // 2)
    print("Computing 2 *", res, "+", x)
    res = 2 * res + x
  print("Result", res)
  return res
