def euclid(a,b):
  assert b >= 0
  print ('gcd(', a, ',', b, ') =')
  if b == 0:
    print ('    ',a)
    return a
  else:
    return euclid(b, a % b)
