from extendedeuclid import extendedeuclid

def mulinv(a, N):
    assert a >= 0
    assert a < N
    assert N > 0
    x, y, d = extendedeuclid(a, N)
    if d > 1:
        print ("Inverse does not exist")
        return 0
    r = x % N
    assert r >= 0
    assert r < N
    assert (a * r) % N == 1
    return r
