def longestIncreasingSubsequence(a):
    L = []
    for j, aj in enumerate(a):
        maxL = 0
        for i, ai in enumerate(a[:j]):
            if ai < aj:
                if L[i] > maxL:
                    maxL = L[i]
        L.append(1 + maxL)
    #print (L)
    return max(L)
