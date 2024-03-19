from manim import *
from src.vertices_examples import VerticesExamples
from src.vertex import Vertex


def getGraphAsMobjects():
    vertices, edges = VerticesExamples.SedgewickWayne()
    graph = Graph(vertices, edges)

    verticesAsObjects = []

    for dot, i in enumerate(graph.vertices):
        x, y, _ = graph._layout[dot]

        vertex = Vertex(i, x, y)
        verticesAsObjects.append(vertex)

    for vertex in verticesAsObjects:
        print(vertex.id, vertex.x_coord, vertex.y_coord)

    return verticesAsObjects
