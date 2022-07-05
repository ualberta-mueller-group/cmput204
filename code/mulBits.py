# Similar to mulCalls.py, but prints full histogram of how many
# numbers of each bit length were multiplied in all calls
# Use mul(x,y) to create the histogram for multiplication of x and y

def split(x, n):
    left  = x >> n//2
    right = x - (left << n//2)
    return left, right

def addhistogram(n):
    histogram[n] = histogram.get(n,0) + 1

def multiply(x,y):
    assert x >= 0
    assert y >= 0
    xbits = x.bit_length()
    ybits = y.bit_length()
    addhistogram(xbits)
    addhistogram(ybits)
    n = max(xbits, ybits)
    limit = 1 # Use direct multiply for small numbers
    if n <= limit:
        return x * y
    xl,xr = split(x, n)
    yl,yr = split(y, n)
    r1 = multiply(xl, yl)
    r3 = multiply(xr,yr)
    r2 = multiply(xl+xr, yl+yr)
    r2 = r2 - r1 - r3 # Gauss trick
    n2 = n//2
    r = (r1 << (2*n2)) + (r2 << n2) + r3
    return r

histogram = {0:0} # Python dictionary - here, map number-of-bits to count

def mul(x,y):
    histogram.clear()
    r = multiply(x,y)
    for e in sorted(histogram): print (e, "bits: count =", histogram[e])
