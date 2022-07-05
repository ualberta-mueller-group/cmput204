import sampleGraphsWithLengths as samples
from dijkstra import dijkstra
from dagShortestDistance import dagShortestDistance

print("Dijkstra Shortest Distance:", dijkstra(samples.dijkstraBadCase, 'A'))
print("Dag Shortest Distance:", dagShortestDistance(samples.dijkstraBadCase, 'A'))
