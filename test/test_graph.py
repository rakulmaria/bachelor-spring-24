from manim import *
from src.graph import FlowGraph
from src.vertices_examples import VerticesExamples as V


class Test_Graph(Scene):
    def construct(self):
        vertices, edges, capacities = V.SedgewickWayne()
        graph = FlowGraph(vertices, edges, capacities)
        self.camera.background_color = WHITE

        self.add(graph)
