# graph-tool.skewed.de/
from graph_tool import Graph
from graph_tool import draw

g = Graph(directed=True)

for i in range(5):
    g.add_vertex()

v1 = g.add_vertex()
v2 = g.add_vertex()

v3 = g.vertex(2)

e1 = g.add_edge(v1, v2)
g.add_edge(v1, v3)

draw.graph_draw(g)

