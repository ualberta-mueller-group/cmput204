#from unionFindVersion1 import initializeUnionFindForGraph, union, find, printRank
#from unionFindVersion2 import initializeUnionFindForGraph, union, find, printRank
from unionFindVersion3 import initializeUnionFindForGraph, union, find, printRank

import sampleGraphsWithLengths as samples

parent = initializeUnionFindForGraph(samples.undirectedAB)
print (parent, find(parent, 'A'), find(parent, 'B'))
union(parent, 'A', 'B')
print (parent, find(parent, 'A'), find(parent, 'B'))
printRank(samples.undirectedAB, parent)

parent = initializeUnionFindForGraph(samples.ryansExample)
print (parent, find(parent, 'A'), find(parent, 'B'))
printRank(samples.ryansExample, parent)
union(parent, 'A', 'B')
union(parent, 'C', 'A')
union(parent, 'D', 'A')
union(parent, 'E', 'A')
print (parent, find(parent, 'A'), find(parent, 'B'))
printRank(samples.ryansExample, parent)
