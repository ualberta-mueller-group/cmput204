from scc import scc
from reverse import reverse
from directedGraphs import simple, bookfigure3point7, bookfigure3point8, bookfigure3point9, bookfigure3point10

print ("\nscc for simple graph:")
scc(simple)

print ("\nscc for textbook figure 3.7:")
scc(bookfigure3point7)

print ("\nscc for textbook figure 3.8:")
scc(bookfigure3point8)

print ("\nscc for textbook figure 3.9:")
scc(bookfigure3point9)

print ("\nscc for textbook figure 3.10:")
scc(bookfigure3point10)
