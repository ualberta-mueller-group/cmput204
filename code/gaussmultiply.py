def split(x, n): # returns two about n/2 bit numbers
    assert x >= 1
    nx = x.bit_length()
    assert nx <= n
    left  = x >> n//2
    right = x - (left << n//2) # slow, could be faster with low-level access
    assert right < 1 << (n//2)
    #print ("split", bin(x), "into", bin(left), bin(right))
    assert left.bit_length() <= (n+1)//2
    assert right.bit_length() <= n//2
    assert left*pow(2,n//2) + right == x
    return left, right

def multiply(x,y):
    print(bin(x),bin(y))
    assert x >= 0
    assert y >= 0
    xbits = x.bit_length()
    ybits = y.bit_length()
    n = max(xbits, ybits)
    limit = 32 # Use direct multiply for small numbers
    if n <= limit:
        return x * y
    xl,xr = split(x, n)
    yl,yr = split(y, n)
    r1 = multiply(xl, yl)
    r3 = multiply(xr,yr)
    r2 = multiply(xl+xr, yl+yr) - r1 - r3 # Gauss trick
    n2 = n//2 # floor(n/2) in integer arithmetic
    return (r1 << (2*n2)) + (r2 << n2) + r3
