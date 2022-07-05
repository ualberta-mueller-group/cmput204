import sampleGraphsWithNegativeLengths as samples
from bellmanFord import bellmanFord
from dijkstra import dijkstra

def printResult(algorithm, result, start):
    print("Running", algorithm)
    distances = result[0]
    previous = result[1]
    print("Shortest distances from", start)
    print(distances)
    print("Previous links", previous)
    
# Note: this runs Dijkstra, then prints out the result,
# which is the dictionary with all shortest distances
printResult("Dijkstra", dijkstra(samples.bookFigure4point12, 'S'), 'S')
printResult("BellmanFord", bellmanFord(samples.bookFigure4point12, 'S'), 'S')
printResult("Dijkstra", dijkstra(samples.dijkstraFail, 'S'), 'S')
printResult("BellmanFord", bellmanFord(samples.dijkstraFail, 'S'), 'S')
printResult("Dijkstra", dijkstra(samples.bookFigure4point14, 'S'), 'S')
printResult("BellmanFord", bellmanFord(samples.bookFigure4point14, 'S'), 'S')

from sampleGraphsWithNegativeLengths import abc, bookFigure4point14

    