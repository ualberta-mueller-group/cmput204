def rmult(x,y):
  assert x >= 0
  assert y >= 0
  if y == 0:
    return 0
  elif 0 == y % 2:
    return 2 * rmult(x, y // 2)
  else:
    return x + 2 * rmult(x, y // 2)
