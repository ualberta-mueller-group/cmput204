def mr(x,y):
  print(x, y)
  if (x==0):
    return 0
  z = mr(x//2,y)
  if (1==x%2):
    return z + z + y
  return z + z
