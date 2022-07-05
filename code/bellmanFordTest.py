from sampleGraphsWithNegativeLengths import abc, bookFigure4point14
from bellmanFord import bellmanFord

def printResult(algorithm, result, start):
    print("Running", algorithm)
    distances = result[0]
    previous = result[1]
    print("Shortest distances from", start)
    print(distances)
    print("Previous links", previous)
    
printResult("BellmanFord", bellmanFord(abc, 'A'), 'A')
printResult("BellmanFord", bellmanFord(bookFigure4point14, 'S'), 'S')
