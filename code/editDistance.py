def letterOf(word, i): #letter array is 0-based, so subtract 1
    assert i >= 1
    assert i <= len(word)
    return word[i-1]

def addDistance(E, i, j):
    return 1 + E[i][j-1]

def deleteDistance(E, i, j):
    return 1 + E[i-1][j]

# handles both cases change and no change, as in textbook
def changeDistance(E, i, j, word1, word2):
    assert i >= 1
    assert j >= 1
    if letterOf(word1, i) == letterOf(word2, j):
        diff = 0
    else:
        diff = 1
    return diff + E[i-1][j-1]

def minDistance(E, i, j, word1, word2):
    return min(  addDistance(E, i, j),
                 deleteDistance(E, i, j),
                 changeDistance(E, i, j, word1, word2)
              )

def editDistance(word1, word2):
    m = len(word1)
    n = len(word2)
    E = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m+1):
        E[i][0] = i
    for j in range(n+1):
        E[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            E[i][j] = minDistance(E, i, j, word1, word2)
    for i in range(m+1):
        print (E[i])
    return E[m][n]
