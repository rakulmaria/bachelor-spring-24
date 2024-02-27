from manim import *
from src.flow import BackgroundGraph, ArrowGraph, GraphLabel
from src.edge import Edge
from src.vertex import Vertex


class Graph1(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.camera.frame_width = 25
        self.camera.resize_frame_shape(0)
        self.edges = {}
        self.vertices = {}
        self.add_vertices(
            [
                ["vertex0", 0, 6],
                ["vertex1", -4, 2],
                ["vertex2", 4, 2],
                ["vertex3", -4, -2],
                ["vertex4", 4, -2],
                ["vertex5", 0, -6],
            ]
        )

        self.add_edges(
            [
                ["edge0_to_1", self.vertices["vertex0"], self.vertices["vertex1"], 2],
                ["edge0_to_2", self.vertices["vertex0"], self.vertices["vertex2"], 3],
                ["edge1_to_3", self.vertices["vertex1"], self.vertices["vertex3"], 3],
                ["edge1_to_4", self.vertices["vertex1"], self.vertices["vertex4"], 1],
                ["edge2_to_3", self.vertices["vertex2"], self.vertices["vertex3"], 1],
                ["edge2_to_4", self.vertices["vertex2"], self.vertices["vertex4"], 1],
                ["edge3_to_5", self.vertices["vertex3"], self.vertices["vertex5"], 3],
                ["edge4_to_5", self.vertices["vertex4"], self.vertices["vertex5"], 3],
            ]
        )

        g = BackgroundGraph(self.edges.values())
        a = ArrowGraph(self.edges.values())
        graghLabel = GraphLabel(self.vertices.values())

        self.add(g)
        self.add_foreground_mobject(a)
        self.add_foreground_mobject(graghLabel)

    def add_edges(self, lst):
        for id, start_node, end_node, max_capacity in lst:
            self.edges[id] = Edge(id, start_node, end_node, max_capacity)

    def add_vertices(self, lst):
        for id, x_coord, y_coord in lst:
            self.vertices[id] = Vertex(id, x_coord, y_coord)
