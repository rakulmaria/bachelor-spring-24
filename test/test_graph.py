from manim import *
from network import Network
from src.vertices_examples import VerticesExamples as V


class Test_Graph(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.SedgewickWayne()
        graph = Network(vertices, edges, capacities, source, sink)
        self.camera.background_color = WHITE

        self.add(graph)
