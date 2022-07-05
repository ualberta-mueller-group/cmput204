def printbit(b):
    assert b >= 0
    assert b <= 1
    if (b==0):
        return '0'
    else:
        return '1'

def binaryprint(n):
    assert n >= 0
    if (n <= 1):
        return printbit(n)
    else:
        return binaryprint(n // 2) + printbit(n % 2)

def testbit():
    for b in range(2):
        print("Bit", b, printbit(b))

def test():
    testbit()
    for n in range(20):
        print("Decimal", n, "in binary:", binaryprint(n))
    print("2**100",binaryprint(2**100))
