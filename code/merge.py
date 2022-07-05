def merge(x,y):
    i = 0 # index in x
    j = 0 # index in y
    result = []
    while i < len(x) and j < len(y):
        if x[i] <= y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1
    if i < len(x):
        result += x[i:]
    else:
        result += y[j:]
    return result
