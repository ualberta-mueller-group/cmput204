from reverse import reverse
from directedGraphs import simple, bookfigure3point7

def testReverse(graph):
    print ("The reverse of graph", graph)
    print ("is", reverse(graph))

testReverse(simple)
testReverse(bookfigure3point7)

