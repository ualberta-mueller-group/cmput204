from bfs import breadthFirstSearch
import directedGraphs, undirectedGraphs

def runBfsFromAllNodes(graph):
    for node in graph:
        breadthFirstSearch(graph, node)

print("All possible bfs for westernCanada")
runBfsFromAllNodes(undirectedGraphs.westernCanada)
print("\nAll possible bfs for bookFigure3Point2")
runBfsFromAllNodes(undirectedGraphs.bookFigure3Point2)
print("\nAll possible bfs for bookfigure3point7")
runBfsFromAllNodes(directedGraphs.bookfigure3point7)