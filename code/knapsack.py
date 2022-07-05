def getelement(array,i):
    assert i >= 1
    assert i <= len(array)
    return array[i-1]

def printK(K):
    for row in K:
        print (row)

def knapsack(W, weights, v):
    n = len(weights)
    assert n == len(v)
    # Need to initialize all K(0, j) = 0 and all K(w, 0) = 0
    # Here I just initialized thee whole 2-d "array"
    K = [[0 for j in range(n+1)] for i in range(W+1)]
    for j in range(1, n+1):
        wj = getelement(weights, j)
        #print ("j, wj = ", j, wj)
        for w in range(1, W+1):
            withoutItemJ = K[w][j-1]
            #print ("w = ", w, "without wj = ", withoutItemJ)
            if wj > w:
                K[w][j] = withoutItemJ
            else:
                withItemJ = getelement(v, j) + K[w - wj][j-1]
                #print ("w = ", w, "with wj = ", withItemJ)
                K[w][j] = max(withoutItemJ, withItemJ)
    #printK(K)
    return K[W][n]