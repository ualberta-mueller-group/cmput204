# Classical implementation of adjacency lists using an index
# into a Python list for representing each node,
# and a separate list westernCanadaNames with node information.

def printNames(names):
    for name in names:
        print name

def printNeighbors(nodeAdjList, names):
    for index in nodeAdjList:
        print names[index]

def printAllNeighbors(graphAdjList, names):
    for index in range(len(graphAdjList)):
        print "Neighbors of node", index, "=", names[index], ":"
        printNeighbors(graphAdjList[index], names)

def printDegrees(graphAdjList):
    print "Node degrees:"
    for nodeAdjList in graphAdjList:
        print len(nodeAdjList)

# Indices of nodes:
# BC = node 0
# AB = node 1
# SK = node 2
# MT = node 3
westernCanadaNames = ['BC','AB', 'SK', 'MT']
westernCanadaAdjList = [ [1],   # List of neighbors of BC
                         [0,2], # List of neighbors of AB
                         [1,3], # List of neighbors of SK
                         [2]    # List of neighbors of MT
                       ]

printNames(westernCanadaNames)
printAllNeighbors(westernCanadaAdjList, westernCanadaNames)
printDegrees(westernCanadaAdjList)
