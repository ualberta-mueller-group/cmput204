from extendedeuclid import extendedeuclid

def mulinv(a, N):
    assert a >= 0
    assert a < N
    assert N > 0
    print("multiplicative inverse of", a, "modulo", N)
    x, y, d = extendedeuclid(a, N)
    print((x,y,d))
    if d > 1:
        print ("Inverse does not exist")
        return 0 # or throw an assertion?
    r = x % N
    assert r >= 0
    assert r < N
    assert (a * r) % N == 1
    print("Inverse =", r, "because", a, "*", r, "mod", N, "= 1")
    return r
