from longestIncreasingSubsequence import longestIncreasingSubsequence

def lisTest(a):
    print ("The longest increasing subsequence of", a,)
    print ("has length", longestIncreasingSubsequence(a))

lisTest([1])
lisTest([1,2])
lisTest([1,2,3])
lisTest([3,2,1])
lisTest([1,2,3,4,3,2,1])
lisTest([4,3,2,1,2,3,4])
lisTest([5,2,8,6,3,6,9,7])
