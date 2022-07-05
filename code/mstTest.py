import sampleGraphsWithLengths as samples
from mstKruskal import minimumSpanningTree

mst = minimumSpanningTree(samples.abcundirected)
print (mst)

mst = minimumSpanningTree(samples.westernCanada)
print (mst)

mst = minimumSpanningTree(samples.bookundirected)
print (mst)

mst = minimumSpanningTree(samples.ryansExample)
print (mst)

