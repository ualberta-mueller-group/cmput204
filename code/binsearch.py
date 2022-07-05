# A simple example showing how to use binary search in Python
# to find the index of elements in a sorted sequence.

import bisect

sortedmarks = [3, 5, 12, 22, 22, 23, 26, 30, 31, 33, 46, 46, 48, 48, 49, 50, 50, 50]

i = bisect.bisect_left(sortedmarks, 30)
print (i, sortedmarks[i])

j = bisect.bisect_left(sortedmarks, 50)
print (j, sortedmarks[j])
