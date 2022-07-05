def modexp(x, y, n): # all integers
    assert y >= 0
    assert n >= 2
    print("modexp", x, y, n)
    if y == 0:
        print(1)
        return 1
    z = modexp(x, y // 2, n)
    if 0 == y % 2:
        r = (z * z) % n
    else:
        r = (x * z * z) % n
    print(r)
    return r
