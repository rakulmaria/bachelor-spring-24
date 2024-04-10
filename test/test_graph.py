from manim import *
from flow_network import FlowNetwork
from src.vertices_examples import VerticesExamples as V


class Test_Graph(Scene):
    def construct(self):
        vertices, edges, capacities, source, sink = V.sedgewick_wayne()
        graph = FlowNetwork(vertices, edges, capacities, source, sink)
        self.camera.background_color = WHITE

        self.add(graph)
