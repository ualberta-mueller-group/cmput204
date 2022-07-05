def isSorted(a):
    for i in range(len(a)-1):
        if a[i] > a[i+1]: return False
    return True
    