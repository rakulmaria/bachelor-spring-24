from manim import *
from src.vertices_examples import VerticesExamples
from src.vertex import Vertex


def getGraphAsMobjects():
    vertices, edges, capacities = VerticesExamples.SedgewickWayne()
    graph = Graph(vertices, edges)

    verticesAsObjects = {}
    # edgesAsObjects = {}

    for dot, i in enumerate(graph.vertices):
        x, y, _ = graph._layout[dot]

        vertex = Vertex(i, x, y)
        verticesAsObjects.update(vertex)

    for line in graph.edges:
        print(line)

    # for vertex in verticesAsObjects:
    #     print(vertex.id, vertex.x_coord, vertex.y_coord)

    return verticesAsObjects
