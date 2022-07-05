# mergesort implementation, close to textbook version p.50

def merge(x,y):
    if len(x) == 0: return y
    if len(y) == 0: return x
    if x[0] <= y[0]:
        return x[0:1] + merge(x[1:], y)
    else:
        return y[0:1] + merge(x, y[1:])

def ms(a, start, end): # sort a[start]..a[end - 1]
    assert start < end
    if start == end - 1: # single element, is sorted
        return a[start:end]
    mid = (start + end)//2
    return merge(ms(a, start, mid), ms(a, mid, end))

def mergesort(a):
    return ms(a, 0, len(a))
