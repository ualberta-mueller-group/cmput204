# Pick one application of dfs here.
#from dfs import dfs
from dfsTimestamp import dfs
#from dfsConnectedComponents import dfs

from undirectedGraphs import westernCanadaPlus2, bookFigure3Point2, mostlyDisconnected

print ("dfs for western Canada, plus 2 connected extra nodes XX and YY:")
dfs(westernCanadaPlus2)

print ("\ndfs for textbook figure 3.2:")
dfs(bookFigure3Point2)

print ("\ndfs for mostly disconnected undirected:")
dfs(mostlyDisconnected)
