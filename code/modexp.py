def modexp(x, y, n): # all integers
    assert y >= 0
    assert n >= 2
    if y == 0:
        return 1
    z = modexp(x, y // 2, n)
    if 0 == y % 2:
        return (z * z) % n
    else:
        return (x * z * z) % n
