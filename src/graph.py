from manim import *
from src.edge import Edge
from src.vertex import Vertex


class FlowGraph(VMobject):
    def __init__(self, vertices, edges):
        super().__init__()
        self.vertices = vertices
        self.edges = edges

        for vertex in vertices:
            self.add(vertex)
            vertex.draw()

        for edge in edges:
            self.add(edge)


class Ex(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame_width = 30
        self.camera.resize_frame_shape(0)
        self.edges = {}
        self.vertices = {}

        self.add_vertices(
            [
                ["vertex0", -5, 0],
                ["vertex1", 0, 5],
                ["vertex2", 0, -5],
                ["vertex3", 5, 0],
            ]
        )

        self.add_edges(
            [
                ["edge0_to_1", self.vertices["vertex0"], self.vertices["vertex1"], 2],
                ["edge0_to_2", self.vertices["vertex0"], self.vertices["vertex2"], 1],
                ["edge1_to_2", self.vertices["vertex1"], self.vertices["vertex2"], 3],
                ["edge1_to_3", self.vertices["vertex1"], self.vertices["vertex3"], 1],
                ["edge2_to_3", self.vertices["vertex2"], self.vertices["vertex3"], 6],
                ["edge0_to_3", self.vertices["vertex0"], self.vertices["vertex3"], 2],
            ]
        )

        graph = Graph(self.vertices.values(), self.edges.values())
        self.add(graph)

    def add_edges(self, lst):
        for id, start_vertex, end_vertex, max_capacity in lst:
            self.edges[id] = Edge(id, start_vertex, end_vertex, max_capacity)

    def add_vertices(self, lst):
        for id, x_coord, y_coord in lst:
            self.vertices[id] = Vertex(id, x_coord, y_coord, 6)
