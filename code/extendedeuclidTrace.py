def extendedeuclid(a,b):
  assert b >= 0
  print ("Call extendedeuclid(", a, ",", b, ")")
  if b == 0:
    print (a, "* 1 +", b, "* 0 =", a)
    return 1, 0, a
  x, y, d = extendedeuclid(b, a % b)
  x, y = y, x - (a // b) * y
  print (a, "*", x, "+", b, "*", y, "=", d)
  return x, y, d
