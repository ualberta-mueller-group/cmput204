# This example extends the multiply function from gaussmultiply.py
# to return both the result and the number of recursive calls.
# mul() is a simple wrapper function that only returns the number of calls

def split(x, n): # returns two about n/2 bit numbers
    left  = x >> n//2
    right = x - (left << n//2)
    return left, right

def multiply(x, y):
    count = 1 # count this call
    assert x >= 0
    assert y >= 0
    xbits = x.bit_length()
    ybits = y.bit_length()
    n = max(xbits, ybits)
    limit = 32 # Use direct multiply for small numbers
    if n <= limit:
        #print ("multiply",x,y, "=",x*y, "count = ", count)
        return x * y, count
    xl,xr = split(x, n)
    yl,yr = split(y, n)
    r1, count1 = multiply(xl, yl)
    r3, count3 = multiply(xr, yr)
    r2, count2 = multiply(xl + xr, yl + yr)
    r2 = r2 - r1 - r3
    n2 = n//2
    r = (r1 << (2*n2)) + (r2 << n2) + r3
    count += count1 + count2 + count3
    #print ("multiply",x,y, "=",r, "count = ", count)
    return r, count

def mul(x, y):
    r,count = multiply(x, y)
    return count
