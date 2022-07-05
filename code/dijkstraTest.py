import sampleGraphsWithLengths as samples
from dijkstra import dijkstra

def printResult(result, start):
    distances = result[0]
    previous = result[1]
    print("Shortest distances from", start)
    print(distances)
    print("Previous links", previous)
    
# Note: this runs Dijkstra, then prints out the result,
# which is the dictionary with all shortest distances
printResult(dijkstra(samples.abc, 'A'), 'A')
printResult(dijkstra(samples.westernCanada, 'AB'), 'AB')
printResult(dijkstra(samples.book, 'A'), 'A')
printResult(dijkstra(samples.book, 'E'), 'E')
printResult(dijkstra(samples.ryansExample, 'A'), 'A')
printResult(dijkstra(samples.dijkstraBadCase, 'A'), 'A')