# Adjacency lists implemented using a Python dictionary

westernCanadaAdjList =  {  'BC': ['AB'],
                           'AB': ['BC', 'SK'],
                           'SK': ['AB', 'MB'],
                           'MB': ['SK']
                        }

def printNames(graph):
    for node in graph:
        print node

def printNeighbors(node, graph):
    for neighbor in graph[node]:
        print neighbor

def printAllNeighbors(graph):
    for node in graph:
        print "Neighbors of node", node, ":"
        printNeighbors(node, graph)

def printDegrees(graph):
    print "Node degrees:"
    for node in graph:
        print len(graph[node])

printNames(westernCanadaAdjList)
printAllNeighbors(westernCanadaAdjList)
printDegrees(westernCanadaAdjList)
