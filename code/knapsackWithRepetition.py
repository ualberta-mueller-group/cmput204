def knapsack(weight, w, v):
    K = []
    for W in range(weight+1):
        maxV = 0
        for i, wi in enumerate(w):
            if wi <= W:
                value = v[i] + K[W - wi]
                if value > maxV:
                    maxV = value
        K.append(maxV)
    print (K)
    return K[weight]

