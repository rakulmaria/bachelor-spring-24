from manim import *
from src.vertex import Vertex
from src.edge import Edge


def getGraphAsMobjects(graphData, layout_scale=2, layout="spring"):
    vertices, edges, capacities = graphData
    graph = Graph(vertices, edges, layout_scale=layout_scale, layout=layout)

    verticesAsObjects = {}
    edgesAsObjects = []

    for dot, i in enumerate(graph.vertices):
        x, y, _ = graph._layout[dot]

        vertex = Vertex(i, x, y, 1)
        verticesAsObjects.update({i: vertex})

    for _from, to, capacity in capacities:
        edge = Edge(verticesAsObjects.get(_from), verticesAsObjects.get(to), capacity)
        edgesAsObjects.append(edge)

    return verticesAsObjects.values(), edgesAsObjects
