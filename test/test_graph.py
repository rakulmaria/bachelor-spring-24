from manim import *
from src.network import Network
from src.vertices_examples import VerticesExamples as V


class Test_Graph(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.sedgewick_wayne()
        graph = Network(vertices, edges, capacities, source, sink)
        self.camera.background_color = WHITE

        self.add(graph)
